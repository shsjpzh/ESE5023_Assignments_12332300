def Pascal_triangle(k):
    if k == 1:       
        return [1]     #第一行只有一个元素1
    else:
        current_line = [1]        #每行的第一个元素为1
        previous_line = Pascal_triangle(k - 1)       #调用递归函数，获取上一行的值
        for i in range(len(previous_line) - 1):      #实际每行需要计算的元素为行数减2（除去了首尾的1），也就是前一行的长度减1
            current_line.append(previous_line[i] + previous_line[i + 1])  #计算每行的元素值
        current_line += [1]       #每行的最后一个元素为1
        return current_line

# 打印第 100 行和第 200 行的值
print(Pascal_triangle(100))
print(Pascal_triangle(200))