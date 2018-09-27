# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/node_execution.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.event import event_pb2 as flyteidl_dot_event_dot_event__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='flyteidl/admin/node_execution.proto',
  package='flyteidl.admin',
  syntax='proto3',
  serialized_pb=_b('\n#flyteidl/admin/node_execution.proto\x12\x0e\x66lyteidl.admin\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1a\x66lyteidl/event/event.proto\"W\n\x17NodeExecutionIdentifier\x12\x0f\n\x07node_id\x18\x01 \x01(\t\x12\x14\n\x0c\x65xecution_id\x18\x02 \x01(\t\x12\x15\n\rretry_attempt\x18\x03 \x01(\r\"4\n\x17NodeExecutionGetRequest\x12\x19\n\x11node_execution_id\x18\x01 \x01(\t\"J\n\x18NodeExecutionListRequest\x12\r\n\x05limit\x18\x01 \x01(\r\x12\x0e\n\x06offset\x18\x02 \x01(\r\x12\x0f\n\x07\x66ilters\x18\x03 \x01(\t\"\xa9\x01\n\rNodeExecution\x12\x33\n\x02id\x18\x01 \x01(\x0b\x32\'.flyteidl.admin.NodeExecutionIdentifier\x12\x19\n\x11node_execution_id\x18\x02 \x01(\t\x12\x11\n\tinput_uri\x18\x03 \x01(\t\x12\x35\n\x07\x63losure\x18\x04 \x01(\x0b\x32$.flyteidl.admin.NodeExecutionClosure\"K\n\x11NodeExecutionList\x12\x36\n\x0fnode_executions\x18\x01 \x03(\x0b\x32\x1d.flyteidl.admin.NodeExecution\"\xf2\x02\n\x14NodeExecutionClosure\x12\x39\n\rtask_metadata\x18\x01 \x01(\x0b\x32 .flyteidl.event.TaskNodeMetadataH\x00\x12=\n\x0f\x62ranch_metadata\x18\x02 \x01(\x0b\x32\".flyteidl.event.BranchNodeMetadataH\x00\x12\x44\n\x11workflow_metadata\x18\x03 \x01(\x0b\x32\'.flyteidl.event.SubworkflowNodeMetadataH\x00\x12\x14\n\noutput_uri\x18\x04 \x01(\tH\x01\x12.\n\x05\x65rror\x18\x05 \x01(\x0b\x32\x1d.flyteidl.core.ExecutionErrorH\x01\x12\x30\n\x05phase\x18\x06 \x01(\x0e\x32!.flyteidl.core.NodeExecutionPhaseB\x11\n\x0ftarget_metadataB\x0f\n\routput_resultB3Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/adminb\x06proto3')
  ,
  dependencies=[flyteidl_dot_core_dot_execution__pb2.DESCRIPTOR,flyteidl_dot_event_dot_event__pb2.DESCRIPTOR,])




_NODEEXECUTIONIDENTIFIER = _descriptor.Descriptor(
  name='NodeExecutionIdentifier',
  full_name='flyteidl.admin.NodeExecutionIdentifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='flyteidl.admin.NodeExecutionIdentifier.node_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='execution_id', full_name='flyteidl.admin.NodeExecutionIdentifier.execution_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='retry_attempt', full_name='flyteidl.admin.NodeExecutionIdentifier.retry_attempt', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=201,
)


_NODEEXECUTIONGETREQUEST = _descriptor.Descriptor(
  name='NodeExecutionGetRequest',
  full_name='flyteidl.admin.NodeExecutionGetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_execution_id', full_name='flyteidl.admin.NodeExecutionGetRequest.node_execution_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=203,
  serialized_end=255,
)


_NODEEXECUTIONLISTREQUEST = _descriptor.Descriptor(
  name='NodeExecutionListRequest',
  full_name='flyteidl.admin.NodeExecutionListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='flyteidl.admin.NodeExecutionListRequest.limit', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='flyteidl.admin.NodeExecutionListRequest.offset', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filters', full_name='flyteidl.admin.NodeExecutionListRequest.filters', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=257,
  serialized_end=331,
)


_NODEEXECUTION = _descriptor.Descriptor(
  name='NodeExecution',
  full_name='flyteidl.admin.NodeExecution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='flyteidl.admin.NodeExecution.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_execution_id', full_name='flyteidl.admin.NodeExecution.node_execution_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='input_uri', full_name='flyteidl.admin.NodeExecution.input_uri', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closure', full_name='flyteidl.admin.NodeExecution.closure', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=334,
  serialized_end=503,
)


_NODEEXECUTIONLIST = _descriptor.Descriptor(
  name='NodeExecutionList',
  full_name='flyteidl.admin.NodeExecutionList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_executions', full_name='flyteidl.admin.NodeExecutionList.node_executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=505,
  serialized_end=580,
)


_NODEEXECUTIONCLOSURE = _descriptor.Descriptor(
  name='NodeExecutionClosure',
  full_name='flyteidl.admin.NodeExecutionClosure',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task_metadata', full_name='flyteidl.admin.NodeExecutionClosure.task_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='branch_metadata', full_name='flyteidl.admin.NodeExecutionClosure.branch_metadata', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_metadata', full_name='flyteidl.admin.NodeExecutionClosure.workflow_metadata', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_uri', full_name='flyteidl.admin.NodeExecutionClosure.output_uri', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='flyteidl.admin.NodeExecutionClosure.error', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phase', full_name='flyteidl.admin.NodeExecutionClosure.phase', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='target_metadata', full_name='flyteidl.admin.NodeExecutionClosure.target_metadata',
      index=0, containing_type=None, fields=[]),
    _descriptor.OneofDescriptor(
      name='output_result', full_name='flyteidl.admin.NodeExecutionClosure.output_result',
      index=1, containing_type=None, fields=[]),
  ],
  serialized_start=583,
  serialized_end=953,
)

_NODEEXECUTION.fields_by_name['id'].message_type = _NODEEXECUTIONIDENTIFIER
_NODEEXECUTION.fields_by_name['closure'].message_type = _NODEEXECUTIONCLOSURE
_NODEEXECUTIONLIST.fields_by_name['node_executions'].message_type = _NODEEXECUTION
_NODEEXECUTIONCLOSURE.fields_by_name['task_metadata'].message_type = flyteidl_dot_event_dot_event__pb2._TASKNODEMETADATA
_NODEEXECUTIONCLOSURE.fields_by_name['branch_metadata'].message_type = flyteidl_dot_event_dot_event__pb2._BRANCHNODEMETADATA
_NODEEXECUTIONCLOSURE.fields_by_name['workflow_metadata'].message_type = flyteidl_dot_event_dot_event__pb2._SUBWORKFLOWNODEMETADATA
_NODEEXECUTIONCLOSURE.fields_by_name['error'].message_type = flyteidl_dot_core_dot_execution__pb2._EXECUTIONERROR
_NODEEXECUTIONCLOSURE.fields_by_name['phase'].enum_type = flyteidl_dot_core_dot_execution__pb2._NODEEXECUTIONPHASE
_NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['task_metadata'])
_NODEEXECUTIONCLOSURE.fields_by_name['task_metadata'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata']
_NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['branch_metadata'])
_NODEEXECUTIONCLOSURE.fields_by_name['branch_metadata'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata']
_NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['workflow_metadata'])
_NODEEXECUTIONCLOSURE.fields_by_name['workflow_metadata'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['target_metadata']
_NODEEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['output_uri'])
_NODEEXECUTIONCLOSURE.fields_by_name['output_uri'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['output_result']
_NODEEXECUTIONCLOSURE.oneofs_by_name['output_result'].fields.append(
  _NODEEXECUTIONCLOSURE.fields_by_name['error'])
_NODEEXECUTIONCLOSURE.fields_by_name['error'].containing_oneof = _NODEEXECUTIONCLOSURE.oneofs_by_name['output_result']
DESCRIPTOR.message_types_by_name['NodeExecutionIdentifier'] = _NODEEXECUTIONIDENTIFIER
DESCRIPTOR.message_types_by_name['NodeExecutionGetRequest'] = _NODEEXECUTIONGETREQUEST
DESCRIPTOR.message_types_by_name['NodeExecutionListRequest'] = _NODEEXECUTIONLISTREQUEST
DESCRIPTOR.message_types_by_name['NodeExecution'] = _NODEEXECUTION
DESCRIPTOR.message_types_by_name['NodeExecutionList'] = _NODEEXECUTIONLIST
DESCRIPTOR.message_types_by_name['NodeExecutionClosure'] = _NODEEXECUTIONCLOSURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NodeExecutionIdentifier = _reflection.GeneratedProtocolMessageType('NodeExecutionIdentifier', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONIDENTIFIER,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionIdentifier)
  ))
_sym_db.RegisterMessage(NodeExecutionIdentifier)

NodeExecutionGetRequest = _reflection.GeneratedProtocolMessageType('NodeExecutionGetRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONGETREQUEST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionGetRequest)
  ))
_sym_db.RegisterMessage(NodeExecutionGetRequest)

NodeExecutionListRequest = _reflection.GeneratedProtocolMessageType('NodeExecutionListRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONLISTREQUEST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionListRequest)
  ))
_sym_db.RegisterMessage(NodeExecutionListRequest)

NodeExecution = _reflection.GeneratedProtocolMessageType('NodeExecution', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTION,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecution)
  ))
_sym_db.RegisterMessage(NodeExecution)

NodeExecutionList = _reflection.GeneratedProtocolMessageType('NodeExecutionList', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONLIST,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionList)
  ))
_sym_db.RegisterMessage(NodeExecutionList)

NodeExecutionClosure = _reflection.GeneratedProtocolMessageType('NodeExecutionClosure', (_message.Message,), dict(
  DESCRIPTOR = _NODEEXECUTIONCLOSURE,
  __module__ = 'flyteidl.admin.node_execution_pb2'
  # @@protoc_insertion_point(class_scope:flyteidl.admin.NodeExecutionClosure)
  ))
_sym_db.RegisterMessage(NodeExecutionClosure)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z1github.com/lyft/flyteidl/gen/pb-go/flyteidl/admin'))
# @@protoc_insertion_point(module_scope)
