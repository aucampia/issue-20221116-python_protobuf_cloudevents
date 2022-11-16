# ...

```bash
poetry install --no-root
HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
```

```console
$ HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
============================================================================ test session starts ============================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents, configfile: pyproject.toml, testpaths: tests
plugins: cov-4.0.0
collecting ...
---------------------------------------------------------------------------- live log collection ----------------------------------------------------------------------------
2022-11-16T15:06:54 3645347 140223964989248 020:INFO     root         test_conflicting_ns:11:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python310.zip', '/usr/lib64/python3.10', '/usr/lib64/python3.10/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.10/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.10/site-packages']
2022-11-16T15:06:54 3645347 140223964989248 020:INFO     root         test_conflicting_ns:13:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/src', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python310.zip', '/usr/lib64/python3.10', '/usr/lib64/python3.10/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.10/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.10/site-packages']
collected 2 items

tests/test_conflicting_ns.py::test_something
------------------------------------------------------------------------------- live log call -------------------------------------------------------------------------------
2022-11-16T15:06:54 3645347 140223964989248 020:INFO     root         test_conflicting_ns:17:test_something entry: ...
PASSED                                                                                                                                                                [ 50%]
tests/test_conflicting_ns.py::test_conflict_a
------------------------------------------------------------------------------- live log call -------------------------------------------------------------------------------
2022-11-16T15:06:54 3645347 140223964989248 020:INFO     root         test_conflicting_ns:24:test_conflict_a entry: ...
FAILED                                                                                                                                                                [100%]

================================================================================= FAILURES ==================================================================================
______________________________________________________________________________ test_conflict_a ______________________________________________________________________________

    def test_conflict_a() -> None:
        logging.info("entry: ...")

>       import argparse.sub
E       ModuleNotFoundError: No module named 'argparse.sub'; 'argparse' is not a package

tests/test_conflicting_ns.py:26: ModuleNotFoundError
----------------------------------------------------------------------------- Captured log call -----------------------------------------------------------------------------
2022-11-16T15:06:54 3645347 140223964989248 020:INFO     root         test_conflicting_ns:24:test_conflict_a entry: ...

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                                          Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------
src/argparse/__init__.py                          2      2     0%   3-7
src/argparse/sub/__init__.py                      2      2     0%   1-2
src/example/aucampia/nsconflict/__init__.py       4      0   100%
src/example/aucampia/nsconflict/_version.py       1      0   100%
---------------------------------------------------------------------------
TOTAL                                             9      4    56%

========================================================================== short test summary info ==========================================================================
FAILED tests/test_conflicting_ns.py::test_conflict_a - ModuleNotFoundError: No module named 'argparse.sub'; 'argparse' is not a package
======================================================================== 1 failed, 1 passed in 0.04s ========================================================================
```

## Using docker devtools

```bash
make -C devtools -B
docker compose build

docker compose run --rm python-devtools make help
docker compose run --rm python-devtools make validate-fix validate
```

## Updating from template base

```bash
pipx run --spec=cruft cruft update
```

## other commands ...

```bash
make help
make validate-fix validate
HACK_SYS_PATH=1 make test pytest_args='--log-cli-level=DEBUG'
```
