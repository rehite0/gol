import numpy as np
import pygame as pg
#import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from buff_gen import *
from term_print import *
from time import sleep

h=59
w=220
bufflen=None
pid=None
buffid1=None
buffid2=None

pg.init()
pg.display.set_mode((8,4),pg.OPENGL)

with open("gol.cs.glsl",'r') as f:
    src=f.readlines()
pid=compileProgram(compileShader(src,GL_COMPUTE_SHADER))
glUseProgram(pid)

buffid1,buffid2=glGenBuffers(2)
glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid1)
data=gol_gen_buff(w,h)
bufflen=data.nbytes
glBufferData(GL_SHADER_STORAGE_BUFFER, bufflen, data, GL_DYNAMIC_COPY)
glBindBufferBase(GL_SHADER_STORAGE_BUFFER,0,buffid1)    #input

glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid2)
glBufferData(GL_SHADER_STORAGE_BUFFER, bufflen, data, GL_DYNAMIC_COPY)
glBindBufferBase(GL_SHADER_STORAGE_BUFFER,1,buffid2)    #output

u=glGetUniformLocation(pid,"dim")
glUniform2ui(u,w,h)
glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

gol_buff_print(data.reshape((h,w)),h,w)
frame=0
while(1):   
    print()
    print()
    glUseProgram(pid)
    glDispatchCompute(w//8+1,h//8+1,1)
    data=glGetBufferSubData(GL_SHADER_STORAGE_BUFFER,0,bufflen)
    data.dtype='int32'
    gol_buff_print(data.reshape((h,w)),h,w)
    if frame%2==0:
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER,0,buffid2)    #input
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER,1,buffid1)    #output
        glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid1)
    else:
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER,0,buffid1)    #input
        glBindBufferBase(GL_SHADER_STORAGE_BUFFER,1,buffid2)    #output
        glBindBuffer(GL_SHADER_STORAGE_BUFFER,buffid2)
    frame+=1
    sleep(0.25)


pg.quit()
glDeleteProgram(pid)
