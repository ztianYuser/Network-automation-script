
money  = 5000000 #全局变量
name  = input ("--欢迎进入自助银行系统--\n请输入你的名字进行查询:")
'''查询功能'''
def  query(show_header):#设置布尔值进行判断
    if  show_header: #如果为真就输出这个
        print ("------查询余额------")
    print (f"{name}你的余额剩下{money}" )
'''存款模块'''
def saving(num):
    global money  #把money在函数内部定义为全局变量
    money+= num
    print("--------存款--------")
    print(f"{name}你好， 你存款{num}成功！！")
    query(False)
'''取款功能'''
def  get(num):
    global money
    money-= num
    print("-----取款-----")
    print(f"{name}你好， 你取款{num}元成功！！")
    query(False) #掉用布尔值的第二个选项
'''菜单功能'''
def  main ():
    print ("-------- 主菜单---------")
    print  (f"{name}你好 欢迎你来到银行")
    print ("查询余额\t[请输入1]") #使用\t进行对齐
    print ("存款\t\t[请输入2]")
    print ("取款\t\t[请输入3]")
    print ("离开银行\t[请输入4]")
    return  input("请输入你的选择：")

while  True:  #进行循环
    keyboard_input=main()  #调用菜单模块用input进行输入！！
    if keyboard_input == "1": # 如果等于1时
        query(True)  #调用查询模块的布尔为True的结果

        continue  #结束当前进程进行下一次语句
    elif   keyboard_input == "2":#如果等于2时
        num=int(input("你要存款多少钱？？请你输入："))#调用存款函数
        saving(num)
        continue
    elif  keyboard_input == "3":
        num =int(input("你要取出多少钱？？？ 请输入："))##调用取款函数
        get(num)
        continue
    
    else:
        keyboard_input == "4"
        print("欢迎下次再来！！")
        break
    
