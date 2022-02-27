# directory-starter
- [directory-starter](#directory-starter)
  - [Overview](#overview)
  - [How to use it](#how-to-use-it)

## Overview
`directory-starter` enables you to start coding immediately, without wasting your time by creating project files and folders first.

In this version 4 types of directory structures can be initialized: `minimal`, `medium` and `large` (which refer directly to the structure proposed in the [Cookie Cutter Data Science Template](https://drivendata.github.io/cookiecutter-data-science/)) and `packaging`, which creates basic files to distribute your application as a python package. 

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

Once the installation is finished, you can initialize the above described directory structures using:
```
python -m directory-starter -mode=<STRUCTURETYPE> -mirror=<PATH-TO-YOUR-PROJECT>
```
By default the `minimal` mode is used.
