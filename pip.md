# Pip

## Installing
Should come with python on windows

## Upgrading
```
pip install -U pip
```
or
```
pip install --upgrade pip
```

## Installing stuff
### Basic
```
pip install SomePackage
```
### Specific version
```
pip install SomePackage==1.0.4
```
### Minimum version
```
pip install 'SomePackage>=1.0.4'
```
### From version control
```
pip install git+https://github.com/multiplay/mysql-connector-python
```
- Also works with other VCSs

### From Wheels
```
pip install SomePackage-1.0-py2.py3-none-any.whl
```
### From requirements file
```
pip install -r requirements.txt
```

## Uninstalling
```
pip uninstall SomePackage
```
## Listing
```
pip list
```
### List oudated stuff
```
pip list --outdated
```
## Upgrade stuff
```
pip install --upgrade SomePackage
```
## Searching
```
pip search "query"
```
## Freezing
- Output installed packages in requirements text format.

```
pip freeze > requirements.txt
```
## Package info
```
pip show SomePackage
```
