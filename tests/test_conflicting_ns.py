# import argparse
import logging
import os
import sys

from pathlib import Path

MODULE_PATH = Path(__file__)

if os.environ.get("HACK_SYS_PATH", "") != "":
    logging.info("sys.path = %s", sys.path)
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'src'}")
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'generated' / 'proto'}")
    logging.info("sys.path = %s", sys.path)

## First load
import lib2to3.sub
import lib2to3 as _


def test_something() -> None:
    logging.info("entry: ...")
    import example.aucampia.nsconflict

    assert example.aucampia.nsconflict.whoami() == "example.aucampia.nsconflict"


def test_conflict_a() -> None:
    logging.info("entry: ...")

    import lib2to3.sub

    assert lib2to3.sub.whoami() == "lib2to3.sub"


def test_conflict_c() -> None:
    import example.v1.messages_pb2

    example.v1.messages_pb2.Something()
