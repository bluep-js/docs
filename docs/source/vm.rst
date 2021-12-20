Virtual Machine
===============

.. _intro:

Intro
-----

@bluepjs Virtual Machine (VM) executes Blueprints

.. _installation:

Installation
------------

To use VM, first install it using npm:

.. code-block:: console

   npm install @bluepjs/vm


Then import VM class, create VM object and load libraries

.. code-block:: javascript

   import { Vm } from '@bluepjs/vm'

   const vm = new Vm()

   // loading libraries
   const libraries = loadLibraries()
   vm.updateLibraries(libraries)
