# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example/v1/messages.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from io.cloudevents.v1 import cloudevents_pb2 as io_dot_cloudevents_dot_v1_dot_cloudevents__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x65xample/v1/messages.proto\x12\nexample.v1\x1a#io/cloudevents/v1/cloudevents.proto\"\\\n\tSomething\x12\x17\n\x07\x66ield_a\x18\x01 \x01(\tR\x06\x66ieldA\x12\x36\n\x07\x66ield_b\x18\x02 \x01(\x0b\x32\x1d.io.cloudevents.v1.CloudEventR\x06\x66ieldBB\xaa\x01\n\x0e\x63om.example.v1B\rMessagesProtoP\x01Z@github.com/coopnorge/go-services-interfaces/example/v1;examplev1\xa2\x02\x03\x45XX\xaa\x02\nExample.V1\xca\x02\nExample\\V1\xe2\x02\x16\x45xample\\V1\\GPBMetadata\xea\x02\x0b\x45xample::V1b\x06proto3')



_SOMETHING = DESCRIPTOR.message_types_by_name['Something']
Something = _reflection.GeneratedProtocolMessageType('Something', (_message.Message,), {
  'DESCRIPTOR' : _SOMETHING,
  '__module__' : 'example.v1.messages_pb2'
  # @@protoc_insertion_point(class_scope:example.v1.Something)
  })
_sym_db.RegisterMessage(Something)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.example.v1B\rMessagesProtoP\001Z@github.com/coopnorge/go-services-interfaces/example/v1;examplev1\242\002\003EXX\252\002\nExample.V1\312\002\nExample\\V1\342\002\026Example\\V1\\GPBMetadata\352\002\013Example::V1'
  _SOMETHING._serialized_start=78
  _SOMETHING._serialized_end=170
# @@protoc_insertion_point(module_scope)
