# ruff: noqa: F821

import os
import sys
from typing import Any

import lit.formats

config: Any
lit_config: Any

config.name = "StrictDoc integration tests"
config.test_format = lit.formats.ShTest("0")
config.suffixes = [".itest"]

current_dir = os.getcwd()

parse_syntax_exec = lit_config.params["PARSE_SYNTAX_EXEC"]

# NOTE: All substitutions work for the RUN: statements but they don't for CHECK:.
#       That's how LLVM LIT works.
config.substitutions.append(("%THIS_TEST_FOLDER", '$(basename "%S")'))

config.substitutions.append(("%parse_syntax", parse_syntax_exec))
