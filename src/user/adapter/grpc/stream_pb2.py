# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstream.proto\x12\x02pb\"$\n\x07Request\x12\r\n\x05image\x18\x01 \x01(\x0c\x12\n\n\x02id\x18\x02 \x01(\t\"%\n\x08Response\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\x0c\"\x1a\n\x0cVideoRequest\x12\n\n\x02id\x18\x01 \x01(\t2\x82\x01\n\rStreamService\x12\x37\n\x16GeneratedContentStream\x12\x0b.pb.Request\x1a\x0c.pb.Response\"\x00\x30\x01\x12\x38\n\x12VideoContentStream\x12\x10.pb.VideoRequest\x1a\x0c.pb.Response\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stream_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_REQUEST']._serialized_start=20
  _globals['_REQUEST']._serialized_end=56
  _globals['_RESPONSE']._serialized_start=58
  _globals['_RESPONSE']._serialized_end=95
  _globals['_VIDEOREQUEST']._serialized_start=97
  _globals['_VIDEOREQUEST']._serialized_end=123
  _globals['_STREAMSERVICE']._serialized_start=126
  _globals['_STREAMSERVICE']._serialized_end=256
# @@protoc_insertion_point(module_scope)
