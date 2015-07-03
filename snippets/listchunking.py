# Splits array into blocks of 100
chunks=[data[x:x+100] for x in xrange(0, len(data), 100)]