from buff_gen import *
from os import system

chars=["\u2588"         #█
       ,"\u25a0"        #■
       ,"#"
       ]
def init_altscr():
    system('tput smcup')
    system('tput civis')
    system('tput setaf 2')
    system('tput setab 0')
def del_altscr():
    system('tput rmcup')
    system('tput cnorm')
    system('tput sgr0')
def gol_buff_print(buff,h,w):
    t=open("t.temp","w+")
    for i in range(h):
        for j in range(w):
            print(chars[1] if buff[i][j]==1 else " ",sep="",end="",file=t)
        print(file=t)
    t.close()
    system("tput cup 0 0 && cat t.temp")

if __name__=="__main__":
    h=350
    w=1900
    gol_buff_print(gol_gen_buff(w,h),h,w)
