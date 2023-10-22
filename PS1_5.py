#Question 5.1
def find_expression(target):
    digits = "123456789"
    solutions = []
    for i in range(6561): # 3 ** 8 = 6561
        expr = ""           # 用于存储当前的表达式
        for j in range(8):   # 9个数字之间有8个运算符
            if i % 3 == 0:   # 如果 i 除以 3 的余数为 0，则不需要添加
                op = ""
            elif i % 3 == 1: # 如果 i 除以 3 的余数为 1，则添加"+" 
                op = "+"  
            elif i % 3 == 2: # 如果 i 除以 3 的余数为 2，则添加"-" 
                op = "-"
            i //= 3
            expr += digits[j] + op  # 将数字和运算符添加到表达式中
        expr += digits[8]  # 最后再添加最后一个数字
        if eval(expr) == target:
            solutions.append(expr + " = " + str(target))  # 如果当前表达式的结果等于目标值，则将其添加到 solutions 列表中
    return solutions

#Question 5.2
import matplotlib.pyplot as plt

Total_solutions = []   
for i in range(1, 101):
    solutions = find_expression(i)
    count = len(solutions)
    Total_solutions.append(count)  # 将每个目标值的解的个数添加到 Total_solutions 中

plt.figure(figsize=(12, 6))  # 设置画布的尺寸
plt.plot(range(1, 101), Total_solutions, color='blue', linewidth=2, label='Number of Solutions')  # 绘制折线图
plt.xlabel("Target Value", fontsize=14)   # 设置x轴标签
plt.ylabel("Number of Solutions", fontsize=14)   # 设置y轴标签
plt.title("Number of Solutions for Each Target Value", fontsize=16)   # 设置标题
plt.xticks(range(0, 101, 2), fontsize=12, rotation=90)   # 设置x轴刻度
plt.yticks(range(0, max(Total_solutions) + 1, 1), fontsize=12)  # 设置y轴刻度
plt.grid(True)   # 添加网格
plt.legend(fontsize=12)  # 添加图例
plt.tight_layout()   # 设置紧凑布局
plt.show()  # 显示图形