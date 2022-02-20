# directory-starter
- [directory-starter](#directory-starter)
  - [Overview](#overview)
  - [How to use it](#how-to-use-it)

## Overview
directory-starter is a little Tool to setup the [cookie cutter data science project structure](https://drivendata.github.io/cookiecutter-data-science/) within a few seconds. In this version it also creates basic packaging files (e.g. `MANIFEST.in`, `setup.cfg`).

The following structure is created when using the tool:
```
- data/ 
   - external/
   - interim/ 
   - processed/
   - raw/ 
- docs/
- output/
- references/
- reports/
   - figures/
- src/
- tests/
- .gitignore
- LICENSE
- main.py
- MANIFEST.in
- pyproject.toml
- README.md
- requirements.txt
- setup.cfg
- setup.py
```

## How to use it
The tool is provided by testpypi at the moment (see [here](https://test.pypi.org/project/directory-starter/)).

To install it run 
```bash
pip install -i https://test.pypi.org/simple/ directory-starter
```

Once the installation is finished, you can initialize the above described directory structure using:
```
python -m directory-starter
```

