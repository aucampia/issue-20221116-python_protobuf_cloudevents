# ...

```bash
poetry install --no-root

make help
make validate-fix validate
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
