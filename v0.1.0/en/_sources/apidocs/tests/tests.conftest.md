# {py:mod}`tests.conftest`

```{py:module} tests.conftest
```

```{autodoc2-docstring} tests.conftest
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`pytest_addoption <tests.conftest.pytest_addoption>`
  - ```{autodoc2-docstring} tests.conftest.pytest_addoption
    :summary:
    ```
* - {py:obj}`pytest_configure <tests.conftest.pytest_configure>`
  - ```{autodoc2-docstring} tests.conftest.pytest_configure
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`options <tests.conftest.options>`
  - ```{autodoc2-docstring} tests.conftest.options
    :summary:
    ```
````

### API

````{py:data} options
:canonical: tests.conftest.options
:type: typing.List[typing.Dict[str, typing.Any]]
:value: >
   None

```{autodoc2-docstring} tests.conftest.options
```

````

````{py:function} pytest_addoption(parser: pytest.Parser, pluginmanager: pytest.PytestPluginManager)
:canonical: tests.conftest.pytest_addoption

```{autodoc2-docstring} tests.conftest.pytest_addoption
```
````

````{py:function} pytest_configure(config: pytest.Config)
:canonical: tests.conftest.pytest_configure

```{autodoc2-docstring} tests.conftest.pytest_configure
```
````
