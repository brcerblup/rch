import numpy as np
import config as cfg


def prandom_nums(n, seed): #pseudosluchainye v diapazone [-1,1]
    prandomg = np.random.default_rng(seed)
    return prandomg.uniform(-1,1,size=n)

def almost_cancellation(n, seed): #pochti sokrashayushiesya
    rng = np.random.default_rng(seed)
    eps = rng.uniform(-cfg.volume_eps, cfg.volume_eps,size=n//2) 
    tmp_randoms = rng.uniform(0,cfg.volume_randoms, size=n//2)
    #tmp_randoms_neg = list(map(lambda x: -x, tmp_randoms))
    #result = list()
    #for i in range(n//2):
    #    result.append(tmp_randoms[i])
    #    result.append(tmp_randoms_neg[i]+eps[i])
    result = np.empty(n, dtype=np.float64)
    result[0::2] = tmp_randoms
    result[1::2] = -tmp_randoms + eps
    rng.shuffle(result)
    return result

def cancellation(n,seed): 
    rng = np.random.default_rng(seed)
    tmp = rng.uniform(0,cfg.volume_randoms, size=n//2)
    result = np.empty(n, dtype=np.float64)
    result [0::2] = -tmp
    result [1::2] = tmp
    rng.shuffle(result)
    return result           # sokrashayushiesya

def harmonic(n, seed):
    rng = np.random.default_rng(seed)
    l,m = rng.uniform(2,100, size=2)
    sequence = np.empty(n, dtype=np.float64)
    for k in range(n):
        sequence[k] = 1/(l+m*k)
    rng.shuffle(sequence)
    return sequence
    

def pizdec_raznye(n, seed): #chisla s silno otlichayusheisya exponentoi
    rng = np.random.default_rng(seed)
    exp = rng.integers(0, cfg.exp_volume, size=n)
    mantissaaaaaa = rng.uniform(1,2,size=n)
    result = mantissaaaaaa*(2**exp)
    return result

