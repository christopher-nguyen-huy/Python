import time
try:
	from cStringIO import StringIO
except:
	from io import StringIO

# 10x more, aka 10000000, += will take 200 seconds, be carefull!
qty = 1000000

start = time.time()
li = []
for j in range(0,qty):
	li.append(str(j))
# print(''.join(li))
somestring = ''.join(li)
end = time.time()
elapsed = end - start
print('List join time: %s' % elapsed)

somestring = ''
buf = StringIO()
start = time.time()
for j in range(0,qty):
	buf.write(str(j)) 
# print(somestring)
somestring = buf.getvalue()
end = time.time()
elapsed = end - start
print('String IO time: %s' % elapsed)


### Super slow!!! ###
somestring = ''
start = time.time()
for j in range(0,qty):
	somestring += str(j)
# print(somestring)
end = time.time()
elapsed = end - start
print('+= time: %s' % elapsed)