# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: example/v1/messages.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from ...io.cloudevents import v1 as __io_cloudevents_v1__


@dataclass(eq=False, repr=False)
class Something(betterproto.Message):
    field_a: str = betterproto.string_field(1)
    field_b: "__io_cloudevents_v1__.CloudEvent" = betterproto.message_field(2)
