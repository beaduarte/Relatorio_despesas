import sys
from cx_Freeze import setup, Executable

target = Executable(
    script="PY/main.py",
    base="Win32GUI",
    icon="SCR/maloch.ico",
    )

buildOptions = dict(
    packages = ["os"],
    includes = [],
    include_files = ["SCR/maloch.ico"],
    excludes = []
)

setup(
    name="despesas",
    version="1.0",
    description="",
    author="beatriz",
    options = dict(build_exe = buildOptions),
    executables=[target]
    )