def tax(salary_pre, social_accumulation_insurance, deduction):
    """根据税前月薪，社保比例，公积金比例，专项扣除
    算出2019每月应交税额"""
    temp = salary_pre - social_accumulation_insurance - 5000 - deduction
    month1 = []
    count = 0
# 计算新税
    for i in range(1, 13):
        k = int(temp * i)
        if k <= 0:
            rate_tax = 0
            part_tax = 0
        elif 0 < k <= 36000:
            rate_tax = 0.03
            part_tax = 0
        elif 36000 < k <= 144000:
            rate_tax = 0.1
            part_tax = 2520
        elif 144000 < k <= 300000:
            rate_tax = 0.2
            part_tax = 16920
        elif 300000 < k <= 420000:
            rate_tax = 0.25
            part_tax = 31920
        elif 420000 < k <= 660000:
            rate_tax = 0.3
            part_tax = 52920
        elif 660000 < k <= 960000:
            rate_tax = 0.35
            part_tax = 85920
        elif k > 960000:
            rate_tax = 0.45
            part_tax = 181920

        month1.append(temp * i * rate_tax - part_tax - count)
        count += month1[i-1]

    year = round(sum(month1), 2)
    month = [round(i, 2) for i in month1]
# 

    tax_pre = round(tax_pre, 2)
    year_pre = round(tax_pre * 12, 2)

    print("2019各月交税：")
    print(month)
    print('2019全年交税：' + str(year))



#填入税前月薪，社保比例，公积金比例，专项扣除
tax(39000,5650 , 1500)
