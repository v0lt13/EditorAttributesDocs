Rename Attribute
================

Attribute to rename a field in the inspector

**Parameters:**
	- ``string`` name: The new name of the field
	- `optional`, ``CaseType`` caseType: In what case to rename the field

Example::

	using UnityEngine;
	using EditorAttributes;
	
	public class AttributesExample : MonoBehaviour
	{
		[SerializeField] private int intField;
		[Space]
		[SerializeField, Rename("Int Field")] private int intField2;
		[SerializeField, Rename("pascal case mode", CaseType.Pascal)] private int intField3;
		[SerializeField, Rename("Camel Case mode", CaseType.Camel)] private int intField4;
		[SerializeField, Rename("snake case mode", CaseType.Snake)] private int intField5;
		[SerializeField, Rename("kebab case mode", CaseType.Kebab)] private int intField6;
		[SerializeField, Rename("upper case mode", CaseType.Upper)] private int intField7;
		[SerializeField, Rename("LOWER CASE MODE", CaseType.Lower)] private int intField8;
	}
	
.. image:: ../Images/Rename01.png
