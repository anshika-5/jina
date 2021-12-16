# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='test.proto',
    package='test',
    syntax='proto3',
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\ntest.proto\x12\x04test\"!\n\tunitProto\x12\t\n\x01\x61\x18\x01 \x01(\t\x12\t\n\x01\x62\x18\x02 \x01(\r\"0\n\x0epopulatedProto\x12\x1e\n\x05units\x18\x01 \x03(\x0b\x32\x0f.test.unitProto\"\x1a\n\tskipProto\x12\r\n\x05units\x18\x01 \x01(\x0c\x62\x06proto3',
)


_UNITPROTO = _descriptor.Descriptor(
    name='unitProto',
    full_name='test.unitProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='a',
            full_name='test.unitProto.a',
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode('utf-8'),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name='b',
            full_name='test.unitProto.b',
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=20,
    serialized_end=53,
)


_POPULATEDPROTO = _descriptor.Descriptor(
    name='populatedProto',
    full_name='test.populatedProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='units',
            full_name='test.populatedProto.units',
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=55,
    serialized_end=103,
)


_SKIPPROTO = _descriptor.Descriptor(
    name='skipProto',
    full_name='test.skipProto',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name='units',
            full_name='test.skipProto.units',
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=131,
)

_POPULATEDPROTO.fields_by_name['units'].message_type = _UNITPROTO
DESCRIPTOR.message_types_by_name['unitProto'] = _UNITPROTO
DESCRIPTOR.message_types_by_name['populatedProto'] = _POPULATEDPROTO
DESCRIPTOR.message_types_by_name['skipProto'] = _SKIPPROTO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

unitProto = _reflection.GeneratedProtocolMessageType(
    'unitProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _UNITPROTO,
        '__module__': 'test_pb2'
        # @@protoc_insertion_point(class_scope:test.unitProto)
    },
)
_sym_db.RegisterMessage(unitProto)

populatedProto = _reflection.GeneratedProtocolMessageType(
    'populatedProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _POPULATEDPROTO,
        '__module__': 'test_pb2'
        # @@protoc_insertion_point(class_scope:test.populatedProto)
    },
)
_sym_db.RegisterMessage(populatedProto)

skipProto = _reflection.GeneratedProtocolMessageType(
    'skipProto',
    (_message.Message,),
    {
        'DESCRIPTOR': _SKIPPROTO,
        '__module__': 'test_pb2'
        # @@protoc_insertion_point(class_scope:test.skipProto)
    },
)
_sym_db.RegisterMessage(skipProto)


# @@protoc_insertion_point(module_scope)
