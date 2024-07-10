# # import numpy as np
# import sys
# input=sys.stdin.readline
# R=1000000007
# t=int(input())
# x_f=[[2,1],[1,1]]
# x_s=[[1,1],[1,0]]
# x_l=[[0,0],[0,0]]

# # for i in range(t):
# #     if i==t-1:
# #         print(x_n[1][0])
# #     x_n = x_n @ x_1
# #     x_n=x_n % R

# def matmul(A,B,C):
#     l=C
#     c=0
#     for i in range(2):
#         for j in range(2):
#             for k in range(2):
#                 C[i][j]+=A[i][k]*B[k][j]
#                 c+=1
#     return matmul(A,B,C)

# print(matmul(x_f, x_s, x_l))




########################################################################
########################################################################

R=1000000007
t=int(input())

class Matrix:
    @classmethod
    def zeroes(cls, rows: int, cols: int) -> 'Matrix':
        return cls([[0] * cols for _ in range(rows)])

    def __init__(self, data):
        self.rows = len(data)
        self.cols = len(data[0])
        self.data = data

    def __matmul__(self, other) -> 'Matrix':
        """Python 3.5에 추가된 행렬 곱셈 연산자(@) 오버로딩"""
        if self.cols != other.rows:
            raise ValueError("Matrix inner dimensions must agree")
        result = Matrix.zeroes(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
                    result.data[i][j]%=R
        return result

    def __getitem__(self, key):
        """행렬 인덱싱 연산자([]) 오버로딩"""
        return self.data[key]
    
def power(Matrix, t):
    if t==1: return Matrix
    elif t%2==0:
        result=power(Matrix, t//2)
        return result@result
    else:
        result=power(Matrix, t//2)
        return result@result@Matrix
    
if __name__ == '__main__':
    F_1 = Matrix([[1, 1], [1, 0]])
    if t==0: print(0)
    elif t==1: print(1)
    else:
        F_n=power(F_1,t)
        print(F_n[0][1]%R)