
import    random
from unicodedata import name
dog = {"藏獒":200,"牧羊犬":150,"中华田园犬":120,"哈士奇":100,"泰迪":50}  #狗血量
monkey = {'公猴':300,"母猴":240,"老猴":160,"小猴":100,"幼猴":120} #猴血量
dog1 = {"藏獒":100,"牧羊犬":80,"中华田园犬":60,"哈士奇":40,"泰迪":20}  #dog的攻击
monkey1 = {'公猴':70,"母猴":50,"老猴":30,"小猴":10,"幼猴":20} #monkey攻击 
while  True:
    print(f"狗的战力表{dog1}\n血量表单{dog}")
    print( )
    print(f"猴子的战力表{monkey1}\n血量表单{monkey}")
    user= input("---种族大战开始---\n请输入你要与狗对战的猴子:")
    for a  in  dog.keys():
        b =  random.sample (dog.keys(),1)
        c=b[0]                               #进行字典的随机
    print(f"你选择{user}出战它的血量{monkey[user]}战斗力{monkey1[user]}")
    print(f"狗出战的是{b}血量为{dog[c]}战斗力为{dog1[c]}")
    
    while True:
        print(monkey.__contains__(user))   #输入的字符串如果不是猴子的就出返回flase
        if  monkey[user]  > 0 < dog[c]:
            monkey[user]  -= dog1[c]
            dog[c] -= monkey1[user]
            print(f"发起进攻{b}")
            print(f"{user}剩下{monkey[user]}血量")
            print(f"{b}剩下血量{dog[c]}战斗力为{dog1[c]}")
        elif monkey[user] <= 0:
            del monkey[user]
            print(f"{user}在大战中没了")
            break 
        elif dog[c] <=0:
            del dog[c]
            print(f"{b}在大战中没了")
            break
        else:
            print("大战结束")
