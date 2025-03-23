from buff_gen import *
def gol_buff_print(buff,h,w):
    for i in range(h):
        for j in range(w):
            #print(buff)
            print(buff[i][j],sep="",end="")
            #print("#" if buff[i][j]==1 else ".",sep="",end="")
        print()

if __name__=="__main__":
    pass
    #h=350
    #w=1900
    #gol_buff_print(gol_gen_buff(w,h),h,w)
