import sys

from timeit import default_timer as timer

from pyspark import SparkContext
from pyspark.mllib.clustering import KMeans

sc = SparkContext(appName="KMeans")
dataset = None

start = timer()

try:
    dataset = sc.textFile(sys.argv[1]).map(lambda line: line.split(" "))
except :
    print 'Missing input file'
    raise

k = int(sys.argv[2])
model = KMeans.train(dataset, k)
print("Final centers: " + str(model.clusterCenters))
print("Total Cost: " + str(model.computeCost(dataset)))

end = timer()
print('Model generated in %f seconds' % (end - start))

sc.stop()
