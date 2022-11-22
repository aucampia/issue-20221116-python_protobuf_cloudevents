# ...

```bash
# Only install dependencies as we want to hack the python path
poetry install --no-root
# Check that everything is valid
make validate-fix validate-static
# Run the tests with sys.path hax.
HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
```

```console
$ HACK_SYS_PATH=1 poetry run pytest --log-cli-level=DEBUG
============================================================================ test session starts ============================================================================
platform linux -- Python 3.9.15, pytest-7.2.0, pluggy-1.0.0
rootdir: /home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents, configfile: pyproject.toml, testpaths: tests
plugins: cov-4.0.0
collecting ...
---------------------------------------------------------------------------- live log collection ----------------------------------------------------------------------------
2022-11-22T09:24:53 408971 140212516071232 020:INFO     root         test_conflicting_ns:17:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python39.zip', '/usr/lib64/python3.9', '/usr/lib64/python3.9/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.9/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.9/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/betterproto', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/protol', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/src']
2022-11-22T09:24:53 408971 140212516071232 020:INFO     root         test_conflicting_ns:22:<module> sys.path = ['/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/protol', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/betterproto', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/proto', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/src', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/tests', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/bin', '/usr/lib64/python39.zip', '/usr/lib64/python3.9', '/usr/lib64/python3.9/lib-dynload', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib64/python3.9/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/.venv/lib/python3.9/site-packages', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/betterproto', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/generated/protol', '/home/iwana/sw/d/github.com/aucampia/issue-20221116-python_protobuf_cloudevents/src']
collected 5 items

tests/test_conflicting_ns.py::test_sane PASSED                                                                                                                        [ 20%]
tests/test_conflicting_ns.py::test_io_conflict FAILED                                                                                                                 [ 40%]
tests/test_conflicting_ns.py::test_pb_okay PASSED                                                                                                                     [ 60%]
tests/test_conflicting_ns.py::test_bpb_okay
------------------------------------------------------------------------------- live log call -------------------------------------------------------------------------------
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:68:test_bpb_okay json = {'fieldA': '', 'fieldB': {'id': '', 'source': '', 'specVersion': '', 'type': '', 'attributes': {}, 'binaryData': '', 'textData': '', 'protoData': {'typeUrl': '', 'value': ''}}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:68:test_bpb_okay json = {'fieldA': '', 'fieldB': '0', 'someField': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:68:test_bpb_okay json = {'id': '', 'source': '', 'specVersion': '', 'type': '', 'attributes': {}, 'binaryData': '', 'textData': '', 'protoData': {'typeUrl': '', 'value': ''}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:72:test_bpb_okay json = {'field_a': '', 'field_b': {'id': '', 'source': '', 'spec_version': '', 'type': '', 'attributes': {}, 'binary_data': '', 'text_data': '', 'proto_data': {'type_url': '', 'value': ''}}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:72:test_bpb_okay json = {'field_a': '', 'field_b': '0', 'some_field': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:72:test_bpb_okay json = {'id': '', 'source': '', 'spec_version': '', 'type': '', 'attributes': {}, 'binary_data': '', 'text_data': '', 'proto_data': {'type_url': '', 'value': ''}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:76:test_bpb_okay json = {'field_a': '', 'field_b': {'id': '', 'source': '', 'spec_version': '', 'type': '', 'attributes': {}, 'binary_data': '', 'text_data': '', 'proto_data': {'type_url': '', 'value': ''}}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:76:test_bpb_okay json = {'field_a': '', 'field_b': '0', 'some_field': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:76:test_bpb_okay json = {'id': '', 'source': '', 'spec_version': '', 'type': '', 'attributes': {}, 'binary_data': '', 'text_data': '', 'proto_data': {'type_url': '', 'value': ''}}
PASSED                                                                                                                                                                [ 80%]
tests/test_conflicting_ns.py::test_pl_okay
------------------------------------------------------------------------------- live log call -------------------------------------------------------------------------------
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:96:test_pl_okay msg_dict = {'field_a': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:96:test_pl_okay msg_dict = {'field_a': '', 'field_b': '0', 'SOME_FIELD': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:96:test_pl_okay msg_dict = {'id': '', 'source': '', 'spec_version': '', 'type': '', 'attributes': {}}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:102:test_pl_okay msg_dict = {'fieldA': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:102:test_pl_okay msg_dict = {'fieldA': '', 'fieldB': '0', 'SOMEFIELD': ''}
2022-11-22T09:24:54 408971 140212516071232 020:INFO     root         test_conflicting_ns:102:test_pl_okay msg_dict = {'id': '', 'source': '', 'specVersion': '', 'type': '', 'attributes': {}}
PASSED                                                                                                                                                                [100%]

================================================================================= FAILURES ==================================================================================
_____________________________________________________________________________ test_io_conflict ______________________________________________________________________________

    def test_io_conflict() -> None:
        """
        this does not work because it generates modules inside io namespace

        ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package
        """
>       import example.v1.messages_pb2

tests/test_conflicting_ns.py:37:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

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

---------- coverage: platform linux, python 3.9.15-final-0 -----------
Name                                          Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------
src/example/aucampia/nsconflict/__init__.py       4      0   100%
src/example/aucampia/nsconflict/_version.py       1      0   100%
---------------------------------------------------------------------------
TOTAL                                             5      0   100%

========================================================================== short test summary info ==========================================================================
FAILED tests/test_conflicting_ns.py::test_io_conflict - ModuleNotFoundError: No module named 'io.cloudevents'; 'io' is not a package
======================================================================== 1 failed, 4 passed in 0.36s ========================================================================
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


## ...

```bash
poetry run python devscripts/protoc_fixer.py --prefix _qnrgwqoo generated/protorope/
```
