print("求根计算器<只算整数版>")
while True:
    a = int(input("请输入a："))#输入二次项系数
    b = int(input("请输入b："))#输入一次项系数
    c = int(input("请输入c："))#输入常数项系数
    d = b**2-4*a*c#计算有无实数根
    if a==0:
        print("a不能等于零")
    elif d<0:
        print("判别式为负，没有实数根")
    else:
        print("结果为：",(-b + d**0.5) / (2*a))#二元一次方程的求根公式
        print("结果为：",(-b - d**0.5) / (2*a))
    if input("继续吗，回车继续计算/退出q:") == "q":
        break
