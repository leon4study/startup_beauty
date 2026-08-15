"""GLOU 설문 QR 생성 — 색감 3종.

기본 사각형 대신 둥근 모듈과 눈(finder) 포인트를 직접 그려서 만든다.
로고를 QR 한가운데 얹는 방식은 쓰지 않는다. 가로형 워드마크라 정사각형에
넣으면 글자가 뭉개지고, 흰 받침을 깔면 스티커처럼 보이기 때문이다.
대신 워드마크는 QR 아래에 비율 그대로 배치한다(카드형).

실행:  python3 qr_gen.py
출력:  out_qr/glou_qr_<이름>.png (QR 단독) + glou_card_<이름>.png (워드마크 포함)
"""

from pathlib import Path

import segno
from PIL import Image, ImageDraw

URL = (
    "https://docs.google.com/forms/d/e/"
    "1FAIpQLScpr4X6pGNZIyUB8Xzy-aJtQaIacxVJYCssCm2H3wNlm8eP0A/viewform"
)
LOGO = Path("glou_img.png")
OUT = Path("out_qr")

# 이름, 배경, 모듈, 눈 바깥, 눈 안쪽
PALETTES = [
    ("copper", "#FFFCF7", "#3B2A20", "#B87333", "#8C5A2B"),
    ("ink", "#FFFFFF", "#1B2A41", "#C58940", "#1B2A41"),
    ("sand", "#FBF7F2", "#4A3B32", "#C97B5A", "#7A4E3B"),
]

MODULE = 16  # 모듈 한 칸 픽셀
QUIET = 4  # 여백 모듈 수 (QR 규격 최소 4)


def finder_cells(n: int) -> set[tuple[int, int]]:
    """세 개 눈(finder pattern)이 차지하는 좌표. 분리자 1칸 포함."""
    cells = set()
    for r0, c0 in [(0, 0), (0, n - 7), (n - 7, 0)]:
        for r in range(r0 - 1, r0 + 8):
            for c in range(c0 - 1, c0 + 8):
                if 0 <= r < n and 0 <= c < n:
                    cells.add((r, c))
    return cells


def rounded(draw, box, radius, fill):
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_eye(draw, r0, c0, outer, inner):
    """눈 하나를 둥근 사각형 3겹으로 그린다."""

    def px(i):
        return (QUIET + i) * MODULE

    # 7x7 바깥 테두리
    rounded(draw, (px(c0), px(r0), px(c0 + 7) - 1, px(r0 + 7) - 1), MODULE * 2, outer)
    # 5x5 배경색으로 파냄
    rounded(
        draw,
        (px(c0 + 1), px(r0 + 1), px(c0 + 6) - 1, px(r0 + 6) - 1),
        int(MODULE * 1.4),
        BG,
    )
    # 3x3 안쪽 점
    rounded(
        draw,
        (px(c0 + 2), px(r0 + 2), px(c0 + 5) - 1, px(r0 + 5) - 1),
        MODULE,
        inner,
    )


def build(name: str, bg: str, dark: str, eye_out: str, eye_in: str) -> Image.Image:
    global BG
    BG = bg

    qr = segno.make_qr(URL, error="h")
    matrix = [list(row) for row in qr.matrix]
    n = len(matrix)
    size = (n + QUIET * 2) * MODULE

    img = Image.new("RGB", (size, size), bg)
    draw = ImageDraw.Draw(img)

    skip = finder_cells(n)
    pad = MODULE * 0.14  # 모듈 사이 숨구멍
    for r in range(n):
        for c in range(n):
            if matrix[r][c] and (r, c) not in skip:
                x = (QUIET + c) * MODULE
                y = (QUIET + r) * MODULE
                draw.ellipse(
                    (x + pad, y + pad, x + MODULE - pad - 1, y + MODULE - pad - 1),
                    fill=dark,
                )

    for r0, c0 in [(0, 0), (0, n - 7), (n - 7, 0)]:
        draw_eye(draw, r0, c0, eye_out, eye_in)

    return img


def knockout_white(im: Image.Image, solid: int = 200, clear: int = 248) -> Image.Image:
    """흰 배경을 투명하게 만든다.

    밝기 solid 이하는 그대로 두고 clear 이상은 완전히 지우며 그 사이는
    부드럽게 이어 준다. 임계값 하나로 자르면 글자 경계에 회색 테두리가
    남아 지저분해지므로 이렇게 처리한다.
    """
    lum = im.convert("L")
    alpha = lum.point(
        lambda v: (
            255 if v <= solid else (0 if v >= clear else int(255 * (clear - v) / (clear - solid)))
        )
    )
    out = im.convert("RGBA")
    out.putalpha(alpha)
    return out


def trim(im: Image.Image) -> Image.Image:
    """투명 여백을 잘라낸다."""
    box = im.getchannel("A").getbbox()
    return im.crop(box) if box else im


def make_card(qr_img: Image.Image, bg: str) -> Image.Image:
    """QR 아래에 워드마크를 비율 그대로 배치한 카드."""
    if not LOGO.exists():
        return qr_img

    logo = trim(knockout_white(Image.open(LOGO)))
    target_w = int(qr_img.width * 0.52)
    ratio = target_w / logo.width
    logo = logo.resize((target_w, int(logo.height * ratio)), Image.Resampling.LANCZOS)

    gap = int(qr_img.width * 0.05)
    bottom = int(qr_img.width * 0.06)
    card = Image.new("RGB", (qr_img.width, qr_img.height + gap + logo.height + bottom), bg)
    card.paste(qr_img, (0, 0))
    card.paste(logo, ((card.width - logo.width) // 2, qr_img.height + gap), logo)
    return card


def verify(path: Path) -> str:
    """생성된 이미지가 실제로 읽히는지 확인한다.

    zbar로 검사한다. opencv의 QRCodeDetector는 둥근 모듈이나 변형된 눈을
    잘 못 읽어서, 멀쩡한 QR도 실패로 보고한다. 실제 휴대폰 스캐너와
    비슷하게 동작하는 zbar 쪽이 판단 기준으로 맞다.
    """
    import os

    os.environ.setdefault("DYLD_LIBRARY_PATH", "/opt/homebrew/lib")
    try:
        from pyzbar.pyzbar import decode
    except Exception:
        return "미검증"

    try:
        found = decode(Image.open(path))
    except Exception:
        return "미검증"
    if not found:
        return "읽기 실패"
    return "정상" if found[0].data.decode() == URL else "다른 값"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name, bg, dark, eo, ei in PALETTES:
        qr_img = build(name, bg, dark, eo, ei)
        p1 = OUT / f"glou_qr_{name}.png"
        qr_img.save(p1)
        p2 = OUT / f"glou_card_{name}.png"
        make_card(qr_img, bg).save(p2)
        print(f"{name:8s} {qr_img.size[0]}px  스캔 {verify(p1):8s} →  {p1.name} / {p2.name}")
    print(f"\n{len(PALETTES)}종 생성 완료: {OUT}/")
    print("인쇄 전 휴대폰으로도 한 번 찍어 볼 것.")


if __name__ == "__main__":
    main()
