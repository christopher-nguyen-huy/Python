## Setup
- Download latest python setups for 2.x and 3.x
- Install in C:\\Unix\\
- Make sure to check add to path for preferred version (2.x or 3.x)
- Check to see if it works
```
python
```
- Add the C:\\Unix\\Python\\Scripts folder to the path

### Installer notes
The windows installer of python comes with pip nowadays. If it didn't, you'll need to get pip via setup tools.

#### Install setup tools
- Go to https://pypi.python.org/pypi/setuptools
- Find the **windows (simplified)** section
- Download the ez_setup.py file
- Run it in python

```
wget https://bootstrap.pypa.io/ez_setup.py -O - | python
```

#### Install pip from easy_install
```
easy_install pip
```

## Install setuptools
If the installer included pip, you only need to install setuptools
```
pip install setuptools
```

## Unofficial binaries for packages
[Here!](http://www.lfd.uci.edu/~gohlke/pythonlibs/)

## Visual Studio to compile extension modules
Depending on the python version you are using, you need the correct version of visual studio on your machine. Each python version wants a different c++ compiler.

The version of visual studio needed can be viewed in the source code of python in `PCbuild\\readme.txt`

| Python Version | VC++ Version | VS Year |
| :-: | :-: | :-: |
| 2.3 |  | 6 |
| 2.4 | 7.1 | 2003 |
| 2.5 | 7.1 | 2003 |
| 2.6 | 9.0 | 2008 |
| 2.7 | 9.0 | 2008 |
| 3.0 | 9.0 | 2008 |
| 3.1 | 9.0 | 2008 |
| 3.2 | 9.0 | 2008 |
| 3.3 | 10.0 | 2010 |
| 3.4 | 10.0 | 2010 |

| VC++ Version | _MSC_VER | Visual Studio Year | vsXXXcomntool # |
| :-: | :-: | :-: | :-: |
| 1.0 | 800 |   |   |
| 2.0 | 900 |   |   |
| 2.x | 900 |   |   |
| 4.0 | 1000 |   |   |
| 5.0 | 1100 |   |   |
| 6.0 | 1200 |   |   |
| 7.0 | 1300 | .NET 2002 |   |
| 7.1 | 1310 | .NET 2003 | 70 |
| 8.0 | 1400 | 2005 | 80 |
| 9.0 | 1500 | 2008 | 90 |
| 10.0 | 1600 | 2010 | 100 |
| 11.0 | 1700 | 2012 | 110 |
| 12.0 | 1800 | 2013 | 120 |
| 14.0 | tbd | 2015 | tbd |

### Do not do any of this!
Errors will occur, like when trying to compile lxml for python-docx

- Visual Studio 2010 (VS10): `SET VS90COMNTOOLS=%VS100COMNTOOLS%`
- Visual Studio 2012 (VS11): `SET VS90COMNTOOLS=%VS110COMNTOOLS%`
- Visual Studio 2013 (VS12): `SET VS90COMNTOOLS=%VS120COMNTOOLS%`

### Compilers
- [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-us/download/details.aspx?id=44266)
- Visual Studio 2010 Express
	- [Visual Studio 2010 SP1](http://go.microsoft.com/fwlink/?LinkId=210710)

### Redistributable packages
- [Visual C++ 2008 Redistributable (x86)](http://www.microsoft.com/en-us/download/details.aspx?displaylang=en&id=29)
- [Visual C++ 2008 Redistributable (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=15336)
- [Visual C++ 2010 Redistributable (x86)](http://www.microsoft.com/en-us/download/details.aspx?id=5555)
- [Visual C++ 2010 Redistributable (x64)](http://www.microsoft.com/en-us/download/details.aspx?id=14632)
- [Visual C++ 2010 Redistributable (x86) SP1](http://www.microsoft.com/en-us/download/details.aspx?id=8328)
- [Visual C++ 2010 Redistributable (x64) SP1](http://www.microsoft.com/en-us/download/details.aspx?id=13523)

## Install from cmdline
https://docs.python.org/3.5/using/windows.html
```python
python-3.5.1.exe /passive InstallAllUsers=1 TargetDir=C:\Unix\Python35 PrependPath=1 Shortcuts=0 Include_doc=0 Include_debug=1
```

## How to compile c Extensions
https://blog.ionelmc.ro/2014/12/21/compiling-python-extensions-on-windows/
Either install VS 2015/2017 Community Edition or get the MS [C++ Build tooks](http://landinghub.visualstudio.com/visual-cpp-build-tools)
