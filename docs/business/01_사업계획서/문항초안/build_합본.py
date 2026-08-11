#!/usr/bin/env python3
"""Q1~Q4 문항초안을 하나의 사업계획서 합본으로 묶는다.

사용법:  python3 docs/business/01_사업계획서/문항초안/build_합본.py
출력:    docs/business/01_사업계획서/참고2_PSSD_사업계획서_초안.md

문항 파일을 고친 뒤 다시 실행하면 합본이 갱신된다.
합본은 직접 고치지 말 것(다음 실행 때 덮어씀).
"""

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "참고2_PSSD_사업계획서_초안.md"
FILES = [
    "Q1_문제인식.md",
    "Q2_실현가능성.md",
    "Q3_성장전략.md",
    "Q4_향후발전방안.md",
]

HEAD = """# GLOU 사업계획서 초안 — 참고 2 : PSSD 양식

> 이 파일은 [문항초안/](문항초안/)의 Q1~Q4를 하나로 묶은 **자동 생성 합본**입니다.
> 내용을 고칠 때는 문항별 파일을 고치고 `python3 docs/business/01_사업계획서/문항초안/build_합본.py`를 다시 실행하세요.
> 이 파일을 직접 고치면 다음 실행 때 덮어써집니다.
>
> 문체: 사실·수치는 개조식(명사형 종결), 논리 설명은 서술형 존댓말. 표는 수치·비교에만 사용.
> 표기: 팀원은 역할로만 적음. **실명은 제출본에서 채울 것.**
> 미확정 항목은 `[팀 확정]` / `[산정 예정]`으로 표시함.

## 목차

- Q1. 문제 인식 (Problem) — 아이디어의 개발 동기·목적 및 목표 시장
- Q2. 실현가능성 (Solution) — 아이디어의 개발 방안, 준비 정도, 차별화 방안
- Q3. 성장전략 (Scale-up) — 사업화 계획, 추진일정, 자금 소요 및 조달 계획
- Q4. 향후 발전방안 (Development) — 멘토링 후 아이디어 발전 방향 및 주요 개선점
- 용어 설명 (각주)
- 참고 출처
"""


def demote(md: str) -> str:
    """머리말 수준을 한 단계 낮춘다."""
    for level in range(5, 0, -1):
        md = re.sub(r"^%s " % ("#" * level), "#" * (level + 1) + " ", md, flags=re.M)
    return md


def split_sections(md: str):
    """본문 / 각주 / 참고 출처로 나눈다."""
    i_note = md.find("\n## 각주")
    i_ref = md.find("\n## 참고 출처")
    cuts = [i for i in (i_note, i_ref) if i != -1]
    body = md[: min(cuts)] if cuts else md

    notes = ""
    if i_note != -1:
        end = i_ref if i_ref > i_note else len(md)
        notes = md[i_note:end].split("\n", 1)[1] if "\n" in md[i_note:end] else ""
        notes = re.sub(r"^## 각주[^\n]*\n", "", notes)

    refs = ""
    if i_ref != -1:
        refs = re.sub(r"^\n## 참고 출처[^\n]*\n", "", md[i_ref:])

    return body.rstrip(), notes.strip(), refs.strip()


def strip_meta(body: str) -> str:
    """제목 바로 뒤의 안내용 인용문과 구분선을 걷어낸다."""
    lines = body.split("\n")
    title, rest = lines[0], lines[1:]
    while rest and (not rest[0].strip() or rest[0].startswith(">") or rest[0].strip() == "---"):
        rest.pop(0)
    return "\n".join([title, ""] + rest)


def fix_relpath(md: str) -> str:
    """합본은 문항초안/의 한 단계 위에 있으므로 상대경로에서 ../ 하나를 뺀다."""
    return re.sub(r"\]\(\.\./", "](", md)


def main() -> None:
    bodies, all_notes, all_refs = [], [], []
    table_map = {}  # (Qn, 기존번호) -> 합본 번호
    counter = 0

    for name in FILES:
        path = HERE / name
        if not path.exists():
            print(f"건너뜀(파일 없음): {name}")
            continue
        qkey = name.split("_")[0]  # Q1, Q2 ...
        body, notes, refs = split_sections(path.read_text(encoding="utf-8"))
        body = demote(strip_meta(body)).strip()

        # 표 번호를 합본 기준으로 이어 붙인다
        def renum(m, _q=qkey):
            nonlocal counter
            counter += 1
            table_map[(_q, int(m.group(1)))] = counter
            return f"**[표 {counter}]"

        body = re.sub(r"\*\*\[표 (\d+)\]", renum, body)
        bodies.append(fix_relpath(body))

        if notes:
            all_notes.append(fix_relpath(notes))
        for line in refs.split("\n"):
            line = fix_relpath(line.strip())
            if line.startswith("- ") and line not in all_refs:
                all_refs.append(line)

    # "Q2 [표 1]" 같은 문항 간 참조를 합본 번호로 바꾼다
    def fix_ref(m):
        new = table_map.get((m.group(1), int(m.group(2))))
        return f"[표 {new}]" if new else m.group(0)

    bodies = [re.sub(r"(Q\d) \[표 (\d+)\]", fix_ref, b) for b in bodies]

    parts = [HEAD, "\n---\n\n", "\n\n---\n\n".join(bodies)]
    if all_notes:
        parts.append("\n\n---\n\n## 용어 설명 (각주)\n\n" + "\n\n".join(all_notes))
    if all_refs:
        parts.append("\n\n---\n\n## 참고 출처\n\n" + "\n".join(all_refs) + "\n")

    OUT.write_text("".join(parts), encoding="utf-8")

    text = OUT.read_text(encoding="utf-8")
    n_table = len(re.findall(r"\*\*\[표 \d+\]", text))
    n_char = len(re.sub(r"\s+", "", re.sub(r"[|>#*`\[\]()]", "", text)))
    print(f"생성: {OUT}")
    print(f"문항 {len(bodies)}개 · 표 {n_table}개 · 약 {n_char:,}자(공백 제외)")


if __name__ == "__main__":
    main()
