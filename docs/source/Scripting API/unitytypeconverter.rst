UnityTypeConverter
==================

A custom JSON converter used by the :doc:`../Attributes/ButtonAttributes/button` to serialize the following Unity types: 
``Vector2``, ``Vector2Int``, ``Vector3``, ``Vector3Int``, ``Vector4``, ``Color``, ``Rect``, ``RectInt``, ``Bounds``, ``BoundsInt``

**Inheritance:**
	- *object* -> *JsonConverter* -> *UnityTypeConverter*

**Namespace:** 
	*EditorAttributes.Editor.Utility*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	public class UnityTypeConverter : JsonConverter

Methods:
--------

CanConvert(Type)
^^^^^^^^^^^^^^^^

Determines whether this instance can convert the specified object type.

Declaration::

	public override bool CanConvert(Type objectType)
	
**Parameters:**
	- ``Type`` objectType: The object type
	
**Returns:** ``bool``: true if this instance can convert the specified object type; otherwise, false
	
Overrides::

	JsonConverter.CanConvert(Type)

ReadJson(JsonReader, Type, object?, JsonSerializer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reads the JSON representation of the object.

Declaration::

	public override object? ReadJson(JsonReader reader, Type objectType, object? existingValue, JsonSerializer serializer)
	
**Parameters:**
	- ``JsonReader`` reader: The JSON reader to read from
	- ``Type`` objectType: The object type
	- ``object?`` existingValue: The existing value of object being read
	- ``Type`` serializer: The calling serializer

**Returns:** ``object?``: The object value

Overrides::

	JsonConverter.ReadJson(JsonReader, Type, object?, JsonSerializer)

WriteJson(JsonWriter, object?, JsonSerializer)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Writes the JSON representation of the object.

Declaration::

	public override void WriteJson(JsonWriter writer, object? value, JsonSerializer serializer) 
	
**Parameters:**
	- ``JsonWriter`` writer: Writes the JSON representation of the object
	- ``object?`` value: The value
	- ``JsonSerializer`` serializer: The calling serializer

Overrides::

	JsonConverter.WriteJson(JsonWriter, object?, JsonSerializer)
