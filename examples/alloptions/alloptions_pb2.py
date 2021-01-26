# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alloptions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from nrpc import nrpc_pb2 as nrpc_dot_nrpc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='alloptions.proto',
  package='main',
  syntax='proto3',
  serialized_options=b'\202\265\030\004root\212\265\030\010instance\220\265\030\001\230\265\030\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x61lloptions.proto\x12\x04main\x1a\x0fnrpc/nrpc.proto\"\x19\n\tStringArg\x12\x0c\n\x04\x61rg1\x18\x01 \x01(\t\"\"\n\x11SimpleStringReply\x12\r\n\x05reply\x18\x01 \x01(\t2\xe7\x02\n\x10SvcCustomSubject\x12N\n\rMtSimpleReply\x12\x0f.main.StringArg\x1a\x17.main.SimpleStringReply\"\x13\x82\xb2\x19\x0fmt_simple_reply\x12,\n\x0bMtVoidReply\x12\x0f.main.StringArg\x1a\n.nrpc.Void\"\x00\x12\x39\n\x0bMtNoRequest\x12\x0f.nrpc.NoRequest\x1a\x17.main.SimpleStringReply\"\x00\x12\x41\n\x0fMtStreamedReply\x12\x0f.main.StringArg\x1a\x17.main.SimpleStringReply\"\x04\x90\xb2\x19\x01\x12\x43\n\x16MtVoidReqStreamedReply\x12\n.nrpc.Void\x1a\x17.main.SimpleStringReply\"\x04\x90\xb2\x19\x01\x1a\x12\xc2\xf3\x18\x0e\x63ustom_subject2\xdf\x01\n\x10SvcSubjectParams\x12J\n\x13MtWithSubjectParams\x12\n.nrpc.Void\x1a\x17.main.SimpleStringReply\"\x0e\x8a\xb2\x19\x03mp1\x8a\xb2\x19\x03mp2\x12(\n\tMtNoReply\x12\n.nrpc.Void\x1a\r.nrpc.NoReply\"\x00\x12G\n\x12MtNoRequestWParams\x12\x0f.nrpc.NoRequest\x1a\x17.main.SimpleStringReply\"\x07\x8a\xb2\x19\x03mp1\x1a\x0c\xca\xf3\x18\x08\x63lientid2M\n\x10NoRequestService\x12\x39\n\x0bMtNoRequest\x12\x0f.nrpc.NoRequest\x1a\x17.main.SimpleStringReply\"\x00\x42\x1c\x82\xb5\x18\x04root\x8a\xb5\x18\x08instance\x90\xb5\x18\x01\x98\xb5\x18\x01\x62\x06proto3'
  ,
  dependencies=[nrpc_dot_nrpc__pb2.DESCRIPTOR,])




_STRINGARG = _descriptor.Descriptor(
  name='StringArg',
  full_name='main.StringArg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='arg1', full_name='main.StringArg.arg1', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=68,
)


_SIMPLESTRINGREPLY = _descriptor.Descriptor(
  name='SimpleStringReply',
  full_name='main.SimpleStringReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='main.SimpleStringReply.reply', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=104,
)

DESCRIPTOR.message_types_by_name['StringArg'] = _STRINGARG
DESCRIPTOR.message_types_by_name['SimpleStringReply'] = _SIMPLESTRINGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StringArg = _reflection.GeneratedProtocolMessageType('StringArg', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARG,
  '__module__' : 'alloptions_pb2'
  # @@protoc_insertion_point(class_scope:main.StringArg)
  })
_sym_db.RegisterMessage(StringArg)

SimpleStringReply = _reflection.GeneratedProtocolMessageType('SimpleStringReply', (_message.Message,), {
  'DESCRIPTOR' : _SIMPLESTRINGREPLY,
  '__module__' : 'alloptions_pb2'
  # @@protoc_insertion_point(class_scope:main.SimpleStringReply)
  })
_sym_db.RegisterMessage(SimpleStringReply)


DESCRIPTOR._options = None

_SVCCUSTOMSUBJECT = _descriptor.ServiceDescriptor(
  name='SvcCustomSubject',
  full_name='main.SvcCustomSubject',
  file=DESCRIPTOR,
  index=0,
  serialized_options=b'\302\363\030\016custom_subject',
  create_key=_descriptor._internal_create_key,
  serialized_start=107,
  serialized_end=466,
  methods=[
  _descriptor.MethodDescriptor(
    name='MtSimpleReply',
    full_name='main.SvcCustomSubject.MtSimpleReply',
    index=0,
    containing_service=None,
    input_type=_STRINGARG,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=b'\202\262\031\017mt_simple_reply',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtVoidReply',
    full_name='main.SvcCustomSubject.MtVoidReply',
    index=1,
    containing_service=None,
    input_type=_STRINGARG,
    output_type=nrpc_dot_nrpc__pb2._VOID,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtNoRequest',
    full_name='main.SvcCustomSubject.MtNoRequest',
    index=2,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._NOREQUEST,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtStreamedReply',
    full_name='main.SvcCustomSubject.MtStreamedReply',
    index=3,
    containing_service=None,
    input_type=_STRINGARG,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=b'\220\262\031\001',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtVoidReqStreamedReply',
    full_name='main.SvcCustomSubject.MtVoidReqStreamedReply',
    index=4,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._VOID,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=b'\220\262\031\001',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVCCUSTOMSUBJECT)

DESCRIPTOR.services_by_name['SvcCustomSubject'] = _SVCCUSTOMSUBJECT


_SVCSUBJECTPARAMS = _descriptor.ServiceDescriptor(
  name='SvcSubjectParams',
  full_name='main.SvcSubjectParams',
  file=DESCRIPTOR,
  index=1,
  serialized_options=b'\312\363\030\010clientid',
  create_key=_descriptor._internal_create_key,
  serialized_start=469,
  serialized_end=692,
  methods=[
  _descriptor.MethodDescriptor(
    name='MtWithSubjectParams',
    full_name='main.SvcSubjectParams.MtWithSubjectParams',
    index=0,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._VOID,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=b'\212\262\031\003mp1\212\262\031\003mp2',
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtNoReply',
    full_name='main.SvcSubjectParams.MtNoReply',
    index=1,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._VOID,
    output_type=nrpc_dot_nrpc__pb2._NOREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='MtNoRequestWParams',
    full_name='main.SvcSubjectParams.MtNoRequestWParams',
    index=2,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._NOREQUEST,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=b'\212\262\031\003mp1',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SVCSUBJECTPARAMS)

DESCRIPTOR.services_by_name['SvcSubjectParams'] = _SVCSUBJECTPARAMS


_NOREQUESTSERVICE = _descriptor.ServiceDescriptor(
  name='NoRequestService',
  full_name='main.NoRequestService',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=694,
  serialized_end=771,
  methods=[
  _descriptor.MethodDescriptor(
    name='MtNoRequest',
    full_name='main.NoRequestService.MtNoRequest',
    index=0,
    containing_service=None,
    input_type=nrpc_dot_nrpc__pb2._NOREQUEST,
    output_type=_SIMPLESTRINGREPLY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_NOREQUESTSERVICE)

DESCRIPTOR.services_by_name['NoRequestService'] = _NOREQUESTSERVICE

# @@protoc_insertion_point(module_scope)
