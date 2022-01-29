@bluepjs schemas
================

**@bluepjs** uses different schemas to work.

For any schemas ``arrays`` are **RARE USED** only at special cases.

Instead of arrays **@bluepjs** uses *preindexed objects* by ``code`` field (or ``id`` field).

Examples:

**Not correct**:

.. code-block:: javascript

   const info = [{
     code: 'x'
   }, {
     code: 'y'
   }]

**Correct**:

.. code-block:: javascript

   const info = {
     x: { code: 'x' },
     y: { code: 'y' }
   }

This type of structure allows easy access to required element by it's ``code``, gettings only codes by ``Object.keys`` and getting only values by ``Object.values``.

Library content schemas
-----------------------

Variable
~~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'basic/string', // [required] type code
     value: undefined // default or current value
     list: ['opt1', 'opt2'], // array of possible values
     access: 'public', // [for class properties only] 'public'/'protected'/'private'
   }

**Variable** description can be found at:

  * Function inputs
  * Function outputs
  * Function variable
  * Struct field
  * Class property

Enum
~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'enum', // [required] should be 'enum' for enums
     library: 'libraryCode', // [auto] library where enum is located
     module: 'moduleCode', // [auto] module where enum is located
     values: {  // enum dictionary
       key: 'Value',
       key2: 'Value 2',
     }
   }

**Enum** description can be found at:

  * Libraries enums
  * Modules enums

Struct
~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'struct', // [required] should be 'struct' for structs
     library: 'libraryCode', // [auto] library where struct is located
     module: 'moduleCode', // [auto] module where struct is located
     schema: {  // struct fields
       fieldCode1: { ...VariableDescription },
       fieldCode2: { ...VariableDescription }
     }
   }


**Struct** description can be found at:

  * Libraries structs
  * Modules structs

Functions
~~~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'function', [required] one of 'function'/'method'/'constructor'
     library: 'libraryCode', // [required] library where function or class is located
     class: 'classCode', // [required for type === 'method' || type === 'constructor'] class code
     event: { // [required for event functions]
       code: 'eventCode', // [auto] from event code
       module: 'moduleCode', // [auto] for module event
       actor: 'actorId', // [auto] for actors events
       config: {}, // [auto] for module events constructed by event metadata
       info: { ... }, // [auto] event metadata for IDE
     },
     context: {  // context fields description
       inputs: { //function inputs
         fieldCode1: { ...VariableDescription },
         fieldCode2: { ...VariableDescription }
       },
       outputs: { //function outputs
         fieldCode1: { ...VariableDescription },
         fieldCode2: { ...VariableDescription }
       },
       variables: { //function variables
         fieldCode1: { ...VariableDescription },
         fieldCode2: { ...VariableDescription }
       },
     },
     graph: { // blueprint graph
       nodes: { // "indexed object" of nodes by nodeId
         nodeId: { ...NodeInfo },
         nodeId2: { ...NodeInfo },
       },
       edges: { // "indexed object" of edges by edgeId
         edgeId: { ...EdgeInfo },
         edgeId2: { ...EdgeInfo },
       },
     },
     layout: { // blueprint elements coords and "visual" data
       field: {
         top: Number, // field y position (px)
         left: Number, // field x position (px)
         width: Number, // field width (px)
         height: Number, // field height (px)
       },
       zoom: {
         min: 0.5, // [default] currently predefined
         max: 2, // [default] currently predefined
         step: 0.1, // [default] currently predefined
         current: Float // current value
       },
       parts: { // "indexed object" by partId (nodeId/edgeId)
         ...
         nodeId: {
           x: Number, // node x position (px)
           y: Number, // node y position (px)
         },
         ...
         edgeId: {
           from: {
             x: Number, // edge from x position (px)
             y: Number, // edge from y position (px)
           },
           to: {
             x: Number, // edge to x position (px)
             y: Number, // edge to y position (px)
           }
         }
       }
     },
     entry: 'nodeId'
   }


**Function** description can be found at:

  * Libraries functions
  * Libraries classes

Classes
~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'class', // [required] should be 'class' for classes
     library: 'libraryCode', // [auto] library where class is located
     module: 'moduleCode', // [auto] module where class is located
     schema: {  // struct fields
       fieldCode1: { ...VariableDescription },
       fieldCode2: { ...VariableDescription }
     },
     methods: { // class methods
       code1: { ...FunctionDescription },
       code2: { ...FunctionDescription },
     },
     extends: { // "indexed object" of class inheritance parents
       fullPath: { // full path is `library/{lib}/{class}` or `module/{mod}/{class}`
         library: 'code', // for library class
         module: 'code',  // for module class
         code: 'classCode'
       }
     }
   }


**Class** description can be found at:

  * Libraries classes
  * Modules classes
  * Actors metadata

Library
~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     enums: {}, // "indexed object" of library enums
     structs: {}, // "indexed object" of library structs
     functions: {}, // "indexed object" of library functions
     classes: {}, // "indexed object" of library classes
     options: {}, // additional library options [not implements yet!]
   }

**Library** description can be found at:

  * Libraries

Node Description
~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const info = {
     id: `${code}_${creationTimestamp}`, // [required] unique node id
     code: '${node.metadata.code}[/${someUniques}]', // [required] machine-readable code based on (startsWith) node metadata code
     name: 'Name', // [required] user-readable name
     type: 'execute' || 'modifier' || 'getter', // node type
     addable: Boolean, // [auto] node can be added (from node metadata)
     deletable: Boolean, // [auto] node can be deleted (from node metadata),
     inputs: { // indexed object of node inputs slots
       slotCode: { ...SlotDescription }
     },
     outputs: { // indexed object of node outputs slots
       slotCode: { ...SlotDescription }
     },
     templates: { // indexed object of templates for slots type === 'basic/template'
       templateCode: {  // one or both of.  allow priority is higher
         allow: [],   // array of "regexp" (with * symbol for '.*') for allow types
         disallow: [] // array of "regexp" (with * symbol for '.*') for disallow types
       }
     },
     multiples: {
       multipleCode: { // description of slot multiples
         min: 1, [default]
         current: 1, [default]
         max: 1, [default]
       }
     },
     data: {} // additional data for node execution defined by IDE
   }

**Node** description can be found at:

  * Functions graph nodes

Edge Description
~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const info = {
     id: `edge_${creationTimestamp}`, // [required] unique edge id
     type: 'basic/boolean', // type of data
     from: {
       node: 'fromNodeId',
       slot: 'outputNodeSlotCode'
     },
     to: {
       node: 'toNodeId',
       slot: 'inputNodeSlotCode'
     }
   }

**Edge** description can be found at:

  * Functions graph edges
  * Function graph node slots connections

Slot
~~~~

.. code-block:: javascript

   const info = {
     // same as variable, plus:
     template: 'templateCode', // [required for type === 'basic/template']
     multiple: 'multipleCode', // [required to make slot "multiple"]
     connections: null || { // null or "ondexed object" of slot connections
       edgeId: { ...EdgeDescription }
     }
   }

**Slots** description is similar to **Variable** description, with additional field ``multiple`` and can be found at:

  * Node inputs description
  * Node outputs description

Metadata schemas
----------------

Metadata object returns by ``static metadata()`` method of different classes - ``Modules``, ``Actors`` and ``Nodes``.

For ``Modules`` and ``Actors`` there is also non-static method ``metadata()`` which can be used when **App** requres dynamic metadata.

.. note::

   Use dynamic metadata carefully.

Module
~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     enums: {}, // "indexed object" of module enums
     structs: {}, // "indexed object" of module structs
     classes: {}, // "indexed object" of module classes
     events: {}, // "indexed object" of module events
   }

Actor
~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     events: {
       eventCode: { ...EventDescription }
     }, // "indexed object" of actor events
     methods: {
       methodCode: { ...MethodDescription }
     }, // "indexed object" of actor methods
     state: {
       fieldCode: { ...VariableDescription }
     }, // "indexed object" of actor properties
   }

You can think about **Actor** metadata as about **class** with public methods/properties only.

Node
~~~~

Same as **Node description** but without ``data`` and ``id`` fields and unmodified ``code`` field.

Event
~~~~~

**Event** metadata can be found at **Module** and **Actor** events

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     event: 'uniquecode', // [required] code to subscribe with "obj.on(event, () => {})"
     name: 'Name', // [required] user-readable name
     outputs: { // "indexed object" of event outputs fields
       fieldCode: { ...VariableDescription }
     },
   }

Method
~~~~~~

**Method** metadata can be found at **Actor** methods description, and it's similar to **Node** description:

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     inputs: { // "indexed object" of method inputs fields
       fieldCode: { ...VariableDescription }
     },
     outputs: { // "indexed object" of method outputs fields
       fieldCode: { ...VariableDescription }
     },
   }
