import math
def giaithua(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res
def ckn(n, k):
    return giaithua(n)/(giaithua(k) * giaithua(n - k))
def prob(n, p, N):
    return ckn(N, n) * ((1 - p) ** (N - 1)) * p
def sumProb(N, p):
    '''
    Tổng xác suất phân bố geometric xấp xỉ bằng 1
    Hàm prob(i,p) là xác xuất lần thứ i với p là xác suất của phép thử bernoulli 
    '''
    res = 0.0
    for i in range(1, N+1):
        res += prob(i, p, N)
    return res

def infoMeasure(n, p, N):
    return -math.log2(prob(n,p,N))
def approxEntropy(N, p):
    '''
    Tính giá trị trung bình lượng tin của symbol từ 1 đến N của nguồn tin binomial
    p là xác suất của phép thử bernoulli 
    '''
    res = 0.0
    for i in range(0, N+1):
        res += prob(i, p, N) * infoMeasure(i, p, N)
    return res
