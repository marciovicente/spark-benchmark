from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec
from timeit import default_timer as timer

start = timer()
sc = SparkContext(appName='Word2Vec')
inp = sc.textFile("ofr2.txt").map(lambda row: row.split(" "))

word2vec = Word2Vec()
model = word2vec.fit(inp)
end = timer()
print('Model generated in %f seconds' % (end - start))

synonyms = model.findSynonyms('china', 40)


# for word, cosine_distance in synonyms:
#       print("{}: {}".format(word.encode('utf-8'), cosine_distance))
