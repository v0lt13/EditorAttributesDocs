EditorValidation
================

The class that handles the validation system used by the :doc:`../Attributes/MiscellaneousAttributes/required` and :doc:`../Attributes/MiscellaneousAttributes/validate`.

**Inheritance:**
	- *object* -> *EditorValidation*

**Implements:**
	- IPreprocessBuildWithReport

**Namespace:** 
	*EditorAttributes.Editor*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	[InitializeOnLoad]
	public class EditorExtension : IPreprocessBuildWithReport

Properties:
-----------

callbackOrder
-------------

Returns the relative callback order for callbacks. Callbacks with lower values are called before ones with higher values.

**Type:** ``int``

Declaration::

	public int callbackOrder => 0;

Methods:
--------

OnPreprocessBuild(BuildReport)
------------------------------

Implement this function to receive a callback before the build is started.

Declaration::

	public void OnPreprocessBuild(BuildReport report)

**Parameters:**
	- ``BuildReport`` report: A report containing information about the build, such as its target platform and output path

ValidateAll()
-------------

Validates every asset and scene in the project.

Declaration::

	[MenuItem("EditorValidation/Validate All", priority = 0)]
	public static void ValidateAll()
	
ValidateOpenScenes()
--------------------

Validates all scenes in the build.

Declaration::

		[MenuItem("EditorValidation/Validate Scenes", priority = 2)]
		public static void ValidateAllScenes()

ValidateAllScenes()
-------------------

Validates all scenes currently open.

Declaration::

		[MenuItem("EditorValidation/Validate Open Scenes", priority = 3)]
		public static void ValidateOpenScenes()

ValidateAllAssets()
-------------------

Validates all assets in the project.

Declaration::

		[MenuItem("EditorValidation/Validate Assets", priority = 1)]
		public static void ValidateAllAssets()
	
Validate(Object, ref int, ref int)
----------------------------------

Validates all fields marked for validation with an attribute.

Declaration::

		public static void Validate(Object targetObject, ref int failedValidations, ref int successfulValidations)
		
**Parameters:**
	- ``Object`` targetObject: The target object to validate
	- `reference`, ``int`` failedValidations: The amount of validations that failed
	- `reference`, ``int`` successfulValidations: The amount of validations that succeded
	
IsPackageAsset(string)
----------------------

Checks to see if an asset is inside the Packages folder.

Declaration::

		public static bool IsPackageAsset(string assetPath)
		
**Parameters:**
	- ``string`` assetPath: The path of the asset
	
**Returns:** ``bool``: True if the asset is inside the packages folder
