from pagerank import *

L = np.array([[0,0,0,1],
              [1,0,0,0],
              [0,1,0,0],
              [0,0,1,0]])

r = pageRank(L,1,1e-4,1000)
print(r)
print(sum(r))