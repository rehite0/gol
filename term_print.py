from buff_gen import *
term={"h":350,"w":1900}
def gol_buff_print(buff):
	for i in range(term["h"]):
		for j in range(term["w"]):
			print("#" if buff[i][j]==1 else ".",sep="",end="")
		print()

if __name__=="__main__":
	gol_buff_print(gol_gen_buff(term["w"],term["h"]))

