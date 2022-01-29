IDE integration
===============

Installation
------------

.. code-block:: console

   npm install -s @bluepjs/vue3-ide

Ussage
------

Add IDE module to your Vue app

.. code-block:: javascript

   // main.js
   // ...
   import bluep from '@bluepjs/vue3-ide'
   // ...
   createApp(app)
     .use(bluep)
   // ...

Your application should manage "communication" with Virtual Machine to get VM possibilities.

.. code-block:: javascript

   const vmInfo = vm.ideData()

Integrate Editor into page:

.. code-block::

   <BluepJsEditor
     :height="'100%'"
     :types="vmInfo.types"
     :nodes="vmInfo.nodes"
     :modules="vmInfo.modules"
     :actors="vmInfo.actors"
     :libraries="vmInfo.libraries"
     :options="editorOptions"
     @save="onSave"
     @run="onRun"
     @select="onSelect"
   />

Options
~~~~~~~

Options object used to configure editor icons and starting page, for example:

.. code-block:: javascript

   computed: {
     editorOptions () {
       return {
         icons: { ...iconsObject },
         select: { ...selectObject },
         features: { ...featuresObject },
         dialogs: { ...dialogsObject }
       }
     }
   }


Options are:

 * `icons` - used "i class" style. Without icons some buttons right now are not visible (has no text, will be fixed in future)
 * `select` - object recieved on `@select` event to start editor with required element open

Icons
~~~~~

Default icons are preconfigured for font-awesome:

.. code-block:: javascript

   const defaultIcons = {
     enum: 'fas fa-list-ol',
     struct: 'fab fa-delicious',
     function: 'fas fa-scroll',
     class: 'fas fa-file-code',
     library: 'fas fa-book',
     event: 'fas fa-bell',
     chevronRight: 'fas fa-chevron-right',
     chevronDown: 'fas fa-chevron-down',
     view: 'far fa-eye',
     add: 'fas fa-plus',
     remove: 'fas fa-trash',
     edit: 'fas fa-pencil-alt',
     save: 'fas fa-save',
     run: 'fas fa-play',
     close: 'fas fa-times',
     fw: 'fa-fw'
   }

Features
~~~~~~~~

Features allows tune **IDE**

.. note::

   Under development!

   Not all features are implemented. 

   List and structure of features is not stable yet.

Default features are:

.. code-block:: javascript

   const defaultFeatures = {
     save: true,  // save button enabled
     run: true,   // run button enabled
     panels: {    // [not fully implemented]
       librarySelector: true, // library selector panel enabled
       libraryContent: true,  // library content panel enabled
       variablesBar: true,    // variables bar (function options) enabled
       variablePanel: true    // variable panel enabled
     },
     create: {    // [not implemented]
       libraries: false,      // allow clreate libraries
       classes: true,         // allow create classes
       functions: true,       // allow create functions
       events: true,          // allow create events
       structs: true,         // allow create structs
       enums: true,           // allow create enums
       consts: true           // allow create consts [consts are not implemented]
     },
     limit: {     // [not implemented]
       nodes: [],             // allowed nodes regexps
       types: []              // allowed types regexps
     }
   }

Dialogs
~~~~~~~

To overwrite standart browser dialogs set dialogs settings:

.. code-block:: javascript

   const dialogsObject = {
     confirm: async (question) => { return Boolean },
     prompt: async (question) => { return String },
     alert: async (message) => { return }
   }

Events
~~~~~~

 * `save` - "SAVE" button clicked. `$event` is updated library
 * `run` - "RUN" buttn clicked. $event contains information about library and function codes to run
 * `select` - fires when some element is selected to edit
