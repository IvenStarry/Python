if int(input("输入您的身高：")) > 120:
    print("身高超出限制，不可免费")
    print("但是，如果vip级别大于3，可以免费")
    if int(input("请输入您的vip级别：")) > 3:
        print("恭喜您 ，vip级别达标，可以免费")
    else:
        print("sorry 需要买票~")
else:
    print("欢迎小朋友，免费游玩~")

age = 20
year = 3
level = 3
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜您，年龄和入职时间都达标，可以领取礼物")
        elif level > 3:
            print(" 恭喜您，年龄和级别达标，可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但入职时间和级别都不达标")
    else:
        print("不好意思，年龄太大了，不可以领取礼物")
else:
    print("不好意思，小朋友不可以领取")