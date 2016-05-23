from timeit import default_timer as timer
from operator import add

file=open('ofr_double.txt', 'r+')
start = timer()
lines = file.read().split()
_dict = {}
for l in lines:
    try:
        _dict[l] = _dict[l] + 1
    except:
        _dict[l] = 1
end = timer()

# counts = map(lambda x: _dict[x] = (_dict[x]+1 if _dict[x] else 1), lines).reduceByKey(add)
# for d in _dict:
#     print("%s: %i" % (d.encode('utf-8'), _dict[d]))

print('%f seconds' % (end - start))

