"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys
if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions
DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class Something(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FIELD_A_FIELD_NUMBER: builtins.int
    FIELD_B_FIELD_NUMBER: builtins.int
    SOME_FIELD_FIELD_NUMBER: builtins.int
    field_a: builtins.str
    field_b: builtins.int
    SOME_FIELD: builtins.str
    '  string someField = 4;\n      string some_field = 5;\n    '

    def __init__(self, *, field_a: builtins.str=..., field_b: builtins.int=..., SOME_FIELD: builtins.str=...) -> None:
        ...

    def ClearField(self, field_name: typing_extensions.Literal['SOME_FIELD', b'SOME_FIELD', 'field_a', b'field_a', 'field_b', b'field_b']) -> None:
        ...
global___Something = Something