#Question 2.1
import random

rows = 5
cols = 10
M1 = []
for i in range(rows): # 生成 5 行
    row = []
    for j in range(cols):  # 生成 10 列
        row.append(random.randint(0, 50)) # 生成 0-50 之间的随机数
    M1.append(row) # 将生成的一行添加到 M1 矩阵中
print(M1)


rows = 10
cols = 5
M2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(random.randint(0, 50))
    M2.append(row)
print(M2)

#Question 2.2
def Matrix_multip(M1, M2):
    result = [] # 创建一个结果矩阵
    rows1, cols1 = len(M1), len(M1[0]) # 获取矩阵 M1 的行数和列数
    rows2, cols2 = len(M2), len(M2[0]) # 获取矩阵 M2 的行数和列数
   
    if cols1 != rows2:
        print("Error: M1 and M2 cannot be multiplied. Please check the dimensions of M1 and M2.") # 首先检查矩阵 M1 和矩阵 M2 是否可以相乘
        return None
    
    else:
     for i in range(rows1):   # 计算结果矩阵中第 i 行
        row = []
        for j in range(cols2):  # 计算结果矩阵中第 i 行第 j 列的元素
            element = 0        # 先将其初始化为0
            for k in range(cols1):  
                element += M1[i][k] * M2[k][j]  # 计算矩阵 M1 中第 i 行和矩阵 M2 中第 j 列对应元素的乘积之和
            row.append(element)   
        result.append(row)
    return result
print(Matrix_multip(M1, M2))

