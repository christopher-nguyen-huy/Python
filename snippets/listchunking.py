# Splits array into blocks of 100
chunks=[data[x:x+100] for x in xrange(0, len(data), 100)]


# Dechunking
r = [[1,2,3],[4,5,6], [7], [8,9]]
s = [item for sublist in r for item in sublist]

# Is equivalent to this!
for sublist in r:
	for item in sublist:
		s.append(item)