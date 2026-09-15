# {py:mod}`Todolist.test.test_todo_routes`

```{py:module} Todolist.test.test_todo_routes
```

```{autodoc2-docstring} Todolist.test.test_todo_routes
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`test_deleting_a_todo <Todolist.test.test_todo_routes.test_deleting_a_todo>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_deleting_a_todo
    :summary:
    ```
* - {py:obj}`test_todo_creation <Todolist.test.test_todo_routes.test_todo_creation>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_creation
    :summary:
    ```
* - {py:obj}`test_todo_retrieval <Todolist.test.test_todo_routes.test_todo_retrieval>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_retrieval
    :summary:
    ```
* - {py:obj}`test_todo_retrieval_rejects_a_post <Todolist.test.test_todo_routes.test_todo_retrieval_rejects_a_post>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_retrieval_rejects_a_post
    :summary:
    ```
* - {py:obj}`test_update_route_missing_a_todo_id <Todolist.test.test_todo_routes.test_update_route_missing_a_todo_id>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_update_route_missing_a_todo_id
    :summary:
    ```
* - {py:obj}`test_update_route_receives_a_todo_id <Todolist.test.test_todo_routes.test_update_route_receives_a_todo_id>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_update_route_receives_a_todo_id
    :summary:
    ```
* - {py:obj}`test_updating_a_todo <Todolist.test.test_todo_routes.test_updating_a_todo>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_updating_a_todo
    :summary:
    ```
* - {py:obj}`test_updating_todo_allows_patch_requests <Todolist.test.test_todo_routes.test_updating_todo_allows_patch_requests>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.test_updating_todo_allows_patch_requests
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fake <Todolist.test.test_todo_routes.fake>`
  - ```{autodoc2-docstring} Todolist.test.test_todo_routes.fake
    :summary:
    ```
````

### API

````{py:data} fake
:canonical: Todolist.test.test_todo_routes.fake
:value: >
   'Faker(...)'

```{autodoc2-docstring} Todolist.test.test_todo_routes.fake
```

````

````{py:function} test_deleting_a_todo(test_app: flask.testing.FlaskClient, stored_todo: Todolist.Backend.models.todo.Todo) -> None
:canonical: Todolist.test.test_todo_routes.test_deleting_a_todo

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_deleting_a_todo
```
````

````{py:function} test_todo_creation(test_app: flask.testing.FlaskClient, todo_data) -> None
:canonical: Todolist.test.test_todo_routes.test_todo_creation

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_creation
```
````

````{py:function} test_todo_retrieval(test_app) -> None
:canonical: Todolist.test.test_todo_routes.test_todo_retrieval

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_retrieval
```
````

````{py:function} test_todo_retrieval_rejects_a_post(test_app: flask.testing.FlaskClient) -> None
:canonical: Todolist.test.test_todo_routes.test_todo_retrieval_rejects_a_post

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_todo_retrieval_rejects_a_post
```
````

````{py:function} test_update_route_missing_a_todo_id(test_app: flask.testing.FlaskClient, todo_data: Todolist.Backend.models.todo.Todo) -> None
:canonical: Todolist.test.test_todo_routes.test_update_route_missing_a_todo_id

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_update_route_missing_a_todo_id
```
````

````{py:function} test_update_route_receives_a_todo_id(test_app: flask.testing.FlaskClient, todo_data: Todolist.Backend.models.todo.Todo) -> None
:canonical: Todolist.test.test_todo_routes.test_update_route_receives_a_todo_id

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_update_route_receives_a_todo_id
```
````

````{py:function} test_updating_a_todo(test_app: flask.testing.FlaskClient, todo_data: Todolist.Backend.models.todo.Todo) -> None
:canonical: Todolist.test.test_todo_routes.test_updating_a_todo

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_updating_a_todo
```
````

````{py:function} test_updating_todo_allows_patch_requests(test_app: flask.testing.FlaskClient, todo_data) -> None
:canonical: Todolist.test.test_todo_routes.test_updating_todo_allows_patch_requests

```{autodoc2-docstring} Todolist.test.test_todo_routes.test_updating_todo_allows_patch_requests
```
````
