Tests for `src/usoar_edm`.

## Running tests

```
uv run pytest
```

With coverage:
```
uv run pytest --cov=usoar_edm
```

## Structure

Mirror the `src/` structure:
```
tests/
├── __init__.py
├── test_data.py      # Tests for src/usoar_edm/data.py
├── test_models.py    # Tests for src/usoar_edm/models.py
└── ...
```

## Writing tests

```python
from usoar_edm import data

def test_load_data():
    result = data.load("sample.csv")
    assert result is not None
```
