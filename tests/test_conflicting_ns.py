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


def test_something() -> None:
    import example.aucampia.nsconflict

    assert example.aucampia.nsconflict.whereami() == "example.aucampia.nsconflict"


def test_conflict_a() -> None:
    """
    this works because of the content of src/mailbox/__init__.py
    """
    import mailbox.sub

    assert mailbox.sub.whereami() == "mailbox.sub"


def test_mailbox() -> None:
    """
    this does not work because of the content of src/mailbox/__init__.py
    """
    import mailbox

    assert callable(mailbox.Mailbox)  # type: ignore


def test_conflict_b() -> None:
    """
    this does not work because it generates modules inside io namespace

    ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package
    """
    import example.v1.messages_pb2

    example.v1.messages_pb2.Something()


def test_pb_okay() -> None:
    """
    this works fine
    """
    import example.v2.messages_pb2

    example.v2.messages_pb2.Something()
