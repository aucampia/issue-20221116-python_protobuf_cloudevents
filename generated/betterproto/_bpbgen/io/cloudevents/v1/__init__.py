# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: io/cloudevents/v1/cloudevents.proto
# plugin: python-betterproto
from dataclasses import dataclass
from datetime import datetime
from typing import (
    Dict,
    List,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf


@dataclass(eq=False, repr=False)
class CloudEvent(betterproto.Message):
    id: str = betterproto.string_field(1)
    """Required Attributes"""

    source: str = betterproto.string_field(2)
    spec_version: str = betterproto.string_field(3)
    type: str = betterproto.string_field(4)
    attributes: Dict[str, "CloudEventCloudEventAttributeValue"] = betterproto.map_field(
        5, betterproto.TYPE_STRING, betterproto.TYPE_MESSAGE
    )
    """Optional & Extension Attributes"""

    binary_data: bytes = betterproto.bytes_field(6, group="data")
    text_data: str = betterproto.string_field(7, group="data")
    proto_data: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        8, group="data"
    )


@dataclass(eq=False, repr=False)
class CloudEventCloudEventAttributeValue(betterproto.Message):
    ce_boolean: bool = betterproto.bool_field(1, group="attr")
    ce_integer: int = betterproto.int32_field(2, group="attr")
    ce_string: str = betterproto.string_field(3, group="attr")
    ce_bytes: bytes = betterproto.bytes_field(4, group="attr")
    ce_uri: str = betterproto.string_field(5, group="attr")
    ce_uri_ref: str = betterproto.string_field(6, group="attr")
    ce_timestamp: datetime = betterproto.message_field(7, group="attr")


@dataclass(eq=False, repr=False)
class CloudEventBatch(betterproto.Message):
    events: List["CloudEvent"] = betterproto.message_field(1)
