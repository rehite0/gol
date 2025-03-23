#version 430

layout(local_size_x = 8,local_size_y=8) in;
layout(std430, binding = 0) buffer data_buff
{
    int data[];
};
layout(std430, binding = 1) buffer data_buff2
{
    int data2[];
};


void main(void){
	uvec3 id=gl_GlobalInvocationID;
    data2[id.y*80+id.x] =data[id.y*80+id.x]+ 1;
}
