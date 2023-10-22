def Least_moves(x):
    count = 0       # 用于存储最少的步数
    original_input = x   # 最终x的值会发生改变，因此新定义一个变量用于存储原始输入的值
    if x == 1:
     print("The smallest number of moves to get 1 is 0.")  # 如果输入的值为1，则不需要任何操作，步数为0
     return None
    if x < 1 or x > 100 or isinstance(x, int) == False:
     print("Please enter an integer between 1 and 100.")   # 如果输入的值不在1-100之间或者不是整数，则报错
     return None
    else:
     while x > 1 and x <= 100:  
        if x % 2 == 0:
            x = x / 2     # 如果x是偶数，则除以2
        else:
            x = x - 1    # 如果x是奇数，则减1
        count += 1       # 每进行一次操作，步数加1
    print("The smallest number of moves to get "+ str(original_input) + " is " + str(count) +".")


Least_moves(2)
Least_moves(5)