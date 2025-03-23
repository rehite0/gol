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

uniform uvec2 dim;

void main(void){
	uvec3 id=gl_GlobalInvocationID;
	if( id.x>=dim.x || id.y>=dim.y ) {return;}
	if( id.x==0 || id.y==0 || id.x>=dim.x-1 || id.y>=dim.y-1 )
	{	data2[id.y*dim.x+id.x]=0;return;}
	int sum=0;
	sum=data[id.y*dim.x+(id.x+1)]
	   +data[id.y*dim.x+(id.x-1)]

	   +data[(id.y+1)*dim.x+id.x]
	   +data[(id.y+1)*dim.x+(id.x+1)]
	   +data[(id.y+1)*dim.x+(id.x-1)]

	   +data[(id.y-1)*dim.x+id.x]
	   +data[(id.y-1)*dim.x+(id.x+1)]
	   +data[(id.y-1)*dim.x+(id.x-1)];
	if( sum<2 )
	{	data2[id.y*dim.x+id.x] =0;return;	}
	else if( sum<3 )
	{	data2[id.y*dim.x+id.x] =data[id.y*dim.x+id.x];;return;	}
	else if( sum<4 )
	{	data2[id.y*dim.x+id.x] =1;return;	}
	else
	{	data2[id.y*dim.x+id.x] =0;return;	}
}
