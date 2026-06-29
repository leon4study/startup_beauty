# Cross-platform notes (Mac / Windows / Linux)

## Why this matters
Mac and Windows differ in:
- Line endings (LF vs CRLF) — handled by `.gitattributes`
- Path separators — always use `pathlib.Path`, never raw `/` or `\`
- GPU backends — Mac=MPS, Windows/Linux=CUDA
- Python install paths

## Required one-time team setup

```bash
# Mac/Linux
git config --global core.autocrlf input

# Windows (in Git Bash or PowerShell)
git config --global core.autocrlf true
```

## Python 3.11

Pinned via `.python-version`. With **uv**:
```bash
uv sync                  # installs the right Python + all deps
```

Without uv:
- macOS: `brew install python@3.11` or `pyenv install 3.11`
- Windows: from python.org installer, or `pyenv-win`
- Linux: `pyenv install 3.11`

## Device-agnostic PyTorch (if used)

```python
import torch

def get_device() -> torch.device:
    if torch.cuda.is_available():
        return torch.device("cuda")
    if torch.backends.mps.is_available():  # Apple Silicon
        return torch.device("mps")
    return torch.device("cpu")
```

## PyTorch installation — two patterns

PyTorch is **not** in default deps. Pick the pattern that matches your team.

### Pattern 1 — uncomment in `pyproject.toml` (single-backend team)

```toml
dependencies = [
    "torch>=2.2",   # Mac MPS / Linux CPU
]
```

Then for CUDA users, install via the right index:
```bash
# CUDA 12.1
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121

# CPU-only fallback
uv pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

### Pattern 2 — multi-backend extras (Mac + CUDA mixed team)

Add to `pyproject.toml`:
```toml
[project.optional-dependencies]
cpu = ["torch>=2.2"]
gpu = ["torch>=2.2"]

[tool.uv]
conflicts = [[{ extra = "cpu" }, { extra = "gpu" }]]

[tool.uv.sources]
torch = [
    { index = "pytorch-cpu",   extra = "cpu" },
    { index = "pytorch-cu121", extra = "gpu" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[[tool.uv.index]]
name = "pytorch-cu121"
url = "https://download.pytorch.org/whl/cu121"
explicit = true
```

Each contributor picks the right wheel:
```bash
uv sync --extra gpu     # CUDA build (Linux/Win with NVIDIA)
uv sync --extra cpu     # CPU/Mac build
```

## Heavy training

Mac MPS is slower than CUDA. For real training runs:
- Use a Windows/Linux teammate's NVIDIA GPU, or
- Use Google Colab / Lambda Labs / RunPod

Mac is fine for development, debugging, and inference.

## Common gotchas

| Symptom | Cause | Fix |
|---|---|---|
| Diff shows every line changed | CRLF vs LF | Ensure `.gitattributes` committed; re-run `git add --renormalize .` |
| `\r` in shell scripts | Saved as CRLF | Convert: `dos2unix script.sh` |
| `ModuleNotFoundError` after install | Editable install missing | `uv sync` (or `pip install -e .`) |
| YOLO/CUDA errors on Mac | Wrong torch wheel | Install Mac wheel (no `--index-url`) |
| `uv: command not found` | uv not installed | `curl -LsSf https://astral.sh/uv/install.sh | sh` |
