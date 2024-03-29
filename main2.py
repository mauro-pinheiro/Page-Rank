from pagerank import *

L = np.array([[0,   1/2, 1/3, 0, 0,   0  , 0 ],
               [1/3, 0,   0,   0, 1/2, 0  , 0 ],
               [1/3, 1/2, 0,   1, 0,   1/3, 0 ],
               [1/3, 0,   1/3, 0, 1/2, 1/3, 0 ],
               [0,   0,   0,   0, 0,   0  , 0 ],
               [0,   0,   1/3, 0, 0,   0  , 0 ],
               [0,   0,   0,   0, 0,   1/3, 1 ]])

r = pageRank(L,.7,1e-4,1000)
print(r)
print(sum(r))