weight=float(input("请输入您的体重（kg）："))
height=float(input("请输入您的身高（m）："))
bmi=weight/(height*height)
if bmi<18.5:
    print("您的BMI指数为："+str(bmi))
    print("您的体重过轻，该多吃吃哟！")
if bmi>=18.5 and bmi<24.9:
    print("您的BMI指数为："+str(bmi))
    print("您的体重正常，请继续保持哟！")
if bmi>=24.9 and bmi<29.9:
    print("您的BMI指数为：" + str(bmi))
    print("您的体重偏胖，是时候跑起来了！")
if bmi>=29.9:
    print("您的BMI指数为：" + str(bmi))
    print("您的体重过重，跑的不能停！")