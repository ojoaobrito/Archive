#include <stdio.h>
#include <stdlib.h>
#include "Maze.h"

using namespace std;

int main(int argc, char**argv){

    Maze maze(5);
    maze.build_maze_matrix();
    maze.maze_coordinates();

    // estas 2 variáveis ficam com o resultado final
    // maze.cube_coordinates
    // maze.cube_colors

    return(0);
}