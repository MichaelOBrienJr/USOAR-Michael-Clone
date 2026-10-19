Project source code. Installed as an editable package via `pyproject.toml`.

## Structure

```
src/
└── usoar_edm/
    ├── __init__.py
    ├── data.py        # Data loading and processing
    ├── models.py      # Model definitions
    ├── utils.py       # Shared utilities
    └── ...
```

## Usage

In notebooks:
```python
from usoar_edm import data, models
```

In workflow scripts:
```python
from usoar_edm.utils import some_function
```

Move reusable code from notebooks here. Keep notebooks for exploration, keep `src/` for tested, reusable code.
