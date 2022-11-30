Welcome to @bluepjs documentation!
===================================

**@bluepjs** is a Java Script visual scripting engine library, inspired by Unreal Engine Blueprints system.

Blueprint scripting looks like this:

.. image:: ./_static/intro-blueprint-example.png
   :alt: Blueprint scripting example

**@bluepjs** may be integrated into projects required visual scripting of project entities behavior.

Version compatibility
---------------------

@bluepjs project is under active development, but it doesn't mean u can't use it.

Version numbers for @bluepjs are: **MAJOR.MINOR.PATCH**.

There is no guarantee of back-compatibility between versions now, sorry. Some functionality of new versions rebuilds some old temporary solutions and version update until ``1.0.x`` defenetly will require manual `Library` rebuild on some versions update.

**MAJOR**

  Currently is ``0`` until full OOP/template/import/export impementation and then it will be ``1.0.?`` version.

  Major version will be increased on huge scripting engine updates.

**MINOR**

  Will be increased on each valuable update inside major roadmap. Resets to zero on major number incrementing.

**PATCH**

  Will be incremented on every update. Doesn't resets. Means nothing for back-compatibility.

.. note::

   I'm really sorry, but documentation is also under development (and not so active as engine)

   Please, check https://github.com/bluep-js/example project for demo.

Changelog
---------

**0.3.4**

 * ``AbstractModule::metadata()`` for module dynamic metadata
 * ``AbstractModule::vm()``
 * ``AbstractActor::metadata()`` for actor dynamic metadata
 * ``AbstractNode::context()``
 * Node multiple slots
 * multiple slots for string/append, boolean/and, boolean/or
 * OOP support, node "cast to"
 * node "Switch .. case"
 * node number/plus
 * types basic/date; basic/time
 * ``async Vm::start()`` / ``async Vm::stop()``
 * ``Vm::runModuleEvent(info, inputs)`` for easy run simple events

**0.2.2**

  * Partial OOP support without correct classes inheritance.
  * ``Modules`` ``types``, ``enums`` and ``structs`` autosupport
  * ``Actors`` ``nodes`` updated to OOP style (from "node-per-actor" to "node-per-actor-type(class) with actor input" generation (require actors behavior rebuild in library!)
  * VM should be started to run. VM also can be stopped.
  * ``VM`` module with ``On VM Start`` event.
  * Modules API for start/stop
  * Templates support for IDE (type ``basic/template``)
  * bugfixes

**0.1.1**

  * IDE limited to use only ``Default`` library
  * buxfixes

Contents
--------

.. toctree::

   Intro <intro.rst>
   User's documentation <user.rst>
   Developer's guides <dev.rst>
