import math
def giaithua(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
def ckn(n, k):
    return giaithua(n)/(giaithua(k) * giaithua(n - k))
def prob(n, p, r):
    return ckn(n + r - 1, n) * (p ** r) * ((1 - p) ** n)
def sumProb(N, p, r):
    res = 0.0
    for i in range(1, N+1):
        res += prob(i, p, r)
    return res

def infoMeasure(n, p, r):
    return -math.log2(prob(n,p,r))
def approxEntropy(N, p, r):
    '''
    Tính giá trị trung bình lượng tin của symbol từ 1 đến N của nguồn tin negbinomial
    p là xác suất của phép thử bernoulli 
    '''
    res = 0.0
    for i in range(r, N+1):
        res += prob(i, p, r) * infoMeasure(i, p, r)
    return -res
