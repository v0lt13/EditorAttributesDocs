EditorExtension
===============

The class that expands the base editor functionality, redrawing the editor with UIElements and makes attributes like 
:doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/DecorativeAttributes/guicolor` and :doc:`../Attributes/MiscellaneousAttributes/hideproperty` work.

It is reccomended to derive any custom editor classes from this so the previously mentioned attributes work.

**Inheritance:**
	- *object* -> *UnityEngine.Object* -> *ScriptableObject* -> *Editor* -> *EditorExtension*

**Namespace:** 
	*EditorAttributes.Editor*
	
**Assembly:**
	*EditorAttributes.Editor.asmdef*
	
Syntax::

	[CanEditMultipleObjects, CustomEditor(typeof(Object), true)]
	public class EditorExtension : UnityEditor.Editor

Fields:
-------

DEFAULT_GLOBAL_COLOR
--------------------

The default global color.

**Type:** ``Color``

Declaration::

	public static readonly Color DEFAULT_GLOBAL_COLOR = new(0.8f, 0.8f, 0.8f, 1.0f);

GLOBAL_COLOR
------------

The current global color.

**Type:** ``Color``

Declaration::

	public static Color GLOBAL_COLOR = DEFAULT_GLOBAL_COLOR;

Methods:
--------

OnEnable()
----------

This function is called when the object becomes enabled and active.

.. warning::
	If you override this function make sure you call base.OnEnable()

Declaration::

	protected virtual void OnEnable()

OnDisable()
----------

This function is called when the object becomes disabled or inactive.

.. warning::
	If you override this function make sure you call base.OnDisable()

Declaration::

	protected virtual void OnDisable()
	
CreateInspectorGUI()
--------------------

Implement this method to make a custom UIElements inspector.

.. warning::
	If you override this function make sure you call base.CreateInspectorGUI()

Declaration::

	public override VisualElement CreateInspectorGUI()
	
**Returns:** ``VisualElement``: The created inspector
	
Overrides::

	Editor.CreateInspectorGUI()

DrawDefaultInspector()
----------------------

This function redraws all the inspector properties with UIElements and handles the coloring and hiding of properties.

.. warning::
	If you override this function make sure you call base.DrawDefaultInspector() or handle property hiding and coloring yourself
	
Declaration::

	protected virtual new VisualElement DrawDefaultInspector()
	
**Returns:** ``VisualElement``: All the inspector properties
	
RunUpdateLoop(VisualElement)
----------------------------

Runs the update loop on elements that use the :doc:`propertydrawerbase/UpdateVisualElement` function.
Call this function in the CreateGUI function to have conditional attributes and dynamic string attributes work in custom editor windows.

**Parameters:**
	- ``VisualElement`` root: The root element of the editor

Declaration::

	public static void RunUpdateLoop(VisualElement root)
	
DrawStaticFields()
------------------

Draws all the static and const fields.

Declaration::

	protected VisualElement DrawStaticFields()
	
**Returns:** ``VisualElement``: A visual element containing all static and const fields
	
DrawButtons()
-------------

Draws all the buttons from functions using the Button Attribute.

Declaration::

	protected VisualElement DrawButtons()
	
**Returns:** ``VisualElement``: A visual element containing all drawn buttons
