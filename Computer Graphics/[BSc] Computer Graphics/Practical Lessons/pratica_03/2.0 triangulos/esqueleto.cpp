#include <stdio.h>
#include <stdlib.h>

#include <GL/glew.h>

#include <GLFW/glfw3.h>
GLFWwindow *window;

#include <glm/glm.hpp>
using namespace glm;

#include "loadShadders.hpp"

GLuint VertexArrayID;
GLuint vertexbuffer;
GLuint colorbuffer;
GLuint programID;

void transferDataToGPUMemory(void);
void cleanupDataFromGPU();
void draw();

int main(){
    glfwInit();

    glfwWindowHint(GLFW_SAMPLES, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);    
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);    
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);    
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);    

    window = glfwCreateWindow(1024, 768, "skir", NULL, NULL);

    glfwMakeContextCurrent(window);

    glewExperimental = true;
    glewInit();

    glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);

    glClearColor(0.0f, 0.0f, 0.4f, 0.0f);
    
    transferDataToGPUMemory();

    do{
        draw();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }while(glfwGetKey(window, GLFW_KEY_ESCAPE) != GLFW_PRESS && glfwWindowShouldClose(window) == 0);

    cleanupDataFromGPU();
    glfwTerminate();
    return 0;

}



void transferDataToGPUMemory(void){
    glGenVertexArrays(1, &VertexArrayID);
    glBindVertexArray(VertexArrayID);

    programID = LoadShaders("vertexshader.vs", "fragmentshader.fs");

    static const GLfloat g_vertex_buffer_data[] = {
        -1.0f, -1.0f, 0.0f,
        1.0f, -1.0f, 0.0f,
        0.0f, 1.0f, 0.0f,
        -1.0f, 1.0f, 0.0f,
        1.0f, 1.0f, 0.0f,
        0.0f, -1.0f, 0.0f,
    };

    static const GLfloat g_color_buffer_data[] = {
        1.0f,  0.0f,  0.0f,
        1.0f,  0.0f,  0.0f,
        1.0f,  0.0f,  0.0f,
        0.0f,  1.0f,  0.0f,
        0.0f,  1.0f,  0.0f,
        0.0f,  1.0f,  0.0f,
    };

    glGenBuffers(1, &vertexbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(g_vertex_buffer_data), g_vertex_buffer_data, GL_STATIC_DRAW);

    glGenBuffers(1, &colorbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(g_color_buffer_data), g_color_buffer_data, GL_STATIC_DRAW);
}




void cleanupDataFromGPU(){
    glDeleteBuffers(1, &vertexbuffer);
    glDeleteBuffers(1, &colorbuffer);
    glDeleteVertexArrays(1, &VertexArrayID);
    glDeleteProgram(programID);
}




void draw (void){
    // Clear the screen
    glClear( GL_COLOR_BUFFER_BIT );
    // Use our shader
    glUseProgram(programID);
    // 1rst attribute buffer : vertices
    glEnableVertexAttribArray(0); 
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer); 
    glVertexAttribPointer(
        0,
        3,
        GL_FLOAT,
        GL_FALSE,
        0,
        (void*)0
    );

    glEnableVertexAttribArray(1); 
    glBindBuffer(GL_ARRAY_BUFFER, colorbuffer); 
    glVertexAttribPointer(
        1,
        3, GL_FLOAT, GL_FALSE, 0,
        (void*)0
    );

    glDrawArrays(GL_TRIANGLES, 0, 6); // 6 indices starting at 0
    // Disable arrays of attributes for vertices
    glDisableVertexAttribArray(0);
    glDisableVertexAttribArray(1); 
}