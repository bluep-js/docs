Blueprints scripting
====================

**Blueprint Visual Scripting** is a powerfull scripting system based on the concept of using a node-based interface. This system is extremely flexible and powerful as it provides the ability to use virtually the full range of concepts and tools generally only available to programmers.

**@bluepjs** idea was inspired by the `Epic Games Unreal Engine Blueprint System <https://docs.unrealengine.com/4.27/en-US/ProgrammingAndScripting/Blueprints/>`_, which is full Object Oriented Programming (OOP) supported.

Current version of **@bluepjs** doesn't support OOP and currently is more Functional Programming.

.. note::

   Full OOP support will be added in next versions

Types
-----

**@bluepjs** is a pseudo-typed scripting language. **@bluepjs** **VM** running in Java Scriptwhich is dynamic-typed, so all "**Blueprint** code" runing in **VM** really is dynamic typed. Dynamic types in Java Script is double-sided question - on side it gives to developer fast and simple code development, and on other side it it may surprise developer on automatic types convering.

**Blueprint** concept is fixed typed and **@bluepjs** **IDE** fully implements this concept because it works great here:

  * different types have different colors what helps visually difference them
  * **IDE** block **Edge** connection when **User** try connect type-incompatible **Slots**.

**@bluepjs** has base set of types, but it can be extended same in programmatic way with **Modules**, same with types defined with **IDE**

Base Types
~~~~~~~~~~

``basic/boolean``

  Boolean type - yes/no, 1/0, true/false, on/off

``basic/number``

  Integer numbers - 0, -100, 44, ...

``basic/float``

  Float numbers - 1.23, -3.987, ...

``basic/string``

  Strings - "Hello world!", "Abc de fg", ...

``basic/datetime``

  Date and time.

``basic/date``

  Date only (!Not implemented currently)

``basic/time``

  Time only (!Not implemented currently)

``basic/object``

  Java Script object

Additional Types
~~~~~~~~~~~~~~~~

``basic/execute``

  This is special type to define **Execution Flow**

``basic/template``

  Special type for **Nodes** may work with different types (!Not implemented currently)

@bluepjs Types
~~~~~~~~~~~~~~

``bluep/enum``

  Base type for **Enums**

``bluep/struct``

  Base type for **Structs**

``bluep/function``

  Base type for **Functions** (!Not implemented currently)

``bluep/class``

  Base type for **Classes** (!Not implemented currently)

``bluep/object``

  Base type for **Blueprint Objects** (!Not implemented currently)

Nodes
-----

Inputs and Outputs
~~~~~~~~~~~~~~~~~~

Library Content
---------------

Enums
~~~~~

Structs
~~~~~~~

Functions
~~~~~~~~~

Classes
~~~~~~~

Object-oriented programming and **Classes** are not implemented currently.

Execution Flow in Depth
-----------------------

Call Node
~~~~~~~~~

Return Node
~~~~~~~~~~~
