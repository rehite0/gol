import numpy as np
import pygame as pg
#import ctypes
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader

glo={"h":100
    ,"w":100
    ,"bufflen":None
    ,"shaderpid":None
    ,"buffid1":None
    ,"buffid2":None
    }
#glo["bufflen"]=5    #glo["h"]*glo["w"]

pg.init()
pg.display.set_mode((800,400),pg.OPENGL)
#clock=pg.time.Clock()

with open("test.cs.glsl",'r') as f:
    src=f.readlines()
pid=compileProgram(compileShader(src,GL_COMPUTE_SHADER))
glUseProgram(pid)

glo["buffid1"],glo["buffis2"]=glGenBuffers(2)
glBindBuffer(GL_SHADER_STORAGE_BUFFER,glo["buffid1"]);
data=np.array([1,2,3,4,5],dtype="int32")
glo["bufflen"]=data.nbytes
glBufferData(GL_SHADER_STORAGE_BUFFER, glo["bufflen"], data, GL_DYNAMIC_COPY)
#insert buff data
glBindBufferBase(GL_SHADER_STORAGE_BUFFER,0,glo["buffid1"]);
#glBindBuffer(GL_SHADER_STORAGE_BUFFER,glo["buffid2"]);
#glBindBufferBase(GL_SHADER_STORAGE_BUFFER,1,glo["buffid2"]);
glMemoryBarrier(GL_SHADER_STORAGE_BARRIER_BIT)

#glUseProgram(glo["shaderpid"]);
glDispatchCompute(1,1,1);
data=glGetBufferSubData(GL_SHADER_STORAGE_BUFFER,0,glo["bufflen"])
data.dtype='int32'
print(data)
pg.quit()
glDeleteProgram(pid)
#glDeleteBuffers(1,(vbo,))
