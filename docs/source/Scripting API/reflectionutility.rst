ReflectionUtility
=================

An utiliy class containing usefull functions related to reflection.

**Inheritance:**
	- *object* -> *ReflectionUtility*

**Namespace:** 
	EditorAttributes.Editor.Utility
	
**Assembly:**
	EditorAttributes.Editor.asmdef
	
Syntax::
	public static class ReflectionUtility

***Fields:***

BINDING_FLAGS
-------------

A preset of binding flags used by the package.

**Type:** ``BindingFlags``

Declaration::
	public const BindingFlags BINDING_FLAGS = BindingFlags.Instance | BindingFlags.Public | BindingFlags.NonPublic | BindingFlags.Static;

***Methods:***

FindField(string, SerializedProperty)
-------------------------------------

Finds a field inside a serialized object.

Declaration::
	public static FieldInfo FindField(string fieldName, SerializedProperty property)
	
**Parameters:**
	- ``string`` fieldName: The name of the field to search
	- ``SerializedProperty`` property: The serialized property

**Returns:** ``FieldInfo``: The field info of the desired field

FindProperty(string, SerializedProperty)
----------------------------------------

Finds a property inside a serialized object.

Declaration::
	public static PropertyInfo FindProperty(string propertyName, SerializedProperty property)
	
**Parameters:**
	- ``string`` propertyName: The name of the property to search
	- ``SerializedProperty`` property: The serialized property

**Returns:** ``PropertyInfo``: The property info of the desired property

FindFunction(string, SerializedProperty)
----------------------------------------

Finds a funciton inside a serialized object.

Declaration::
	public static MethodInfo FindFunction(string functionName, SerializedProperty property)
	
**Parameters:**
	- ``string`` functionName: The name of the function to search
	- ``SerializedProperty`` property: The serialized property

**Returns:** ``MethodInfo``: The field info of the desired field

FindMember(string, Type, BindingFlags, MemberTypes)
---------------------------------------------------

Finds a member from the target type.

Declaration::
	public static MemberInfo FindMember(string memberName, Type targetType, BindingFlags bindingFlags, MemberTypes memberType)
	
**Parameters:**
	- ``string`` memberName: The name of the member to look for
	- ``Type`` targetType: The type to get the member from
	- ``BindingFlags`` bindingFlags: The binding flags
	- ``MemberTypes`` memberType: The type of the member to look for. Only Field, Property and Method are supported

**Returns:** ``MemberInfo``: The member info of the desired member

TryGetField(string, Type, BindingFlags, out FieldInfo)
------------------------------------------------------

Tries to get a field from the target type.

Declaration::
	public static bool TryGetField(string name, Type targetType, BindingFlags bindingFlags, out FieldInfo fieldInfo)
	
**Parameters:**
	- ``string`` name: The name of the field to search for
	- ``Type`` targetType: The type to get the field from
	- ``BindingFlags`` bindingFlags: The binding flags
	- `output`, ``FieldInfo`` fieldInfo: The field info of the desired field

**Returns:** ``bool``: True if the field was succesfully found, false otherwise

TryGetProperty(string, Type, BindingFlags, out PropertyInfo)
------------------------------------------------------------

Tries to get a property from the target type.

Declaration::
	public static bool TryGetProperty(string name, Type targetType, BindingFlags bindingFlags, out PropertyInfo propertyInfo)
	
**Parameters:**
	- ``string`` name: The name of the field to search for
	- ``Type`` targetType: The type to get the property from
	- ``BindingFlags`` bindingFlags: The binding flags
	- `output`, ``PropertyInfo`` propertyInfo: The property info of the desired field

**Returns:** ``bool``: True if the field was succesfully found, false otherwise

TryGetMethod(string, Type, BindingFlags, out MethodInfo)
--------------------------------------------------------

Tries to get a function from the target type.

Declaration::
	public static bool TryGetMethod(string name, Type targetType, BindingFlags bindingFlags, out MethodInfo methodInfo)
	
**Parameters:**
	- ``string`` name: The name of the field to search for
	- ``Type`` targetType: The type to get the function from
	- ``BindingFlags`` bindingFlags: The binding flags
	- `output`, ``MethodInfo`` methodInfo: The method info of the desired field

**Returns:** ``bool``: True if the field was succesfully found, false otherwise

IsPropertyCollection(SerializedProperty)
----------------------------------------

Checks to see if a seralized property is a list or array.

Declaration::
	public static bool IsPropertyCollection(SerializedProperty property)
	
**Parameters:**
	- ``SerializedProperty`` property: The serialized property to check

**Returns:** ``bool``: True if the property is a list or array, false otherwise

GetValidMemberInfo(string, SerializedProperty)
----------------------------------------------

Finds a member inside a serialzied object.

Declaration::
	public static MemberInfo GetValidMemberInfo(string memberName, SerializedProperty serializedProperty)
	
**Parameters:**
	- ``string`` memberName: The name of the member to look for
	- ``SerializedProperty`` property: The serialized property

**Returns:** ``MemberInfo``: The member info of the member

GetNestedObjectType(SerializedProperty, out object)
---------------------------------------------------

Gets the type of a nested serialized object.

Declaration::
	public static Type GetNestedObjectType(SerializedProperty property, out object nestedObject)
	
**Parameters:**
	- ``SerializedProperty`` property: The serialized property
	- `output`, ``object`` nestedObject: Outputs the serialized nested object

**Returns:** ``Type``: The nested object type

GetMemberInfoType(MemberInfo)
-----------------------------

Gets the type of a member.

Declaration::
	public static Type GetMemberInfoType(MemberInfo memberInfo)
	
**Parameters:**
	- ``MemberInfo`` memberInfo: The member to get the type from

**Returns:** ``Type``: The type of the member

GetMemberInfoValue(MemberInfo, SerializedProperty)
--------------------------------------------------

Gets the value of a member.

Declaration::
	public static object GetMemberInfoValue(MemberInfo memberInfo, SerializedProperty property)
	
**Parameters:**
	- ``MemberInfo`` memberInfo: The member to get the value from
	- ``SerializedProperty`` property: The serialized property

**Returns:** ``object``: The value of the member
