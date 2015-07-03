### Stringbuffer Method ###

from cStringIO import StringIO
# python3:  from io import StringIO

buf = StringIO()

buf.write('foo')
buf.write('foo')
buf.write('foo')

buf.getvalue()
# 'foofoofoo'

### List Method ###

l = []
l.append('foo')
l.append('bar')
l.append('baz')

s = ''.join(l)