# import argparse
import logging
import os
import sys
from asyncio.log import logger
from pathlib import Path
from typing import List

import betterproto

MODULE_PATH = Path(__file__)


if os.environ.get("HACK_SYS_PATH", "") != "":
    # Doing this to have precise control over the module resolution path and
    # avoid any extraneous logic
    logging.info("sys.path = %s", sys.path)
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'src'}")
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'generated' / 'proto'}")
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'generated' / 'betterproto'}")
    sys.path.insert(0, f"{MODULE_PATH.parent.parent / 'generated' / 'protol'}")
    logging.info("sys.path = %s", sys.path)


def test_sane() -> None:
    import example.aucampia.nsconflict

    assert example.aucampia.nsconflict.whereami() == "example.aucampia.nsconflict"


def test_io_conflict() -> None:
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


def identity_case(value: str, strict: bool = True) -> str:
    return value


def test_bpb_okay() -> None:
    import _bpbgen.example.v1
    import _bpbgen.example.v2
    import _bpbgen.io.cloudevents.v1

    msgs: List[betterproto.Message] = [
        _bpbgen.example.v1.Something(),
        _bpbgen.example.v2.Something(),
        _bpbgen.io.cloudevents.v1.CloudEvent(),
    ]

    for msg in msgs:
        json = msg.to_dict(betterproto.Casing.CAMEL, include_default_values=True)
        logging.info("json = %s", json)

    for msg in msgs:
        json = msg.to_dict(betterproto.Casing.SNAKE, include_default_values=True)
        logging.info("json = %s", json)

    for msg in msgs:
        json = msg.to_dict(identity_case, include_default_values=True)  # type: ignore[arg-type]
        logging.info("json = %s", json)


def test_pl_okay() -> None:
    import _plgen.example.v1.messages_pb2
    import _plgen.example.v2.messages_pb2
    import _plgen.io.cloudevents.v1.cloudevents_pb2
    from google.protobuf.json_format import MessageToDict
    from google.protobuf.message import Message

    msgs: List[Message] = [
        _plgen.example.v1.messages_pb2.Something(),
        _plgen.example.v2.messages_pb2.Something(),
        _plgen.io.cloudevents.v1.cloudevents_pb2.CloudEvent(),
    ]

    for msg in msgs:
        msg_dict = MessageToDict(
            msg, including_default_value_fields=True, preserving_proto_field_name=True
        )
        logging.info("msg_dict = %s", msg_dict)

    for msg in msgs:
        msg_dict = MessageToDict(
            msg, including_default_value_fields=True, preserving_proto_field_name=False
        )
        logging.info("msg_dict = %s", msg_dict)
