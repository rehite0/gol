import numpy as np
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
import time



vert=vert.flatten()
vao=glGenVertexArrays(1)
glBindVertexArray(vao)
vbo=glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, vert.nbytes,vert,GL_STATIC_DRAW)
glEnableVertexAttribArray(0)
glVertexAttribPointer(0,2,GL_FLOAT,GL_FALSE,4*2,ctypes.c_void_p(0))

with open("sha.frag.glsl") as f:
	frag_src=f.readlines()
with open("sha.vert.glsl") as f:
	vert_src=f.readlines()
pid=compileProgram(
	compileShader(vert_src,GL_VERTEX_SHADER)
	,compileShader(frag_src,GL_FRAGMENT_SHADER)
	)
glUseProgram(pid)

while(int(input("enter 0 to exit:"))==0):
	glBindVertexArray(vao)

glDeleteProgram(pid)
glDeleteVertexArrays(1,(vao,))
glDeleteBuffers(1,(vbo,))
