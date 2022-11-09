import random

if __name__ == '__main__':
    while True:
        computer=random.randint(1,3)
        print("比赛开始!")
        print("请选择：")
        print("1-石头\n"
              "2-剪刀\n"
              "3-布\n"
              "输入0退出")
        player=int(input())
        if(player==0):
            exit(0)
        print("电脑的选择是:{}".format(computer))
        if player-computer==1:
            print("很遗憾，你输了")
        elif computer-player==1:
            print("恭喜你，你赢了")
        elif player==computer:
            print("额，你们做出相同的选择，再来一局吧")
        elif player-computer==2:
            print("恭喜你，你赢了")
        elif computer-player==2:
            print("很遗憾，你输了")
        print()