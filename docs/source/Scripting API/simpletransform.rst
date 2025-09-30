SimpleTransform
===============

A simple unity serializable transform struct that can be used with the :doc:`../Attributes/NumericalAttributes/drawhandle`.

**Namespace:** 
	*EditorAttributes*
	
**Assembly:**
	*EditorAttributes.asmdef*
	
Syntax::

	[Serializable]
	public struct SimpleTransform

Fields:
-------

position
^^^^^^^^

Position value.

**Type:** ``Vector3``

Declaration::

	public Vector3 position;
	
rotation
^^^^^^^^

Rotation value in euler angles.

**Type:** ``Vector3``

Declaration::

	public Vector3 rotation;
	
scale
^^^^^

Scale value.

**Type:** ``Vector3``

Declaration::

	public Vector3 scale;

Properties:
-----------

QuaternionRotation
^^^^^^^^^^^^^^^^^^

The rotation of the transform as a quaternion.

Declaration::

	public readonly Quaternion QuaternionRotation;

Constructors:
-------------

SimpleTransform(Vector3, Vector3, Vector3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Construct a SimpleTransform.

Declaration::

	public SimpleTransform(Vector3 position, Vector3 rotation, Vector3 scale)
	
**Parameters:**
	- ``Vector3`` position: Input position
	- ``Vector3`` rotation: Input rotation
	- ``Vector3`` scale: Input scale

SimpleTransform(Vector3, Quaternion, Vector3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Construct a SimpleTransform.

Declaration::

	public SimpleTransform(Vector3 position, Quaternion rotation, Vector3 scale)
	
**Parameters:**
	- ``Vector3`` position: Input position
	- ``Quaternion`` rotation: Input rotation
	- ``Vector3`` scale: Input scale

SimpleTransform(Transform)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Construct a SimpleTransform.

Declaration::

	public SimpleTransform(Transform transform)
	
**Parameters:**
	- ``Transform`` transform: Input transform

Operators:
----------

implicit operator SimpleTransform(Transform)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Implicitly converts a ``Transform`` to ``SimpleTransform``.

Declaration::

	public static implicit operator SimpleTransform(Transform transform);
	
**Parameters:**
	- ``Transform`` transform: Input transform

Methods:
--------

ToString()
^^^^^^^^^^

Returns the transform values as string.

Declaration::

	public override readonly string ToString();
	
**Returns:** ``string``: A string with the transform values

Overrides::

	ValueType.ToString()

ToTransform(Transform)
^^^^^^^^^^^^^^^^^^^^^^

Puts the SimpleTransform values to into a Transform in world space.

Declaration::

	public readonly void ToTransform(Transform transform)
	
**Parameters:**
	- ``Transform`` transform: The transform to put the values into

ToLocalTransform(Transform)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Puts the SimpleTransform values to into a Transform in local space.

Declaration::

	public readonly void ToLocalTransform(Transform transform)
	
**Parameters:**
	- ``Transform`` transform: The transform to put the values into
