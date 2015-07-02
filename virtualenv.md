## Create new virtualenv

```
virtualenv --no-site-packages -p C:\Unix\Python27\python.exe mysite
```
```
virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>
```
### Explanation:
- `--no-site-packages`: do not copy over packages from site-packages install
- `-p C:\Unix\Python27\python.exe`: location of the python version to use
- `mysite`: virtualenv directory

## Activating
### Windows
`Scripts\activate.bat`
### Linux
`source bin/activate`

## Deactivating virtualenv
### Windows
`Scripts\deactivate.bat`
### Linux
`source bin/deactivate`
