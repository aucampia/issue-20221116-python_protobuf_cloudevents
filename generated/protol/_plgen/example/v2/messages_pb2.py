"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19example/v2/messages.proto\x12\nexample.v2"\\\n\tSomething\x12\x17\n\x07field_a\x18\x01 \x01(\tR\x06fieldA\x12\x17\n\x07field_b\x18\x02 \x01(\x03R\x06fieldB\x12\x1d\n\nSOME_FIELD\x18\x03 \x01(\tR\tSOMEFIELDB\xaa\x01\n\x0ecom.example.v2B\rMessagesProtoP\x01Z@github.com/coopnorge/go-services-interfaces/example/v2;examplev2\xa2\x02\x03EXX\xaa\x02\nExample.V2\xca\x02\nExample\\V2\xe2\x02\x16Example\\V2\\GPBMetadata\xea\x02\x0bExample::V2b\x06proto3')
_SOMETHING = DESCRIPTOR.message_types_by_name['Something']
Something = _reflection.GeneratedProtocolMessageType('Something', (_message.Message,), {'DESCRIPTOR': _SOMETHING, '__module__': 'example.v2.messages_pb2'})
_sym_db.RegisterMessage(Something)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x0ecom.example.v2B\rMessagesProtoP\x01Z@github.com/coopnorge/go-services-interfaces/example/v2;examplev2\xa2\x02\x03EXX\xaa\x02\nExample.V2\xca\x02\nExample\\V2\xe2\x02\x16Example\\V2\\GPBMetadata\xea\x02\x0bExample::V2'
    _SOMETHING._serialized_start = 41
    _SOMETHING._serialized_end = 133