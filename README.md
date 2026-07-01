# Postgresql Binaries

Uses releases from [theseus-rs/postgresql-binaries](https://github.com/theseus-rs/postgresql-binaries) and publishes them to pypy, so that you can do:

```shell
pip install postgresql-binaries==18.4.0
```

The package is around 11MB.

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

On the first call to `bin()`, the archive baked into the wheel is unpacked in place.
