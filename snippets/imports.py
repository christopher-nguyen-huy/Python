import X
'''
Use this.
Imports the module X, and creates a reference to that module in the current namespace. Or in other words, after you’ve run this statement, you can use X.name to refer to things defined in module X.
'''
from X import *
'''
Do not use this. Namespace pollution
After you’ve run this statement, you can simply use a plain name to refer to things defined in module X. But X itself is not defined, so X.name doesn’t work.
'''
from X import a, b, c
'''
You can now use a and b and c in your program. But not X.a or X.d.
'''

import X as s
'''
This will allow you to basically rename the module to whatever you want. People generally do this to shorten the name of the module. Matplotlib.pyplot is often imported as plt and numpy is often imported as np, for example.
'''
from statistics import mean as m
'''
Same as above but with the functions/objects
'''

from statistics import mean as m, median as d

print(m(example_list))
print(d(example_list))
