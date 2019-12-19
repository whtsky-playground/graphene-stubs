from ...types import Argument as Argument, Field as Field, Int as Int, List as List, NonNull as NonNull, ObjectType as ObjectType, Schema as Schema, String as String
from ..connection import Connection as Connection, ConnectionField as ConnectionField, PageInfo as PageInfo
from ..node import Node as Node
from typing import Any

class MyObject(ObjectType):
    class Meta:
        interfaces: Any = ...
    field: Any = ...

def test_connection() -> None: ...
def test_connection_inherit_abstracttype() -> None: ...
def test_connection_name() -> None: ...
def test_edge() -> None: ...
def test_edge_with_bases() -> None: ...
def test_edge_with_nonnull_node() -> None: ...
def test_pageinfo() -> None: ...
def test_connectionfield() -> None: ...
def test_connectionfield_node_deprecated() -> None: ...
def test_connectionfield_custom_args() -> None: ...
def test_connectionfield_required() -> Any: ...