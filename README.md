# Postgresql Binaries

Uses releases from [theseus-rs/postgresql-binaries](https://github.com/theseus-rs/postgresql-binaries) and publishes them to pypy, so that you can do:

```shell
pip install postgresql-binaries==18.3.0
```

Then to use, eg:

```python
import postgresql_binaries
import subprocess

cmd = [
    str(postgresql_binaries.bin() / "initdb"),
    *("-D", directory),
    *("-U", "postgres"),
    *("--auth-host", "trust"),
]
subprocess.check_call(cmd)
```

Packages are around 10MB. On the first call to `bin()`, the archive baked into the wheel is unpacked in place.

<hr>

This library is intentionally really dumb, and intended to be built upon. There are [mixed opinions](https://discuss.python.org/t/use-of-pypi-as-a-generic-storage-platform-for-binaries/106044/58?page=3) on whether (ab)using PyPI to host binary files is a good idea. There are [similar](https://github.com/Ladybug-Memory/pgembed) packages around, but they don't handle versioning well and include too much other junk.
