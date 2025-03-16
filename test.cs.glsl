#version 430

layout(local_size_x = 5) in;
layout(std430, binding = 0) buffer data_buff
{
    int data[];
};

void main(void){
    data[gl_GlobalInvocationID.x] =data[gl_GlobalInvocationID.x]+ 1;
}
