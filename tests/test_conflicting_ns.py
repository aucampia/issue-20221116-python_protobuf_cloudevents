import logging
import os
import sys
from pathlib import Path

MODULE_PATH = Path(__file__)


if os.environ.get("HACK_SYS_PATH", "") != "":
    logging.info("sys.path = %s", sys.path)
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'src'}")
    logging.info("sys.path = %s", sys.path)


def test_something() -> None:
    logging.info("entry: ...")
    import example.aucampia.nsconflict

    assert example.aucampia.nsconflict.whoami() == "example.aucampia.nsconflict"


def test_conflict_a() -> None:
    logging.info("entry: ...")
    import argparse.sub

    assert argparse.sub.whoami() == "argparse.sub"
