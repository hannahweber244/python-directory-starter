# directory-starter

## What it is
directory-starter is a little Tool to setup the [cookie cutter data science project structure](https://drivendata.github.io/cookiecutter-data-science/) within a few seconds. In version 0.0.2 it also creates basic packaging files (e.g. `MANIFEST.in`, `setup.cfg`).

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
- requirements.txt
- README.md
```

## How it works
The tool is provided by testpypi at the moment (see [here](https://test.pypi.org/project/directory-starter/0.0.2/)).

To install it run 
```bash
pip install -i https://test.pypi.org/simple/ directory-starter==0.0.2
```

Once everything is setup you can initialize the above described directory structure using:
```
python -m directory-starter
```

