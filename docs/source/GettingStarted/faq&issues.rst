FAQ & Common Issues
===================

Common Issues
-------------

1. The attribute applies on the collection elements instead of the collection itself.

- Unity only supports property drawers applying to collections in Unity 6 and above, upgrading your project will fix the issue.
  
2. Attribute doesn't work on custom serialized object members inside collections.

- It's a Unity bug, a temporary solution until Unity fixes this is to go to the attribute's definition and add an additional parameter to any of the constructors like this ``ExampleConstructor(applyToCollection = false) : base(applyToCollection)`` now you can individually set when an attribute should apply to a collection or not from the attribute itself, leaving it to ``false`` will fix the problem with nested objects in collections.

3. Attributes like :doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/MiscellaneousAttributes/showininspector`, :doc:`../Attributes/DecorativeAttributes/guicolor` and :doc:`../Attributes/DecorativeAttributes/propertyorder` don't work after I create a custom inspector.

- The logic for :doc:`../Attributes/ButtonAttributes/button`, :doc:`../Attributes/MiscellaneousAttributes/showininspector`, :doc:`../Attributes/DecorativeAttributes/guicolor` and :doc:`../Attributes/DecorativeAttributes/propertyorder` is implemented in an :doc:`../Scripting API/editorextension` class that inherits from the `UnityEditor.Editor <https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Editor.html>`_ class, if you want those attributes to work with your custom editor you need to inherit your editor from :doc:`../Scripting API/editorextension` and call the appropriate functions

Frequently Asked Questions
--------------------------

Q: With what Unity version is the package compatible with?

A: The package is compatible with Unity 2022 and above, but there a few features that are only available in Unity 6 and above. Package versions before v2.2.0 that use ImGUI may be compatible with Unity 2021 as well.

Q: Does this package serialize Dictionaries, HashSets, 2D Arrays, etc.?

A: No, custom serialization is a completly different beast and not the purpose of this package and it is not something that will be implemented in the future. But there are plenty of free custom serializers on the internet that you can use along with this package. 

Q: Whats the difference between this package and others like it (`Odin Inspector <https://odininspector.com/>`_, `Naughty Attributes <https://github.com/dbrizov/NaughtyAttributes>`_, `Tri-Inspector <https://github.com/codewriter-packages/Tri-Inspector>`_, etc.)?

A: I can spend hours making a comparison list for each package, the gist of it is that EditorAttributes has most of the features Odin has along with some extra ones but for free and open sourced, unlike Naughty Attributes it's built on `UI Toolkit <https://docs.unity3d.com/6000.1/Documentation/Manual/ui-systems/introduction-ui-toolkit.html>`_ so it's lightweight, modern, constantly updated and designed with the default Unity look and feel to it. But this package doesn't come close to the production level of Odin since it's just me, myself and I, and it doesn't rewrite the entire inspector or does custom serialization logic. Either way it's always best to research each package for yourself and conclude what fits best for your project.

Q: Can I contribute to the package?

A: Of course! Thats basically the point of open source, just create a pull requests and if your contribution is good for the package it will be accepted. If you want contribute a completly new feature/attribute/API talk with me first since for that documentation must also be written and I need to make sure everything is tested, has a sample and fits the package.

Q: Should I get the Github version or Asset Store version?

A: There is no content difference between the Github version and the Asset Store version of the package. The only differences are in the licence, installation and update delivery.

- On Github the package is licenced as public domain while on the Unity Asset Store it licenced with the standard Unity Extension Asset licence.
- On Github if you install the package from the git URL it will install in the Packages folder of Unity which makes the package read only, installing it from the asset store will add it in the Assets folder which will allow modifications.
- On Github you can receive a package update as soon as it's pushed along with any pull requests done by any contribuitors. On the Asset Store there is a review process the update must go trough which can last up to 3 days and any contributions done after an update will only be added in the next package update.

Q: I found a problem/bug with the package, what do I do?

A: If you found a problem/bug just go to the `issues tab <https://github.com/v0lt13/EditorAttributes/issues>`_ on GitHub and create a new issue explaining what and how it happened in detail with reproduction steps make sure you check other closed issues first and the :doc:`commonissues` page, additionaly you can join the `discord server <https://discord.gg/jKXvXyTzYn>`_ and make the issue apparent there.

Q: I have a feature idea, where do I put it?

A: Simply create a new discussion at the `discussions tab <https://github.com/v0lt13/EditorAttributes/discussions>`_ on GitHub or join the `discord server <https://discord.gg/jKXvXyTzYn>`_ and tell me more about the feature and it's usecase.

Q: I found a typo or an error in the documentation, what do I do?

A: You can either raise the issue on GitHub, on discord or the `documentation repo <https://github.com/v0lt13/EditorAttributesDocs>`_, you can also create a pull request there and fix the issue yourself.

Q: When is the next update coming?

A: I usually let submitted bugs/features/improvements or other ideas I have pile up on my Trello board and once there is enough content for an update I do them all at once, rather then creating 10 minor updates with one thing each. Unless there is a critical package braking issue happening in which case I fix it immediatly and push the fix on the same version.

Q: Is there any performance impact from using this package?

A: While the package is lightweight there is a small impact on editor performance that comes by default with more customization complexity but it should be negligible, if you actually experience considerably decreased editor performace try decreasing the complexity of your editors.
