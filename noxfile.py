"""
This file is used to configure Nox for running lint, format, and test tasks in CI/CD pipelines.
In this project, it runs with uv backend.
"""

import nox


# lint and format sessions with ruff
@nox.session(venv_backend="uv", python=["3.12"], tags=["lint"])
def lint(session):
    # linting for frontend
    session.cd('packages/frontend')
    session.install("ruff")
    session.run("uv", "run", "ruff", "check")
    session.run("uv", "run", "ruff", "format")

# linting for backend
    session.cd('../backend')
    session.run("uv", "run", "ruff", "check")
    session.run("uv", "run", "ruff", "format")

# static type check with mypy
# Uneabled due to the issue with mypy and gradio.


# @nox.session(venv_backend="uv", python=["3.12"], tags=["lint"])
# def mypy(session):
#     session.install("pyproject.toml")
#     session.install("mypy")

#     directories = [
#         # "data",
#         # "ai",
#         # "app",
#         "tests",
#     ]
#     for directory in directories:
#         session.run("uv", "run", "mypy", directory)


# test sessions with pytest
# @nox.session(venv_backend="uv", python=["3.12"], tags=["test"])
# def test(session):
#     session.run("uv", "sync", "--dev")

#     if session.posargs:
#         test_files = session.posargs
#     else:
#         test_files = ["tests"]

#     session.run(
#         "uv",
#         "run",
#         "pytest",
#         # "--junitxml=reports/test-results/pytest-results.xml",
#         # "--cov=src",
#         *test_files,
#     )