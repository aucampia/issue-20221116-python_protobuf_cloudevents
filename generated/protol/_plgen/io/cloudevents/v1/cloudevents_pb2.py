"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#io/cloudevents/v1/cloudevents.proto\x12\x11io.cloudevents.v1\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x05\n\nCloudEvent\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x16\n\x06source\x18\x02 \x01(\tR\x06source\x12!\n\x0cspec_version\x18\x03 \x01(\tR\x0bspecVersion\x12\x12\n\x04type\x18\x04 \x01(\tR\x04type\x12M\n\nattributes\x18\x05 \x03(\x0b2-.io.cloudevents.v1.CloudEvent.AttributesEntryR\nattributes\x12!\n\x0bbinary_data\x18\x06 \x01(\x0cH\x00R\nbinaryData\x12\x1d\n\ttext_data\x18\x07 \x01(\tH\x00R\x08textData\x125\n\nproto_data\x18\x08 \x01(\x0b2\x14.google.protobuf.AnyH\x00R\tprotoData\x1au\n\x0fAttributesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12L\n\x05value\x18\x02 \x01(\x0b26.io.cloudevents.v1.CloudEvent.CloudEventAttributeValueR\x05value:\x028\x01\x1a\x9a\x02\n\x18CloudEventAttributeValue\x12\x1f\n\nce_boolean\x18\x01 \x01(\x08H\x00R\tceBoolean\x12\x1f\n\nce_integer\x18\x02 \x01(\x05H\x00R\tceInteger\x12\x1d\n\tce_string\x18\x03 \x01(\tH\x00R\x08ceString\x12\x1b\n\x08ce_bytes\x18\x04 \x01(\x0cH\x00R\x07ceBytes\x12\x17\n\x06ce_uri\x18\x05 \x01(\tH\x00R\x05ceUri\x12\x1e\n\nce_uri_ref\x18\x06 \x01(\tH\x00R\x08ceUriRef\x12?\n\x0cce_timestamp\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00R\x0bceTimestampB\x06\n\x04attrB\x06\n\x04data"H\n\x0fCloudEventBatch\x125\n\x06events\x18\x01 \x03(\x0b2\x1d.io.cloudevents.v1.CloudEventR\x06eventsB\xdc\x01\n\x15com.io.cloudevents.v1B\x10CloudeventsProtoP\x01ZKgithub.com/coopnorge/go-services-interfaces/io/cloudevents/v1;cloudeventsv1\xa2\x02\x03ICX\xaa\x02\x11Io.Cloudevents.V1\xca\x02\x11Io\\Cloudevents\\V1\xe2\x02\x1dIo\\Cloudevents\\V1\\GPBMetadata\xea\x02\x13Io::Cloudevents::V1b\x06proto3')
_CLOUDEVENT = DESCRIPTOR.message_types_by_name['CloudEvent']
_CLOUDEVENT_ATTRIBUTESENTRY = _CLOUDEVENT.nested_types_by_name['AttributesEntry']
_CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE = _CLOUDEVENT.nested_types_by_name['CloudEventAttributeValue']
_CLOUDEVENTBATCH = DESCRIPTOR.message_types_by_name['CloudEventBatch']
CloudEvent = _reflection.GeneratedProtocolMessageType('CloudEvent', (_message.Message,), {'AttributesEntry': _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), {'DESCRIPTOR': _CLOUDEVENT_ATTRIBUTESENTRY, '__module__': 'io.cloudevents.v1.cloudevents_pb2'}), 'CloudEventAttributeValue': _reflection.GeneratedProtocolMessageType('CloudEventAttributeValue', (_message.Message,), {'DESCRIPTOR': _CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE, '__module__': 'io.cloudevents.v1.cloudevents_pb2'}), 'DESCRIPTOR': _CLOUDEVENT, '__module__': 'io.cloudevents.v1.cloudevents_pb2'})
_sym_db.RegisterMessage(CloudEvent)
_sym_db.RegisterMessage(CloudEvent.AttributesEntry)
_sym_db.RegisterMessage(CloudEvent.CloudEventAttributeValue)
CloudEventBatch = _reflection.GeneratedProtocolMessageType('CloudEventBatch', (_message.Message,), {'DESCRIPTOR': _CLOUDEVENTBATCH, '__module__': 'io.cloudevents.v1.cloudevents_pb2'})
_sym_db.RegisterMessage(CloudEventBatch)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'\n\x15com.io.cloudevents.v1B\x10CloudeventsProtoP\x01ZKgithub.com/coopnorge/go-services-interfaces/io/cloudevents/v1;cloudeventsv1\xa2\x02\x03ICX\xaa\x02\x11Io.Cloudevents.V1\xca\x02\x11Io\\Cloudevents\\V1\xe2\x02\x1dIo\\Cloudevents\\V1\\GPBMetadata\xea\x02\x13Io::Cloudevents::V1'
    _CLOUDEVENT_ATTRIBUTESENTRY._options = None
    _CLOUDEVENT_ATTRIBUTESENTRY._serialized_options = b'8\x01'
    _CLOUDEVENT._serialized_start = 119
    _CLOUDEVENT._serialized_end = 838
    _CLOUDEVENT_ATTRIBUTESENTRY._serialized_start = 428
    _CLOUDEVENT_ATTRIBUTESENTRY._serialized_end = 545
    _CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE._serialized_start = 548
    _CLOUDEVENT_CLOUDEVENTATTRIBUTEVALUE._serialized_end = 830
    _CLOUDEVENTBATCH._serialized_start = 840
    _CLOUDEVENTBATCH._serialized_end = 912