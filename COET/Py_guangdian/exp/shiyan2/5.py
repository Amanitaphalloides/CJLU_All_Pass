def sum_of_cubes(n):
    
    str_n = str(n)
    
    sum_cubes = 0
    
    for digit in str_n:
        
        cube = int(digit) ** 3
        
        sum_cubes += cube
    return sum_cubes

if __name__ == "__main__":
    
    num = int(input("请输入一个3位的正整数："))
    
    print("各位数字的立方之和是：", sum_of_cubes(num))
