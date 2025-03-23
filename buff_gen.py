import random as rand
import numpy as np
frac=0.8
def gol_gen_buff(h,w):
	buff=[]
	for _ in range(h):
		for _ in range(w):
			buff.append(1 if rand.random()>frac else 0)
	return np.array(buff,dtype='int32')
