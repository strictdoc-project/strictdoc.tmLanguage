# Invoke is broken on Python 3.11
# https://github.com/pyinvoke/invoke/issues/833#issuecomment-1293148106
import inspect
import os
import re
import shutil
import sys
import tempfile
from enum import Enum
from pathlib import Path
from typing import Dict, Optional

if not hasattr(inspect, "getargspec"):
    inspect.getargspec = inspect.getfullargspec

import invoke
from invoke import task

# Specifying encoding because Windows crashes otherwise when running Invoke
# tasks below:
# UnicodeEncodeError: 'charmap' codec can't encode character '\ufffd'
# in position 16: character maps to <undefined>
# People say, it might also be possible to export PYTHONIOENCODING=utf8 but this
# seems to work.
# FIXME: If you are a Windows user and expert, please advise on how to do this
# properly.
sys.stdout = open(1, "w", encoding="utf-8", closefd=False, buffering=1)


def run_invoke(
    context,
    cmd,
    environment: Optional[dict] = None,
    pty: bool = False,
    warn: bool = False,
) -> invoke.runners.Result:
    def one_line_command(string):
        return re.sub("\\s+", " ", string).strip()

    return context.run(
        one_line_command(cmd),
        env=environment,
        hide=False,
        warn=warn,
        pty=pty,
        echo=True,
    )


@task()
def test(
    context,
    focus=None,
    debug=False,
    no_parallelization=False,
    fail_first=False,
):
    clean_itest_artifacts(context)

    cwd = os.getcwd()

    parse_syntax_script = f'node \\"{cwd}/parse_syntax.js\\"'

    debug_opts = "-vv --show-all" if debug else ""
    focus_or_none = f"--filter {focus}" if focus else ""
    fail_first_argument = "--max-failures 1" if fail_first else ""
    parallelize_opts = "" if not no_parallelization else "--threads 1"
    test_folder = f"{cwd}/tests/integration"

    itest_command = f"""
        lit
        --param PARSE_SYNTAX_EXEC="{parse_syntax_script}"
        -v
        {debug_opts}
        {focus_or_none}
        {fail_first_argument}
        {parallelize_opts}
        {test_folder}
    """
    run_invoke(
        context,
        itest_command,
    )

@task
def clean_itest_artifacts(context):
    # The command sometimes exits with 1 even if the files are deleted.
    # warn=True ensures that the execution continues.
    run_invoke(
        context,
        """
        git clean -dX --force --quiet tests/integration/
        """,
        warn=True,
    )
