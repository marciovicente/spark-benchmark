import sys

from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.linalg import Vectors
from pyspark import SparkContext

from timeit import default_timer as timer

sc = SparkContext(appName="PythonNaiveBayes")

def parse(line):
    parsed_line = line.split(',')
    _class = parsed_line[0]
    values = parsed_line[1]
    words = Vectors.dense([float(x) for x in parsed_line[1].split(' ')])
    return LabeledPoint(_class, words)

start = timer()
try:
    filename = sys.argv[1]
    print '*'*200
    print filename
    dataset = sc.textFile(filename).map(parse)
except :
    print 'Missing input file'
    raise

training_ratio = float(2)/float(3)
testing_ratio = float(1)/float(3)
training, test = dataset.randomSplit([training_ratio, testing_ratio], seed=0)

model = NaiveBayes.train(training, 1.0)

end = timer()
print('Model generated in %f seconds' % (end - start))
