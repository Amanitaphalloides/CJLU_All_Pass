current_weight_earth = float(input("请输入你当前的体重（kg）："))

moon_weight_ratio = 0.165

annual_growth = 0.5

print("\n未来10年体重状况：")
print("{:<10} {:<15} {:<15}".format("年份", "地球体重(kg)", "月球体重(kg)"))
for year in range(1, 11):
    future_weight_earth = current_weight_earth + year * annual_growth
    future_weight_moon = future_weight_earth * moon_weight_ratio
    print("{:<10} {:<15.2f} {:<15.2f}".format(year, future_weight_earth, future_weight_moon))
