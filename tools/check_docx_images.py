"""docx 안 이미지의 인쇄 해상도를 점검한다.

사업계획서를 제출하기 전에 돌린다. 이미지 픽셀 크기와 문서에 실제로
배치된 크기를 비교해 유효 DPI를 계산하고, 기준에 못 미치는 것을 골라
"몇 픽셀로 다시 뽑아야 하는지"까지 알려준다.

배경: 2026-08-14 제출본이 "그림의 글씨가 깨져 보인다"는 피드백을 받았다.
확인해 보니 화면 캡처를 1배 배율로 찍어 넣은 이미지들이 158~222 DPI였다.

사용:
    python3 tools/check_docx_images.py <파일.docx> [--dpi 300]
"""

import argparse
import re
import zipfile
from pathlib import Path

from PIL import Image

EMU_PER_CM = 360000
CM_PER_INCH = 2.54


def collect(path: Path):
    """문서에 놓인 순서대로 (파일명, 픽셀크기, 표시크기cm)를 뽑는다."""
    z = zipfile.ZipFile(path)
    doc = z.read("word/document.xml").decode("utf-8")
    rels = z.read("word/_rels/document.xml.rels").decode("utf-8")
    target = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="media/([^"]+)"', rels))

    # 이미지 하나당 <wp:extent>(표시 크기)와 r:embed(파일 참조)가 짝을 이룬다.
    extents = [(int(a), int(b)) for a, b in re.findall(r'<wp:extent cx="(\d+)" cy="(\d+)"', doc)]
    embeds = re.findall(r'r:embed="(rId\d+)"', doc)

    for (cx, cy), rid in zip(extents, embeds, strict=False):
        name = target.get(rid)
        if not name:
            continue
        try:
            im = Image.open(z.open("word/media/" + name))
        except Exception:
            continue
        yield name, im.size, (cx / EMU_PER_CM, cy / EMU_PER_CM)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("docx", type=Path)
    ap.add_argument("--dpi", type=int, default=300, help="목표 인쇄 해상도 (기본 300)")
    args = ap.parse_args()

    print(f"{'파일':13s} {'픽셀':>12s} {'배치(cm)':>12s} {'DPI':>6s}  {'필요 픽셀':>12s}")
    print("-" * 64)

    low = []
    for name, (pw, ph), (wcm, hcm) in collect(args.docx):
        if wcm <= 0:
            continue
        dpi = pw / (wcm / CM_PER_INCH)
        need_w = round(wcm / CM_PER_INCH * args.dpi)
        need_h = round(hcm / CM_PER_INCH * args.dpi)
        mark = ""
        if dpi < args.dpi:
            mark = f"  {need_w}x{need_h}"
            low.append((name, round(dpi), need_w, need_h, round(need_w / pw, 1)))
        print(f"{name:13s} {pw:5d}x{ph:<6d} {wcm:5.1f}x{hcm:<5.1f} {dpi:6.0f}{mark}")

    print()
    if not low:
        print(f"모든 이미지가 {args.dpi} DPI 이상입니다.")
        return

    print(f"{args.dpi} DPI 미만 {len(low)}개 — 아래 크기로 다시 뽑을 것")
    for name, dpi, w, h, scale in low:
        print(f"  {name:13s} 현재 {dpi:3d} DPI → {w}x{h} 이상 (약 {scale}배)")
    print()
    print("다시 뽑는 방법")
    print("  - 웹 화면: 브라우저를 200~300%로 키우고 캡처하거나,")
    print("    headless Chrome의 --window-size 를 2배로 주고 --screenshot")
    print("  - 도표: 이미지 대신 PDF·SVG로 내보내 붙이면 배율과 무관하게 선명함")
    print("  - Word 저장 시 '파일의 이미지 압축 안 함'을 켤 것")


if __name__ == "__main__":
    main()
