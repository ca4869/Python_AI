user_weight = float(input("请输入您的体重(kg):"))
user_height = float(input("请输入您的身高(m):"))
user_bmi = user_weight/user_height ** 2
print("您的BMI值为:" + str(user_bmi))
# 偏瘦: user_bmi <= 18.5
# 正常: 18.5 < user_bmi <= 25
# 偏胖: 25 < user_bmi <= 30
# 肥胖: user_bmi > 30

if user_bmi <= 18.5:
    print("次BMI值属于偏瘦范围")
elif 18.5 <= user_bmi < 25:
    print("次BMI值属于正常范围")
elif 25 <= user_bmi < 30:
    print("次BMI值属于偏胖范围")
else:
    print("次BMI值属于肥胖范围")