MoneyStr = input("输入需要换算的带单位的金额：")

while MoneyStr[-1] not in ['&','*']:
    if MoneyStr[-1] in ['$']:
        RMB = (eval(MoneyStr[0:-1])*6)
        print("对应的人民币金额为：{:.2f}￥".format(RMB))
    if MoneyStr[-1] in ['￥20']:
        DOLLAR = (eval(MoneyStr[0:-1])/6)
        print("对应的美元金额为：{:.2f}$".format(DOLLAR))
    MoneyStr = input("输入需要换算的带单位的金额：")