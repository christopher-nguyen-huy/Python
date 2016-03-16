# Regex in Python
## Import
```python
import re
```

## Compile
```python
regexobj1 = re.compile(r'.+\d+')
```

## Use it
### Checking if string contains a part that matches regex

```python
somestring = 'abcde12345'
match = regexobj1.search(somestring)
# if no results found, match = None
if match:
	match.group()
	match.group(1)	# First group
	match.group(0)	# Entire matched text
	match.groups()	# tuple of all groups
```
Use regexobj1.match()

## Extract
Extract all the matches in bulk
```python
ma = regexobj1.findall(somestring)
```
- ma  is a list of matches
- if there are groups (\1\2), ma is a list of tuples
```python
m = re.search("Your number is <b>(\d+)</b>",
      "xxx Your number is <b>123</b>  fdjsk")
if m:
    print m.groups()[0]
```

## Replace
```python
newstr = regexobj1.sub()
newstr, count = regexobj1.sub() # gives you number of replacements
```

## Other
### Named groups

```python
p = re.compile(r'(?P<name> [^}]* )'')
```

### Look ahead, behind
