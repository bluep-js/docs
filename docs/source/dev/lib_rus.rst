@bluepjs schemas/схемы
======================

**@bluepjs** использует различные схемы для работы.

Для любых схем ``arrays/массивы`` **RARE USED/РЕДКО ИСПОЛЬЗУЮТСЯ** только в особых случаях.

Вместо массивов **@bluepjs** использует *preindexed objects/преиндексированные объекты* по полю ``code`` (или ``id``).

Examples/Примеры:

**Not correct/Неправильно**:

.. code-block:: javascript

   const info = [{
     code: 'x'
   }, {
     code: 'y'
   }]

**Correct/Правильно**:

.. code-block:: javascript

   const info = {
     x: { code: 'x' },
     y: { code: 'y' }
   }

Этот тип структуры позволяет легко получить доступ к нужному элементу по его ``code/коду``, получить только коды по ``Object.keys``, и получить только значения по ``Object.values``.

Library content schemas/Схемы содержимого библиотеки
----------------------------------------------------

Variable/Переменная
~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     type: 'basic/string', // [required] type code
     value: undefined // default or current value
     list: ['opt1', 'opt2'], // array of possible values
     access: 'public', // [for class properties only] 'public'/'protected'/'private'
   }

Описание **Variable** можно найти:

  * Function inputs/Входы функции
  * Function outputs/Выходы функции
  * Function variable/Переменная функции
  * Struct field/Поле структуры
  * Class property/Свойство класса

Enum/Перечисление
~~~~~~~~~~~~~~~~~

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

Описание **Enum** можно найти:

  * Libraries enums/Перечисления библиотек
  * Modules enums/Перечисления модулей

Struct/Структура
~~~~~~~~~~~~~~~~

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


Описание **Struct** можно найти:

  * Libraries structs/Структуры библиотек
  * Modules structs/Структуры модулей

Functions/Функции
~~~~~~~~~~~~~~~~~

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


Описание **Function** можно найти:

  * Libraries functions/Функции библиотек
  * Libraries classes/Классы библиотек

Classes/Классы
~~~~~~~~~~~~~~

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


Описание **Class** можно найти:

  * Libraries classes/Классы библиотек
  * Modules classes/Классы модулей
  * Actors metadata/Метаданные акторов

Library/Библиотека
~~~~~~~~~~~~~~~~~~

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

Описание **Library** можно найти:

  * Libraries/Библиотеки

Node Description/Описание узла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Описание **Node** можно найти:

  * Functions graph nodes/Узлы графа функций

Edge Description/Описание связки
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

Описание **Edge** можно найти:

  * Functions graph edges
  * Function graph node slots connections

Slot/Слот
~~~~~~~~~

.. code-block:: javascript

   const info = {
     // same as variable, plus:
     template: 'templateCode', // [required for type === 'basic/template']
     multiple: 'multipleCode', // [required to make slot "multiple"]
     connections: null || { // null or "ondexed object" of slot connections
       edgeId: { ...EdgeDescription }
     }
   }

Описание **Slots** похоже на описание **Variable**, с дополнительным полем ``multiple`` и может быть найдено в:

  * Node inputs description/Описание входов узла
  * Node outputs description/Описание выходов узла

Metadata schemas/Схемы метаданных
---------------------------------

Объект метаданных возвращается методом ``static metadata()`` различных классов - ``Modules``, ``Actors`` и ``Nodes``.

Для ``Modules`` и ``Actors`` существует также нестатический метод ``metadata()``, который может быть использован, когда **App** запрашивает динамические метаданные.

.. note::

   Используйте динамические метаданные осторожно.

Module/Модуль
~~~~~~~~~~~~~

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     name: 'Name', // [required] user-readable name
     enums: {}, // "indexed object" of module enums
     structs: {}, // "indexed object" of module structs
     classes: {}, // "indexed object" of module classes
     events: {}, // "indexed object" of module events
   }

Actor/Актор
~~~~~~~~~~~

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

Вы можете думать о метаданных **Actor** как о **class** только с публичными методами/свойствами.

Node/Узел
~~~~~~~~~

То же самое, что и **Node description**, но без полей ``data`` и ``id`` и с немодифицированным полем ``code``.

Event/Событие
~~~~~~~~~~~~~

Метаданные **Event** можно найти в событиях **Module** и **Actor**.

.. code-block:: javascript

   const info = {
     code: 'uniquecode', // [required] machine-readable code
     event: 'uniquecode', // [required] code to subscribe with "obj.on(event, () => {})"
     name: 'Name', // [required] user-readable name
     outputs: { // "indexed object" of event outputs fields
       fieldCode: { ...VariableDescription }
     },
   }

Method/Метод
~~~~~~~~~~~~

Метаданные **Method** можно найти в описании методов **Actor**, и они аналогичны описанию **Node**:

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
