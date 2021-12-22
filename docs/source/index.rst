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

**MAJOR**

  Currently is ``0`` until full OOP/template/import/export impementation and then it will be ``1.0.?`` version.

  Major version will be increased on huge scripting engine updates and there is no guarantee of back-compatibility.

  It may happen big refactoring before ``1.0`` publishing, if any back-compattibility will be loosed - updater will be provided.

**MINOR**

  Will be increased on each valuable update inside major roadmap. Resets to zero on major number incrementing.

  Minor updates will be developed with back compatibility with previous minor version.

**PATCH**

  Will be incremented on every update. Doesn't resets. Means nothing for back-compatibility.

.. note::

   I'm really sorry, but documentation is also under development (and not so active as engine)

   Please, check https://github.com/bluep-js/example project for demo.

Contents
--------

.. toctree::

   intro
   blueprint
   ide
   vm
