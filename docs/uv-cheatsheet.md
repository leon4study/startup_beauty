# uv 치트시트

> `uv` 는 Rust 로 작성된 차세대 Python 패키지 매니저입니다. pip + venv +
> pip-tools + virtualenv 의 기능을 한 도구로 통합하고, 보통 10–100배 빠릅니다.

## 핵심: `uv add` vs `pip install`

겹치는 부분이 있지만 **핵심이 다릅니다**. `pip install` 은 *깔기만* 하고,
`uv add` 는 *프로젝트의 의존성으로 영구 등록 + 깔기 + 락 갱신* 을 한 번에 합니다.

```bash
pip install pandas
# → 현재 venv 에 pandas 만 설치하고 끝.
# → pyproject.toml 은 그대로. 다른 사람이 clone 해도 pandas 는 안 깔림.
# → 손으로 pyproject.toml 에도 추가해야 함.

uv add pandas
# → 1) pyproject.toml 의 [project.dependencies] 에 "pandas>=X.Y" 자동 추가
# → 2) .venv 에 설치
# → 3) uv.lock 에 정확한 버전 + 해시 + 의존 트리 기록
# → 다른 사람이 `uv sync` 하면 동일한 버전이 그대로 재현됨.
```

즉 **`pip install` + `pyproject.toml` 수동 편집** 의 두 단계를 한 번에 묶은 것이 `uv add` 입니다.

## 자주 쓰는 명령

### 환경 구성
```bash
uv sync                       # pyproject + uv.lock 기준으로 .venv 재구성
uv sync --all-groups          # dev / test / lint / notebook 모두 설치
uv sync --no-dev              # 런타임 의존성만 (프로덕션 배포 시)
uv lock                       # 락파일 재생성 (최신 호환 버전으로 재해석)
uv lock --upgrade             # 모든 의존성을 최신 호환 버전으로 업그레이드
uv lock --upgrade-package pandas   # 특정 패키지만 업그레이드
```

### 의존성 추가 / 제거
```bash
uv add pandas                          # 런타임 의존성 추가
uv add 'pandas>=2.2,<3'                # 버전 범위 지정
uv add --group test pytest-mock        # test 그룹에만 추가
uv add --group lint mypy               # lint 그룹에만 추가
uv add --dev ipdb                      # dev 그룹 (test+lint+notebook 의 합집합)
uv remove pandas                       # 제거 (pyproject + lock 자동 정리)
```

### 실행
```bash
uv run python script.py                # venv 활성화 없이 한 줄 실행
uv run pytest                          # 어떤 명령이든 `uv run <cmd>` 로 실행 가능
uv run myproject --help                # console_scripts 진입점도 동일하게
uv run --with httpx python -c "..."    # 일회성으로 추가 패키지 끼워 실행
```

또는 평소처럼 venv 를 활성화해도 됩니다:
```bash
source .venv/bin/activate              # macOS / Linux
# .venv\Scripts\activate             # Windows
pytest                                 # 이제 `uv run` 없이 직접
deactivate                             # 끝낼 때
```

### Python 자체 관리
```bash
uv python install 3.12                 # Python 3.12 설치 (uv 가 직접)
uv python list                         # 설치된 / 사용 가능한 버전 목록
uv python pin 3.12                     # 이 프로젝트의 .python-version 갱신
```

### 캐시 / 정리
```bash
uv cache clean                         # 다운로드 캐시 비우기
uv cache dir                           # 캐시 경로 확인
```

## pip 명령과의 1:1 대응표

| 하려는 일 | pip + venv | uv |
|---|---|---|
| 가상환경 만들기 | `python -m venv .venv` | `uv venv` (보통 `uv sync` 가 자동) |
| 의존성 설치 | `pip install -e . && pip install --group dev` | `uv sync` |
| 패키지 추가 | `pip install X` + pyproject 수동 편집 | `uv add X` |
| 패키지 제거 | `pip uninstall X` + pyproject 수동 편집 | `uv remove X` |
| 명령 실행 | `source .venv/bin/activate && X` | `uv run X` |
| 락파일 생성 | `pip-compile` (별도 도구 필요) | `uv lock` (내장) |
| 락파일 동기화 | `pip-sync` (별도 도구 필요) | `uv sync` |
| Python 설치 | `pyenv install 3.12` (별도 도구) | `uv python install 3.12` |

## 락파일(uv.lock) 이 뭔가요?

`pyproject.toml` 에는 **버전 범위** 만 적습니다 (예: `pandas>=2.2`).
실제로 어느 시점에 누가 깔았느냐에 따라 `2.2.0` 일 수도, `2.2.3` 일 수도 있어
"내 컴퓨터에선 되는데" 문제가 생깁니다.

`uv.lock` 은 이번 해석 결과의 **정확한 버전 + 해시** 를 모두 적어 두는
파일입니다. 다른 사람이 `uv sync` 하면 이 파일을 따라 **완전히 동일한
버전 조합** 이 설치되어 재현성이 보장됩니다.

**언제 갱신되나**:
- `uv add` / `uv remove` → 자동
- `uv sync` 도중 pyproject 가 lock 과 어긋나면 → 자동
- 명시적 `uv lock` → "지금 가능한 최신 호환 버전으로 다시 풀어 줘"

평소에는 직접 `uv lock` 을 칠 일이 거의 없습니다. **`uv.lock` 은 git 에
반드시 커밋** 하세요 — 이게 빠지면 락파일의 의미가 없어집니다.

## 의존성 그룹 ([dependency-groups], PEP 735)

`pyproject.toml` 의 `[dependency-groups]` 에 정의된 그룹들은 **배포되는
wheel 의 메타데이터에 포함되지 않습니다**. 즉 PyPI 에 올려도 ruff / pytest
같은 개발 도구가 따라 올라가지 않습니다.

이 프로젝트의 기본 그룹:
- `test` — pytest, pytest-cov, pytest-randomly
- `lint` — ruff, black, mypy
- `notebook` — jupyter, ipykernel, nbqa, nbstripout
- `dev` — 위 셋 + pre-commit (전부)

```bash
uv sync                       # default-groups = ["dev"] 이므로 dev 그룹 포함
uv sync --no-dev              # 런타임만 (프로덕션 컨테이너 등)
uv sync --group test          # test 만 추가로
uv sync --all-groups          # 모든 그룹
```

## 흔한 트러블슈팅

| 증상 | 원인 | 해결 |
|---|---|---|
| `uv: command not found` | uv 미설치 | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| `ModuleNotFoundError: <name>` | editable 설치가 안 됨 | `uv sync` 한 번 더 |
| CI 에서 동작이 로컬과 다름 | uv.lock 이 커밋 안 됨 | `git add uv.lock && git commit` |
| 의존성을 추가했는데 다른 사람에게 안 깔림 | `pip install` 만 하고 pyproject 수정 안 함 | `uv add` 로 다시 추가 |
| 락파일이 자꾸 변함 | 버전 범위가 너무 느슨 | 범위를 더 좁히거나 lock 만 커밋 |

## 참고

- 공식 문서: https://docs.astral.sh/uv/
- PEP 735 (dependency-groups): https://peps.python.org/pep-0735/
