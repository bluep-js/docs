IDE integration/Интеграция с IDE
================================

Installation/Установка
----------------------

.. code-block:: console

   npm install -s @bluepjs/vue3-ide

Usage/Применение
----------------

Добавьте модуль IDE в ваше приложение Vue

.. code-block:: javascript

   // main.js
   // ...
   import bluep from '@bluepjs/vue3-ide'
   // ...
   createApp(app)
     .use(bluep)
   // ...

Ваше приложение должно управлять "общением" с виртуальной машиной для получения возможностей ВМ.

.. code-block:: javascript

   const vmInfo = vm.ideData()

Интегрируйте редактор в страницу:

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

Options/Опции
~~~~~~~~~~~~~

Объект Options используется для настройки иконок редактора и стартовой страницы, например:

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


Options are/Варианты таковы:

 * `icons` - используется стиль "i class". Без иконок некоторые кнопки сейчас не видны (не имеют текста, будет исправлено в будущем)
 * `select` - объект, получаемый по событию `@select` для запуска редактора с открытым нужным элементом

Icons/Значки
~~~~~~~~~~~~

Значки по умолчанию предварительно настроены для font-awesome:

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

Features/Характеристики
~~~~~~~~~~~~~~~~~~~~~~~

Функции позволяют настраивать **IDE**

.. note::

   В стадии разработки!

   Не все функции реализованы. 

   Список и структура функций пока не стабильны.

Функции по умолчанию:

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

Dialogs/Диалоги
~~~~~~~~~~~~~~~

Для перезаписи стандартных диалогов браузера установите настройки диалогов:

.. code-block:: javascript

   const dialogsObject = {
     confirm: async (question) => { return Boolean },
     prompt: async (question) => { return String },
     alert: async (message) => { return }
   }

Events/События
~~~~~~~~~~~~~~

 * `save` - нажата кнопка "SAVE". Библиотека `$event` обновляется
 * `run` - нажата кнопка "RUN". $event содержит информацию о библиотеке и коды функций для запуска
 * `select` - срабатывает, когда какой-либо элемент выбран для редактирования
