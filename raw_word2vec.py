import word2vec
from timeit import default_timer as timer

start = timer()
word2vec.word2vec('data-test.txt', 'vectors-model.bin', cbow=0, size=100, window=10, negative=5, hs=0, sample='1e-4', threads=8, iter_=20, min_count=1, verbose=True)
end = timer()
print('Model generated in %f seconds' % (end - start))
