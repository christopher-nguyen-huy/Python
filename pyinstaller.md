# Pyinstaller

Its an alternative to py2exe to build executables on windows.

[Manual](https://pythonhosted.org/PyInstaller/)  
[Site](https://github.com/pyinstaller/pyinstaller)
## Installing
### Dependencies
#### pywin32
- Go to [sourceforge](http://sourceforge.net/projects/pywin32/files/pywin32/)
- Download correct build for python and windows version
- Install

### Python 2
```
pip install pyinstaller
```

### Python 3
Must install from python3 branch
```
pip3 install https://github.com/pyinstaller/pyinstaller/archive/python3.zip
```

## Using

[Manual](https://pythonhosted.org/PyInstaller/#using-pyinstaller)

- Navigate to the script's location
- Run pyinstaller on the main script
```
pyinstaller myscript.py
```
- Temporary files are thrown into the `build` folder
- Output is in the `dist` folder

### Options
#### Onefile
Builds 1 exe for eazy distribution
```
-F, --onefile filename.exe
```
