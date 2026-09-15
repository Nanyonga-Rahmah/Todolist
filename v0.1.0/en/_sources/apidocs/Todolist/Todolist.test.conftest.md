# {py:mod}`Todolist.test.conftest`

```{py:module} Todolist.test.conftest
```

```{autodoc2-docstring} Todolist.test.conftest
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`setup <Todolist.test.conftest.setup>`
  - ```{autodoc2-docstring} Todolist.test.conftest.setup
    :summary:
    ```
* - {py:obj}`stored_todo <Todolist.test.conftest.stored_todo>`
  - ```{autodoc2-docstring} Todolist.test.conftest.stored_todo
    :summary:
    ```
* - {py:obj}`test_app <Todolist.test.conftest.test_app>`
  - ```{autodoc2-docstring} Todolist.test.conftest.test_app
    :summary:
    ```
* - {py:obj}`todo_data <Todolist.test.conftest.todo_data>`
  - ```{autodoc2-docstring} Todolist.test.conftest.todo_data
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fake <Todolist.test.conftest.fake>`
  - ```{autodoc2-docstring} Todolist.test.conftest.fake
    :summary:
    ```
````

### API

````{py:data} fake
:canonical: Todolist.test.conftest.fake
:value: >
   'Faker(...)'

```{autodoc2-docstring} Todolist.test.conftest.fake
```

````

````{py:function} setup() -> collections.abc.Generator
:canonical: Todolist.test.conftest.setup

```{autodoc2-docstring} Todolist.test.conftest.setup
```
````

````{py:function} stored_todo(setup) -> Todolist.Backend.models.todo.Todo
:canonical: Todolist.test.conftest.stored_todo

```{autodoc2-docstring} Todolist.test.conftest.stored_todo
```
````

````{py:function} test_app(setup) -> flask.testing.FlaskClient
:canonical: Todolist.test.conftest.test_app

```{autodoc2-docstring} Todolist.test.conftest.test_app
```
````

````{py:function} todo_data() -> dict
:canonical: Todolist.test.conftest.todo_data

```{autodoc2-docstring} Todolist.test.conftest.todo_data
```
````
