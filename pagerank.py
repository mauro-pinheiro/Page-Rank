import numpy as np
import numpy.linalg as la
import math

def pageRank(linkMatrix, d, tol, nMax) :
    n = linkMatrix.shape[0]
    M = d * linkMatrix + ((1-d)/n) * np.ones([n, n])
    r = 100 * np.ones(n)/n
    lastR = r
    r = M @ r
    i = 0
    #np.set_printoptions(precision=int(abs(math.log10(tol))))
    if tol > 0 :
        np.set_printoptions(edgeitems = 3,
                            formatter = None,
                            infstr = 'inf',
                            linewidth = 100,
                            nanstr = 'nan',
                            precision=int(abs(math.log10(tol))),
                            suppress = True,
                            threshold = 1000)
    else :
        np.set_printoptions(precision = 4)
    
    while la.norm(lastR - r) > tol :
        print(lastR)
        lastR = r
        r = M @ r
        i += 1
        if i == nMax :
            break
    print(str(i) + " iterations to convergence.")
    return r