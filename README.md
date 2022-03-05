# directory-starter
- [directory-starter](#directory-starter)
  - [Overview](#overview)
  - [How to use it](#how-to-use-it)
  - [Functionality and scope](#functionality-and-scope)
    - [Structure types](#structure-types)
    - [File templates](#file-templates)
    - [Mirroring an existing project](#mirroring-an-existing-project)

## Overview
`directory-starter` enables you to start coding immediately, without wasting your time by creating project files and folders first.

In this version 4 types of directory structures can be initialized: `minimal`, `medium` and `large` (which refer directly to the structure proposed in the [Cookie Cutter Data Science Template](https://drivendata.github.io/cookiecutter-data-science/)) and `packaging`, which creates basic files to distribute your application as a python package. Some of the files come prefilled (e.g. `LICENSE`, `setup.cfg` & `.gitignore`) so all you need to do is include your project details. Additionally a mirroring functionality enables you to copy the structure of one of your existing projects. All you need is to pass the path of the old project when setting up your new project.

And no worries, if some of the files already exist, `directory-starter` won't overwrite what's already there.

## How to use it
The tool is provided by testpypi at the moment (see [here](https://test.pypi.org/project/directory-starter/)).

To install it run 
```bash
pip install -i https://test.pypi.org/simple/ directory-starter
```

Once the installation is finished, you can initialize the above described directory structures using:
```bash
python -m directory-starter -mode=<STRUCTURETYPE> -mirror=<PATH-TO-YOUR-PROJECT>
```
By default the `minimal` mode is used. If a mirroring project path is passed, the mode will be ignored. Simple initialization: 

```bash
python -m directory-starter
```

## Functionality and scope
In this section the functionality of the package is discussed in more detail:

### Structure types

`minimal`:

```
- data/ 
- notebooks/
- reports/
- src/
   - __init__.py
- .env
- .gitignore
- LICENSE
- main.py
- README.md
- requirements.txt
```

`medium`:
```
- data/ 
- docs/
- notebooks/
- references/
- reports/
- src/
   - __init__.py
- tests/
- .env
- .gitignore
- LICENSE
- main.py
- README.md
- requirements.txt
```

`large`:
```
- data/ 
   - external/
   - interim/ 
   - processed/
   - raw/ 
- docs/
- models/
- notebooks/
- output/
- references/
- reports/
   - figures/
- src/
   - data/
   - features/
   - models/
   - visualization/
- tests/
- .env
- .gitignore
- LICENSE
- main.py
- README.md
- requirements.txt
- setup.py
```

`packaging`:
```
- docs/
- src/
   -<PACKAGE-DIR>
      - __init__.py
      - __main__.py
- tests/
- .gitignore
- LICENSE
- MANIFEST.in
- pyproject.toml
- README.md
- requirements.txt
- setup.cfg
- setup.py
```
### File templates 
For the following files templates are provided, which results in the files not being initialized empty:
- `.gitignore`
- `README`
- `setup.cfg`
- `setup.py`
### Mirroring an existing project
At the moment only first and secondlevel files / directories are mirrored from the passed project. More importantly: Not every file will be copied, but only those on main project level. No contents will be copied from the files, but only from the `directory-starter` templates (if some are provided). 