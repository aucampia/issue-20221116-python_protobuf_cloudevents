"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...io.cloudevents.v1 import cloudevents_pb2 as io_dot_cloudevents_dot_v1_dot_cloudevents__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19example/v1/messages.proto\x12\nexample.v1\x1a#io/cloudevents/v1/cloudevents.proto"\\\n\tSomething\x12\x17\n\x07field_a\x18\x01 \x01(\tR\x06fieldA\x126\n\x07field_b\x18\x02 \x01(\x0b2\x1d.io.cloudevents.v1.CloudEventR\x06fieldBB\xaa\x01\n\x0ecom.example.v1B\rMessagesProtoP\x01Z@github.com/coopnorge/go-services-interfaces/example/v1;examplev1\xa2\x02\x03EXX\xaa\x02\nExample.V1\xca\x02\nExample\\V1\xe2\x02\x16Example\\V1\\GPBMetadata\xea\x02\x0bExample::V1b\x06proto3')
_SOMETHING = DESCRIPTOR.message_types_by_name['Something']
Something = _reflection.GeneratedProtocolMessageType('Something', (_message.Message,), {'DESCRIPTOR': _SOMETHING, '__module__': 'example.v1.messages_pb2'})
_sym_db.RegisterMessage(Something)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0ecom.example.v1B\rMessagesProtoP\x01Z@github.com/coopnorge/go-services-interfaces/example/v1;examplev1\xa2\x02\x03EXX\xaa\x02\nExample.V1\xca\x02\nExample\\V1\xe2\x02\x16Example\\V1\\GPBMetadata\xea\x02\x0bExample::V1'
    _SOMETHING._serialized_start = 78
    _SOMETHING._serialized_end = 170