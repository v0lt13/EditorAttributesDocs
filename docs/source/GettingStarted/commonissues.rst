Common Issues
=============

1. The attribute applies on the collection elements instead of the collection itself.

- Unity only supports property drawers applying to collections in Unity 6 and above, upgrading your project will fix the issue.
  
2. Attribute doesn't work on custom serialized object members inside collections.

- It's a Unity bug, a temporary solution until Unity fixes this is to go to the attribute's definition and add an additional parameter to any of the constructors like this ``ExampleConstructor(applyToCollection = false) : base(applyToCollection)`` now you can individually set when an attribute should apply to a collection or not from the attribute itself, leaving it to ``false`` will fix the problem with nested objects in collections.

3. Attributes like :doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/MiscellaneousAttributes/showininspector`, :doc:`../Attributes/DecorativeAttributes/guicolor` and :doc:`../Attributes/DecorativeAttributes/propertyorder` don't work after I create a custom inspector.

- The logic for :doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/MiscellaneousAttributes/showininspector`, :doc:`../Attributes/DecorativeAttributes/guicolor` and :doc:`../Attributes/DecorativeAttributes/propertyorder` is implemented in an :doc:`../Scripting API/editorextension` class that inherits from the `UnityEditor.Editor <https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Editor.html>`_ class, if you want those attributes to work with your custom editor you need to inherit your editor from :doc:`../Scripting API/editorextension` and call the appropriate functions

4. Attribute doesn't work on inherited members or doesn't find it.

- The reflection system can't find inherited members if they are not accesible by the child class, mark those inherited members as ``protected`` or another modifier that gives it access to the child class.
