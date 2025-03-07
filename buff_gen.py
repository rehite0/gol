import random as rand
frac=0.8
def gol_gen_buff(x,y):
	buff=[]
	for i in range(y):
		subbuff=[]
		for j in range(x):
			subbuff.append(True if rand.random()>frac else False)
		buff.append(subbuff)
	return buff
