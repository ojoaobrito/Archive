#version 330 core

layout(location = 0) in vec3 vertexPosition;
layout(location = 1) in vec3 vertexColor;

out vec3 fragmentColor;

void main(){
    gl_Position.xyz = vertexPosition;
    gl_Position.w = 1.0;

    gl_PointSize = 10;

    fragmentColor = vertexColor;
}