// Include standard headers
#include <stdio.h>
#include <stdlib.h>

// Include GLEW
#include <GL/glew.h>

// Include GLFW
#include <GLFW/glfw3.h>
GLFWwindow* window;

// GLM header file
#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>
#include <glm/gtc/type_ptr.hpp>
using namespace glm;

// shaders header file
#include "loadShadders.hpp"

float x_camera = 4.0;
float y_camera = 3.0;
float z_camera = -3.0;

// Vertex array object (VAO)
GLuint VertexArrayID;

// Vertex buffer object (VBO)
GLuint vertexbuffer;

// color buffer object (CBO)
GLuint colorbuffer;

// Vertex buffer object (VBO)
GLuint pyramidbuffer;

// color buffer object (CBO)
GLuint pyramidcolorbuffer;

// GLSL program from the shaders
GLuint programID;

// Matrix id of the MVP
GLuint MatrixID;
glm::mat4 cubeMVP;
glm::mat4 pyramidMVP;

GLint WindowWidth = 1024;
GLint WindowHeight = 768;

glm::mat4 pyramidModel = glm::mat4(1.0f);
glm::mat4 cubeModel = glm::mat4(1.0f);

GLfloat delta = 0.005f;
GLfloat angulo = 0.0f;

glm::mat4 Projection = glm::mat4(1.0f);
glm::mat4 View = glm::mat4(1.0f);

GLfloat tx = 0.0f;

//--------------------------------------------------------------------------------
void transferDataToGPUMemory(void)
{
    // VAO
    glGenVertexArrays(1, &VertexArrayID);
    glBindVertexArray(VertexArrayID);
    
    // Create and compile our GLSL program from the shaders
    programID = LoadShadders( "TransformVertexShader.vertexshader", "ColorFragmentShader.fragmentshader" );
    
    
    // Our vertices. Tree consecutive floats give a 3D vertex; Three consecutive vertices give a triangle.
    // A cube has 6 faces with 2 triangles each, so this makes 6*2=12 triangles, and 12*3 vertices
    static const GLfloat cube[] = {
        -1.0f,-1.0f,-1.0f,  -1.0f,-1.0f, 1.0f,  -1.0f, 1.0f, 1.0f,
         1.0f, 1.0f,-1.0f,  -1.0f,-1.0f,-1.0f,  -1.0f, 1.0f,-1.0f,
         1.0f,-1.0f, 1.0f,  -1.0f,-1.0f,-1.0f,   1.0f,-1.0f,-1.0f,
         1.0f, 1.0f,-1.0f,   1.0f,-1.0f,-1.0f,  -1.0f,-1.0f,-1.0f,
        -1.0f,-1.0f,-1.0f,  -1.0f, 1.0f, 1.0f,  -1.0f, 1.0f,-1.0f,
         1.0f,-1.0f, 1.0f,  -1.0f,-1.0f, 1.0f,  -1.0f,-1.0f,-1.0f,
        -1.0f, 1.0f, 1.0f,  -1.0f,-1.0f, 1.0f,   1.0f,-1.0f, 1.0f,
         1.0f, 1.0f, 1.0f,   1.0f,-1.0f,-1.0f,   1.0f, 1.0f,-1.0f,
         1.0f,-1.0f,-1.0f,   1.0f, 1.0f, 1.0f,   1.0f,-1.0f, 1.0f,
         1.0f, 1.0f, 1.0f,   1.0f, 1.0f,-1.0f,  -1.0f, 1.0f,-1.0f,
         1.0f, 1.0f, 1.0f,  -1.0f, 1.0f,-1.0f,  -1.0f, 1.0f, 1.0f,
         1.0f, 1.0f, 1.0f,  -1.0f, 1.0f, 1.0f,   1.0f,-1.0f, 1.0f
    };
    
    // One color for each vertex. They were generated randomly.
    static const GLfloat cube_colors[] = {

        0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    // cyan
        0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    // green
        1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    // red
        0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    // green
        0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    // cyan
        1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    // red
        1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f,    // magenta
        1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    // yellow
        1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    // yellow
        0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    // blue
        0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    // blue
        1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f     // magenta
    };
    
    static const GLfloat pyramid[] = {
        1.0f, 1.0f, 1.0f,   1.0f,1.0f,-1.0f,    -1.0f, 1.0f,1.0f,
        -1.0f, 1.0f,1.0f,    1.0f,1.0f,-1.0f,    -1.0f, 1.0f,-1.0f,
        1.0f, 1.0f, 1.0f,   1.0f,1.0f,-1.0f,    0.0f, 1.35f, 0.0f,
        0.0f, 1.35f, 0.0f,   1.0f, 1.0f, -1.0f,   -1.0f,1.0f,-1.0f,
        0.0f, 1.35f, 0.0f,   -1.0f, 1.0f, -1.0f,   -1.0f,1.0f,1.0f,
        0.0f, 1.35f, 0.0f,  -1.0f, 1.0f, 1.0f,   1.0f,1.0f,1.0f,
    };
    
    // One color for each vertex. They were generated randomly.
    static const GLfloat pyramid_colors[] = {
        
        0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    0.00f,  1.0f,  1.0f,    // cyan
        0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    0.00f,  1.0f,  0.0f,    // green
        1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    1.00f,  0.0f,  0.0f,    // red
        0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    0.00f,  0.0f,  1.0f,    // blue
        1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    1.00f,  1.0f,  0.0f,    // yellow
        1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f,    1.00f,  0.0f,  1.0f     // magenta
    };
    
    // Move vertex data to video memory; specifically to VBO called vertexbuffer
    glGenBuffers(1, &vertexbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(cube), cube, GL_STATIC_DRAW);
    
    // Move color data to video memory; specifically to CBO called colorbuffer
    glGenBuffers(1, &colorbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(cube_colors), cube_colors, GL_STATIC_DRAW);
    
    // Move vertex data to video memory; specifically to VBO called vertexbuffer
    glGenBuffers(1, &pyramidbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, pyramidbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(pyramid), pyramid, GL_STATIC_DRAW);
    
    // Move color data to video memory; specifically to CBO called colorbuffer
    glGenBuffers(1, &pyramidcolorbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, pyramidcolorbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(pyramid_colors), pyramid_colors, GL_STATIC_DRAW);
}

//--------------------------------------------------------------------------------
void cleanupDataFromGPU()
{
    glDeleteBuffers(1, &vertexbuffer);
    glDeleteBuffers(1, &pyramidbuffer);
    glDeleteBuffers(1, &colorbuffer);
    glDeleteBuffers(1, &pyramidcolorbuffer);
    glDeleteVertexArrays(1, &VertexArrayID);
    glDeleteProgram(programID);
}

//--------------------------------------------------------------------------------
void setMVP(int inicio, float x, float y, float z)
{
    // Get a handle for our "MVP" uniform
    MatrixID = glGetUniformLocation(programID, "MVP");
    
    // Projection matrix : 45∞ Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
    Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 100.0f);
    
    // Camera matrix
    if(inicio==1){

        View = glm::lookAt(glm::vec3(4.0,3.0,-3.0), // Camera is at (4,3,-3), in World Space
                            glm::vec3(0,0,0), // and looks at the origin
                            glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
                            );

    }

    else{

        View = glm::lookAt(glm::vec3(x,y,z), // Camera is at (4,3,-3), in World Space
                       glm::vec3(0,0,0), // and looks at the origin
                       glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
                       );
    }
    
    // Model matrix depends on the object, so it is defined somewhere in the program
 }

//--------------------------------------------------------------------------------
void draw (void)
{
    // Clear the screen
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    
    // Use our shader
    glUseProgram(programID);
    
    // Send our transformation to the currently bound shader,
    // in the "MVP" uniform, which is now cubeMVP
    glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &cubeMVP[0][0]);
    
    // 1rst attribute buffer : vertices
    glEnableVertexAttribArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    glVertexAttribPointer(
                          0,                  // attribute 0. No particular reason for 0, but must match the layout in the shader.
                          3,                  // size
                          GL_FLOAT,           // type
                          GL_FALSE,           // normalized?
                          0,                  // stride
                          (void*)0            // array buffer offset
                          );
    
    // 2nd attribute buffer : colors
    glEnableVertexAttribArray(1);
    glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
    glVertexAttribPointer(
                          1,                                // attribute. No particular reason for 1, but must match the layout in the shader.
                          3,                                // size
                          GL_FLOAT,                         // type
                          GL_FALSE,                         // normalized?
                          0,                                // stride
                          (void*)0                          // array buffer offset
                          );
    
    glDrawArrays(GL_TRIANGLES, 0, 12*3); //
    
    glDisableVertexAttribArray(0);
    glDisableVertexAttribArray(1);
    
    
    // "MVP" uniform is now pyramidMVP
    glUniformMatrix4fv(MatrixID, 1, GL_FALSE, &pyramidMVP[0][0]);
    
    // 1rst attribute buffer : vertices
    glEnableVertexAttribArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, pyramidbuffer);
    glVertexAttribPointer(
                          0,            // No particular reason for 0, but must match the layout in the shader.
                          3,            // size
                          GL_FLOAT,     // type
                          GL_FALSE,     // normalized?
                          0,            // stride
                          (void*)0      // array buffer offset
                          );
    
    // 2nd attribute buffer : colors
    glEnableVertexAttribArray(1);
    glBindBuffer(GL_ARRAY_BUFFER, pyramidcolorbuffer);
    glVertexAttribPointer(
                          1,            // No particular reason for 1, but must match the layout in the shader.
                          3,            // size
                          GL_FLOAT,     // type
                          GL_FALSE,     // normalized?
                          0,            // stride
                          (void*)0      // array buffer offset
                          );
    
    glDrawArrays(GL_TRIANGLES, 0, 6*3); //

    glDisableVertexAttribArray(0);
    glDisableVertexAttribArray(1);
}
//--------------------------------------------------------------------------------

int main( void )
{
    // Initialise GLFW
    glfwInit();
    
    glfwWindowHint(GLFW_SAMPLES, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    
    // Open a window
    window = glfwCreateWindow( WindowWidth, WindowHeight, "Moving block and roof of a house", NULL, NULL);
    
    // Create window context
    glfwMakeContextCurrent(window);
    
    // Initialize GLEW
    glewExperimental = true; // Needed for core profile
    glewInit();
    
    // Ensure we can capture the escape key being pressed below
    glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);
    
    // White background
    glClearColor(1.0f, 1.0f, 1.0f, 0.0f);
    
    // Clear the screen
    glClear( GL_COLOR_BUFFER_BIT );
    
    // Enable depth test
    glEnable(GL_DEPTH_TEST);
    // Accept fragment if it closer to the camera than the former one
    glDepthFunc(GL_LESS);
    
    // transfer my data (vertices, colors, and shaders) to GPU side
    transferDataToGPUMemory();

    int inicio = 1;

    // set the model-view-projection matrix
    setMVP(1,4,3,-3);
    
    // render scene for each frame
    do{
        // Strafe right
        if (glfwGetKey(window, GLFW_KEY_DOWN ) == GLFW_PRESS){
            setMVP(0,x_camera+0.05,y_camera+0.05,z_camera-0.05);
            z_camera -= 0.05;
            x_camera += 0.05;
        }
        // Strafe left
        if (glfwGetKey(window, GLFW_KEY_UP ) == GLFW_PRESS){
            setMVP(0,x_camera-0.05,y_camera+0.05,z_camera-0.05);
            z_camera += 0.05;
            x_camera -= 0.05;
        }

        if(glfwGetKey(window, GLFW_KEY_RIGHT ) == GLFW_PRESS){
            setMVP(0,x_camera-0.2,y_camera+0.05,z_camera-0.05);

        }

        // let us update the rotation angle for cube
        angulo += delta;
        angulo = (angulo/360-1)*360;
        //cubeModel = glm::rotate(cubeModel,glm::radians(angulo),glm::vec3(0,1,0));
        cubeMVP = Projection * View * cubeModel;

        // let us update the position of the roof
        tx -= 0.00001;
        //pyramidModel = glm::translate(pyramidModel,glm::vec3(tx,-tx,0));
        pyramidMVP = Projection * View * pyramidModel;

        // draw cube and roof
        draw();
        // Swap buffers
        glfwSwapBuffers(window);
        // looking for events
        glfwPollEvents();
        
    } // Check if the ESC key was pressed or the window was closed
    while( glfwGetKey(window, GLFW_KEY_ESCAPE ) != GLFW_PRESS &&
          glfwWindowShouldClose(window) == 0 );
    
    // Cleanup VAO, VBOs, and shaders from GPU
    cleanupDataFromGPU();
    
    // Close OpenGL window and terminate GLFW
    glfwTerminate();
    
    return 0;
}