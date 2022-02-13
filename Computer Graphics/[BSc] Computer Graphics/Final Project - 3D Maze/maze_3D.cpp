// Include standard headers
#include <stdio.h>
#include <stdlib.h>
#include "Maze.h"
#include <iostream>

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
using namespace std;

// shaders header file
#include "loadShadders.hpp"

float x_camera = -50.0;
float y_camera = 100.0;
float z_camera = -50.0;
int keyboard = 0;
int maze_points = 0;

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

class Camera {
	private:
		float pitch = 0.0f;
		float yaw = 180.0f;
		//camera stuff
		glm::vec3 DirFront = glm::vec3(-1.0f, 0.0f, 0.0f);
		glm::vec3 DirUp = glm::vec3(0.0f, 1.0f, 0.0f);

		glm::mat4 *View;
	public:
		glm::vec3 pos = glm::vec3(-20.0f, -1.0f, -20.0f);
		glm::vec3 front() const {
			return DirFront;
		}
		glm::vec3 up() const {
			return DirUp;
		}
		glm::mat4 view() const {
			return *View;
		}

		void update() {
			(*View) = glm::lookAt(pos, pos + DirFront, DirUp);
		}

		float moveSensivity = 0.1;
		void move(glm::vec3 offset){
			pos += offset*moveSensivity;
		}
		void move(GLfloat xoffset, GLfloat yoffset, GLfloat zoffset){
			// pos += glm::vec3(xoffset, yoffset, zoffset);
			pos.x += xoffset*moveSensivity;
			pos.y += yoffset*moveSensivity;
			pos.z += zoffset*moveSensivity;
		}

		float sensitivity = 100.0f;

		void rotate(glm::vec2 offset){
			rotate(offset.x, offset.y);
		}
		void rotate(GLfloat xoffset, GLfloat yoffset)
		{
			xoffset *= sensitivity;
			yoffset *= sensitivity;

			yaw += xoffset;
			pitch += yoffset;

			if (pitch > 89.0f)
				pitch = 89.0f;
			if (pitch < -89.0f)
				pitch = -89.0f;

			glm::vec3 newFront;
			newFront.x = cos(glm::radians(pitch)) * cos(glm::radians(yaw));
			newFront.y = sin(glm::radians(pitch));
			newFront.z = cos(glm::radians(pitch)) * sin(glm::radians(yaw));
			DirFront = glm::normalize(newFront);
		}

		Camera (glm::mat4 *view) {
			View = view;
			update();
		}
		Camera (glm::mat4 *view, glm::vec3 initialPosition) {
			View = view;
			pos = initialPosition;
			(*View) = glm::lookAt(initialPosition, initialPosition + DirFront, DirUp);
		}
};

void process_keyboard(Camera *camera){
	glm::vec3 moveOffset(0);
	glm::vec2 rotationOffset(0);

	if(glfwGetKey(window, GLFW_KEY_W ) == GLFW_PRESS){
        
		// moveOffset.y += 0.1;
		moveOffset += camera->front();
        keyboard = 1;
	}

	if(glfwGetKey(window, GLFW_KEY_S ) == GLFW_PRESS){
        
		// moveOffset.y += -0.1;
		moveOffset += -camera->front();
        keyboard = 1;
	}
	if(glfwGetKey(window, GLFW_KEY_A ) == GLFW_PRESS){
        
		// moveOffset.z += 0.1;
		moveOffset -= glm::normalize(glm::cross(camera->front(), camera->up()));
        keyboard = 1;
	}
	if(glfwGetKey(window, GLFW_KEY_D ) == GLFW_PRESS){
        
		// moveOffset.z += -0.1;
		moveOffset += glm::normalize(glm::cross(camera->front(), camera->up()));
        keyboard = 1;
	}

    if(glfwGetKey(window, GLFW_KEY_UP ) == GLFW_PRESS && glfwGetKey(window, GLFW_KEY_LEFT_SHIFT ) == GLFW_PRESS){
        
		// moveOffset.y += 0.1;
		moveOffset = camera->up();
        keyboard = 1;
	}

    if(glfwGetKey(window, GLFW_KEY_DOWN ) == GLFW_PRESS && glfwGetKey(window, GLFW_KEY_LEFT_SHIFT ) == GLFW_PRESS){
        
		// moveOffset.y += 0.1;
		moveOffset = glm::vec3(0.0f,-1.0f,0.0f);
        keyboard = 1;
	}

	if(glfwGetKey(window, GLFW_KEY_UP ) == GLFW_PRESS && glfwGetKey(window, GLFW_KEY_LEFT_SHIFT ) != GLFW_PRESS){
        
		rotationOffset.y += 0.01;
        keyboard = 1;
	}
	if(glfwGetKey(window, GLFW_KEY_DOWN ) == GLFW_PRESS && glfwGetKey(window, GLFW_KEY_LEFT_SHIFT ) != GLFW_PRESS){
        
		rotationOffset.y += -0.01;
        keyboard = 1;
	}

    if(glfwGetKey(window, GLFW_KEY_LEFT ) == GLFW_PRESS){
        
		rotationOffset.x += -0.01;
        keyboard = 1;
	}
    
	if(glfwGetKey(window, GLFW_KEY_RIGHT ) == GLFW_PRESS){
        
		rotationOffset.x += 0.01;
        keyboard = 1;
	}

	camera->rotate(rotationOffset);
	camera->move(moveOffset);
}

//--------------------------------------------------------------------------------
void transferDataToGPUMemory(float* pontos, int tot_pontos, float* cores, int tot_cores){

    // VAO
    glGenVertexArrays(1, &VertexArrayID);
    glBindVertexArray(VertexArrayID);
    
    // Create and compile our GLSL program from the shaders
    programID = LoadShadders( "TransformVertexShader.vertexshader", "ColorFragmentShader.fragmentshader" );
    
    GLfloat cube[tot_pontos]; 

    for(int i=0; i<tot_pontos; i++)
        cube[i] = pontos[i];

    GLfloat cube_colors[tot_cores]; 

    for(int i=0; i<tot_cores; i++)
        cube_colors[i] = cores[i];
    
    // Move vertex data to video memory; specifically to VBO called vertexbuffer
    glGenBuffers(1, &vertexbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(cube), cube, GL_STATIC_DRAW);
    
    // Move color data to video memory; specifically to CBO called colorbuffer
    glGenBuffers(1, &colorbuffer);
    glBindBuffer(GL_ARRAY_BUFFER, colorbuffer);
    glBufferData(GL_ARRAY_BUFFER, sizeof(cube_colors), cube_colors, GL_STATIC_DRAW);
}

//--------------------------------------------------------------------------------
void cleanupDataFromGPU()
{
    glDeleteBuffers(1, &vertexbuffer);
    glDeleteBuffers(1, &colorbuffer);
    glDeleteVertexArrays(1, &VertexArrayID);
    glDeleteProgram(programID);
}

//--------------------------------------------------------------------------------
void setMVP(void)
{
    // Get a handle for our "MVP" uniform
    MatrixID = glGetUniformLocation(programID, "MVP");
    
    // Projection matrix : 45∞ Field of View, 4:3 ratio, display range : 0.1 unit <-> 100 units
    Projection = glm::perspective(glm::radians(45.0f), 4.0f / 3.0f, 0.1f, 1000.0f);
    
    // Camera matrix
    View = glm::lookAt(
                        glm::vec3(-8,25,-8), // Camera is at (4,3,-3), in World Space
                        glm::vec3(-20,-1,-20), // and looks at the origin
                        glm::vec3(0,1,0)  // Head is up (set to 0,-1,0 to look upside-down)
                        );
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

    static const GLfloat ponto_central[] = {
        0.0f, 0.0f, 0.0f
    };
    
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
    
    glDrawArrays(GL_TRIANGLES, 0, (maze_points/9)*3); //
    
    glDisableVertexAttribArray(0);
    glDisableVertexAttribArray(1);
}
//--------------------------------------------------------------------------------

int main(void){

    Maze maze(5);
    maze.build_maze_matrix(0.2); // aprox. 20% de buracos
    maze.maze_coordinates();
    maze_points = maze.tot_coordinates;

    /*
    for(int i=0; i<maze_points; i++){

        std::cout << maze.cube_coordinates[i] << " ";
    }

    std::cout << "\n";*/

    // Initialise GLFW
    glfwInit();
    
    glfwWindowHint(GLFW_SAMPLES, 4);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE); // To make MacOS happy; should not be needed
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
    
    // Open a window
    window = glfwCreateWindow( WindowWidth, WindowHeight, "3D Maze", NULL, NULL);
    
    // Create window context
    glfwMakeContextCurrent(window);
    
    // Initialize GLEW
    glewExperimental = true; // Needed for core profile
    glewInit();
    
    // Ensure we can capture the escape key being pressed below
    glfwSetInputMode(window, GLFW_STICKY_KEYS, GL_TRUE);
    
    // White background
    glClearColor(204/255.0, 205/255.0, 249/255.0, 0.0f);
    
    // Clear the screen
    glClear( GL_COLOR_BUFFER_BIT );
    
    // Enable depth test
    glEnable(GL_DEPTH_TEST);
    // Accept fragment if it closer to the camera than the former one
    glDepthFunc(GL_LESS);
    
    // transfer my data (vertices, colors, and shaders) to GPU side
    transferDataToGPUMemory(maze.cube_coordinates, maze.tot_coordinates, maze.cube_colors, maze.tot_colors);

    // set the model-view-projection matrix
    setMVP();
    
    // render scene for each frame
	Camera camera(&View, glm::vec3(30,20,-10));
    do{

		process_keyboard(&camera);
        
        if(keyboard==1)
		    camera.update();
        /*
        printf("X = %f\n",camera.pos.x);
        printf("Y = %f\n",camera.pos.y);
        printf("Z = %f\n",camera.pos.z);
        */

        cubeMVP = Projection * View * cubeModel;

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