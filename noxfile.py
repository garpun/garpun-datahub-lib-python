import nox

PYTHON_VERSIONS = ["3.6", "3.7", "3.8"]

FLAKE_PATHS = ["garpundatahub", "tests/test_datahub.py", "setup.py"]

LINT_DEPENDENCIES = [
    "flake8",
    "flake8-mutable",
    "flake8-bugbear",
    "flake8-print",
    "flake8-per-file-ignores",
    "git+https://github.com/gforcada/flake8-builtins.git@1.5.0",
    "git+https://github.com/PyCQA/flake8-commas.git@2.0.0",
    "git+https://github.com/zheller/flake8-quotes.git@3.0.0"
]


@nox.session(python="3.6")
def lint(session):
    session.install(*LINT_DEPENDENCIES)
    session.run("flake8", *FLAKE_PATHS)
    session.run("python", "setup.py", "check", "--metadata", "--strict")


@nox.session(python="3.6")
def cover(session):
    session.install("pytest", "pytest-cov")
    session.install(".")
    session.run("pytest", "--cov=garpundatahub", "--cov=tests", "--cov-report=", "tests")
    session.run("coverage", "report", "--show-missing", "--fail-under=1")
    session.run("coverage", "erase")


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    session.install("pytest")
    session.install(".")
    session.run("pytest", "tests/")
