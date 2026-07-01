from functools import cache
from pathlib import Path
import shutil
import tarfile

LIB = Path(__file__).parent


@cache
def bin() -> Path:
    archive = next(LIB.glob("postgresql-*.tar.gz"))
    stem = archive.name[: -len(".tar.gz")]

    # Clean up any previous versions
    for existing in LIB.glob("postgresql-*"):
        if existing.is_dir() and existing.name != stem:
            shutil.rmtree(existing)

    if not (LIB / stem).exists():
        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(path=LIB, filter="data")

    out = LIB / stem / "bin"
    assert out.exists()
    return out
