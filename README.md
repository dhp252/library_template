A template to create a library with some supportive functions

List of supportive functions:
- import_submodules (in `dhp/lib_utils.py`)
- walk_path (in `dhp/lib_utils.py`)
- ensure_license (in `dhp/lib_utils.py`)
- parse_requirements (in `dhp/lib_utils.py`)
- find / ff (in `dhp/__init__.py`)

***

## FOR USER
### Distribute
create wheel: `python setup.py bdist_wheel`

### Install wheel
`python -m pip install --upgrade path/to/wheel_file`

### Directly install
`python setup.py install`

***

## FOR DEVELOPER:
NOTICE: many package names are "dhp", replace with your desired name.

replace `__<variable_name>__` in `dhp/__init__.py` to your desired library information

### Add library to python path without installing
`python setup.py develop` or `pip install --editable .`


