VectorUtils
===========

An utility class containing usefull functions related to vectors

**Inheritance:**
	- *object* -> *VectorUtils*

**Namespace:** 
	*EditorAttributes.Editor.Utility*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	public static class VectorUtils

Methods:
--------

AddVector(Vector3, float)
^^^^^^^^^^^^^^^^^^^^^^^^^

Adds a value to a vector.

Declaration::

	public static Vector3 AddVector(Vector3 vector, float addend)
	
**Parameters:**
	- ``Vector3`` vector: The vector to add the value to
	- ``float`` addend: The value to add
	
**Returns:** ``Vector3``: A vector with the value added to all axis

SubtractVector(Vector3, float)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Subtracts a value from a vector.

Declaration::

	public static Vector3 SubtractVector(Vector3 vector, float subtrahend)
	
**Parameters:**
	- ``Vector3`` vector: The vector to subtract the value from
	- ``float`` subtrahend: The value to subtract
	
**Returns:** ``Vector3``: A vector with the value subtracted from all axis

Vector3IntToVector2Int(Vector3Int)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a ``Vector3Int`` to a ``Vector2Int``.

Declaration::

	public static Vector2Int Vector3IntToVector2Int(Vector3Int vector3Int)
	
**Parameters:**
	- ``Vector3Int`` vector3Int: The Vector3Int to convert
	
**Returns:** ``Vector2Int``: The converted Vector2Int

Vector2IntToVector2(Vector2Int)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a ``Vector2Int`` to a ``Vector2``.

Declaration::

	public static Vector2 Vector2IntToVector2(Vector2Int vector2int)
	
**Parameters:**
	- ``Vector2Int`` vector2Int: The Vector2Int to convert
	
**Returns:** ``Vector2``: The converted Vector2

Vector2ToVector2Int(Vector3Int)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a ``Vector2`` to a ``Vector2Int``.

Declaration::

	public static Vector2Int Vector2ToVector2Int(Vector2 vector2)
	
**Parameters:**
	- ``Vector2`` vector2: The Vector2 to convert
	
**Returns:** ``Vector2Int``: The converted Vector2Int

Vector3ToVector3Int(Vector3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Converts a ``Vector3`` to a ``Vector3Int``.

Declaration::

	public static Vector3Int Vector3ToVector3Int(Vector3 vector3)
	
**Parameters:**
	- ``Vector3`` vector3: The Vector3 to convert
	
**Returns:** ``Vector3Int``: The converted Vector3Int

ParseVector2(string)
^^^^^^^^^^^^^^^^^^^^

Parses a ``string`` to a ``Vector2``.

Declaration::

	public static Vector2 ParseVector2(string vectorString)
	
**Parameters:**
	- ``string`` vectorString: The string representing the vector
	
**Returns:** ``Vector2``: The vector value from the string

ParseVector2Int(string)
^^^^^^^^^^^^^^^^^^^^^^^

Parses a ``string`` to a ``Vector2Int``.

Declaration::

	public static Vector2Int ParseVector2Int(string vectorString)
	
**Parameters:**
	- ``string`` vectorString: The string representing the vector
	
**Returns:** ``Vector2Int``: The vector value from the string

ParseVector3(string)
^^^^^^^^^^^^^^^^^^^^

Parses a ``string`` to a ``Vector3``.

Declaration::

	public static Vector3 ParseVector3(string vectorString)
	
**Parameters:**
	- ``string`` vectorString: The string representing the vector
	
**Returns:** ``Vector3``: The vector value from the string

ParseVector3Int(string)
^^^^^^^^^^^^^^^^^^^^^^^

Parses a ``string`` to a ``Vector3Int``.

Declaration::

	public static Vector3Int ParseVector3Int(string vectorString)
	
**Parameters:**
	- ``string`` vectorString: The string representing the vector
	
**Returns:** ``Vector3Int``: The vector value from the string

ParseVector4(string)
^^^^^^^^^^^^^^^^^^^^

Parses a ``string`` to a ``Vector4``.

Declaration::

	public static Vector4 ParseVector4(string vectorString)
	
**Parameters:**
	- ``string`` vectorString: The string representing the vector
	
**Returns:** ``Vector4``: The vector value from the string
