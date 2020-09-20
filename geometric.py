import math
def prob(n, p):
    return ((1 - p) ** (n - 1)) * p

def infoMeasure(n, p):
    return -math.log2(prob(n,p))

def sumProb(N, p):
    '''
    Tổng xác suất phân bố geometric xấp xỉ bằng 1
    Hàm prob(i,p) là xác xuất lần thứ i với p là xác suất của phép thử bernoulli 
    '''
    res = 0.0
    for i in range(1, N+1):
        res += prob(i, p)
    return res
def approxEntropy(N, p):
    '''
    Tính giá trị trung bình lượng tin của symbol từ 1 đến N của nguồn tin geometric
    p là xác suất của phép thử bernoulli 
    '''
    res = 0.0
    for i in range(1, N+1):
        res += prob(i, p) * infoMeasure(i, p)
    return res
