import numpy as np
import pygame as pg
#import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from buff_gen import *
from term_print import *

h=10
w=80
bufflen=None
pid=None
buffid1=None
buffid2=None

pg.init()
pg.display.set_mode((800,400),pg.OPENGL)

with open("test.cs.glsl",'r') as f:
    src=f.readlines()
pid=compileProgram(compileShader(src,GL_COMPUTE_SHADER))
glUseProgram(pid)

buffid1,buffid2=glGenBuffers(2)
glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid1)
data=gol_gen_buff(w,h)
bufflen=data.nbytes
glBufferData(GL_SHADER_STORAGE_BUFFER, bufflen, data, GL_DYNAMIC_COPY)
glBindBufferBase(GL_SHADER_STORAGE_BUFFER,0,buffid1)

glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid2)
glBufferData(GL_SHADER_STORAGE_BUFFER, bufflen, data, GL_DYNAMIC_COPY)
glBindBufferBase(GL_SHADER_STORAGE_BUFFER,1,buffid2)
glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)


gol_buff_print(data.reshape((h,w)),h,w)
print()
print()
glUseProgram(pid)
glDispatchCompute(w//8+1,h//8+1,1)
data=glGetBufferSubData(GL_SHADER_STORAGE_BUFFER,0,bufflen)
data.dtype='int32'
gol_buff_print(data.reshape((h,w)),h,w)

pg.quit()
glDeleteProgram(pid)
#glDeleteBuffers(1,(vbo,))
