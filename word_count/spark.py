from pyspark import SparkContext
from timeit import default_timer as timer
from operator import add

sc = SparkContext(appName="PythonWordCount")
lines = sc.textFile('ofr_double.txt')
start = timer()
counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
output = counts.collect()
words_count =0
# words_count = lines.flatMap(lambda x: x.split(' ')).count()
end = timer()
print '*'*100
print('%s words in %f seconds' % (words_count, (end - start)))
print '*'*100
sc.stop()

