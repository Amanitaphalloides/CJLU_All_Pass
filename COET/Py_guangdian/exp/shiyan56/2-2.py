psls = [75, 75, 75, 65, 85, 95, 85, 75, 75, 75, 85, 75, 75, 65, 75]  # 平时成绩
qmls = [68, 63, 70, 51, 78, 83, 75, 66, 70, 73, 85, 67, 78, 60, 66]  # 期末成绩

if len(psls) != len(qmls):
    print("平时成绩和期末成绩列表长度不一致")
else:

    zps = []
    for i in range(len(psls)):
        zp = psls[i] * 0.2 + qmls[i] * 0.8
        zps.append(zp)

    for i in range(len(zps)):
        print(f"学生 {i + 1} 的总成绩是: {zps[i]:.2f}")
