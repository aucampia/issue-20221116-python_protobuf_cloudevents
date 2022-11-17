# ...

```bash
poetry install --no-root
make validate-fix validate-static
HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
```

```console
$ HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
========================================================================================================= test session starts =========================================================================================================
platform linux -- Python 3.10.8, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents, configfile: pyproject.toml, testpaths: tests
plugins: cov-4.0.0
collecting ...
--------------------------------------------------------------------------------------------------------- live log collection ---------------------------------------------------------------------------------------------------------
2022-11-17T10:11:58 3697856 140043171333952 020:INFO     root         test_conflicting_ns:10:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python310.zip', '/usr/lib64/python3.10', '/usr/lib64/python3.10/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.10/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.10/site-packages']
2022-11-17T10:11:58 3697856 140043171333952 020:INFO     root         test_conflicting_ns:13:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/proto', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/src', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python310.zip', '/usr/lib64/python3.10', '/usr/lib64/python3.10/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.10/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.10/site-packages']
collected 5 items

tests/test_conflicting_ns.py::test_something PASSED                                                                                                                                                                             [ 20%]
tests/test_conflicting_ns.py::test_conflict_a PASSED                                                                                                                                                                            [ 40%]
tests/test_conflicting_ns.py::test_mailbox FAILED                                                                                                                                                                               [ 60%]
tests/test_conflicting_ns.py::test_conflict_b FAILED                                                                                                                                                                            [ 80%]
tests/test_conflicting_ns.py::test_pb_okay PASSED                                                                                                                                                                               [100%]

============================================================================================================== FAILURES ===============================================================================================================
____________________________________________________________________________________________________________ test_mailbox _____________________________________________________________________________________________________________

    def test_mailbox() -> None:
        """
        this does not work because of the content of src/mailbox/__init__.py
        """
        import mailbox

>       assert callable(mailbox.Mailbox)  # type: ignore
E       AttributeError: module 'mailbox' has no attribute 'Mailbox'

tests/test_conflicting_ns.py:37: AttributeError
___________________________________________________________________________________________________________ test_conflict_b ___________________________________________________________________________________________________________

    def test_conflict_b() -> None:
        """
        this does not work because it generates modules inside io namespace

        ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package
        """
>       import example.v1.messages_pb2

tests/test_conflicting_ns.py:46:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

    # -*- coding: utf-8 -*-
    # Generated by the protocol buffer compiler.  DO NOT EDIT!
    # source: example/v1/messages.proto
    """Generated protocol buffer code."""
    from google.protobuf import descriptor as _descriptor
    from google.protobuf import descriptor_pool as _descriptor_pool
    from google.protobuf import message as _message
    from google.protobuf import reflection as _reflection
    from google.protobuf import symbol_database as _symbol_database
    # @@protoc_insertion_point(imports)

    _sym_db = _symbol_database.Default()


>   from io.cloudevents.v1 import cloudevents_pb2 as io_dot_cloudevents_dot_v1_dot_cloudevents__pb2
E   ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package

generated/proto/example/v1/messages_pb2.py:15: ModuleNotFoundError

---------- coverage: platform linux, python 3.10.8-final-0 -----------
Name                                          Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------
src/example/aucampia/nsconflict/__init__.py       4      0   100%
src/example/aucampia/nsconflict/_version.py       1      0   100%
src/mailbox/__init__.py                           2      0   100%
src/mailbox/sub/__init__.py                       2      0   100%
---------------------------------------------------------------------------
TOTAL                                             9      0   100%

======================================================================================================= short test summary info =======================================================================================================
FAILED tests/test_conflicting_ns.py::test_mailbox - AttributeError: module 'mailbox' has no attribute 'Mailbox'
FAILED tests/test_conflicting_ns.py::test_conflict_b - ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package
===================================================================================================== 2 failed, 3 passed in 0.09s =====================================================================================================
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
