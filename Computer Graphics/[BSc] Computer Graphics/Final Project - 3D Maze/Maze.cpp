#include <iostream>
#include "Maze.h"

using namespace std;

Maze::Maze(int size_in){

    size = size_in;

    // inicializar a matriz auxiliar
    aux_matrix = (int**)malloc(size*sizeof(int*));
    for(int i=0; i<size; i++){
        aux_matrix[i] = (int*)malloc(size*sizeof(int));
        for(int j=0; j<size; j++)
            aux_matrix[i][j] = 1;
    }

    // inicializar a matriz que representa o labirinto na forma de blocos
    matrix = (char**)malloc(((size*2)+1)*sizeof(char*));
    for(int i=0; i<((size*2)+1); i++)
        matrix[i] = (char*)malloc(((size*2)+1)*sizeof(char));
    
    // estrutura inicial
    maze = (char***)malloc(size*sizeof(char**)); // lines

    for(int i=0; i<size; i++) // columns
        maze[i] = (char**)malloc(size*sizeof(char*));

    for(int i=0; i<size; i++){

        for(int j=0; j<size; j++){

            if(j==0){
                
                maze[i][j] = (char*)malloc(3*sizeof(char));
                maze[i][j][0] = '|';
                maze[i][j][1] = '_';
                maze[i][j][2] = '|';
                maze[i][j][3] = '\0';
            }
            
            else{

                maze[i][j] = (char*)malloc(2*sizeof(char));
                maze[i][j][0] = '_';
                maze[i][j][1] = '|';
                maze[i][j][2] = '\0';
            }
        }
    }

    Maze::build_maze(1); // por defeito, constrói-se logo o labirinto
}

void Maze::build_maze(int inicio){

    int r;
    Cell current;
    Cell* options = NULL;

    if(inicio==1){ // escolher o ponto de entrada

        srand(time(NULL)); 
        r = rand() % size;

        initial_cell = r;
        current.column = r;
        current.line = 0;

        path = (Cell*)realloc(path,(++tot)*sizeof(Cell));
        path[tot-1] = current;
    }

    current = path[tot-1];
    options = movement_options(current);

    while(options==NULL){ // não há possibilidades de movimento, temos de fazer backtrack

        path = (Cell*)realloc(path,(--tot)*sizeof(Cell));
        current = path[tot-1];

        // critério de paragem
        if(all_visited()==1){

            /*
            // definir o ponto de saída
            r = rand() % size;

            if(r==0)
                (*(*(maze+(size-1))+r))[1] = ' ';
            else
                (*(*(maze+(size-1))+r))[0] = ' ';

            final_cell = r;*/
            return;
        }
        
        options = movement_options(current);
    }

    // escolher uma célula candidata aleatoriamente
    r = rand() % tot_options;

    path = (Cell*)realloc(path,(++tot)*sizeof(Cell));
    path[tot-1] = options[r];

    // se for a célula acima
    if(options[r].line<current.line){

        if(options[r].column==0)
            (*(*(maze+options[r].line)+options[r].column))[1] = ' '; 
        
        else
            (*(*(maze+options[r].line)+options[r].column))[0] = ' '; 

        aux_matrix[options[r].line][options[r].column] = 0;
    }

    // se for a célula da direita
    else if(options[r].column>current.column){

        if(current.column==0)
            (*(*(maze+current.line)+current.column))[2] = ' ';
        
        else
            (*(*(maze+current.line)+current.column))[1] = ' ';

        aux_matrix[options[r].line][options[r].column] = 0;
    }

    // se for a célula da esquerda
    else if(options[r].column<current.column){

        if(options[r].column==0)
            (*(*(maze+options[r].line)+options[r].column))[2] = ' '; 
        
        else
            (*(*(maze+options[r].line)+options[r].column))[1] = ' '; 

        aux_matrix[options[r].line][options[r].column] = 0;
    }

    // se for a célula de baixo
    else if(options[r].line>current.line){

        if(options[r].column==0)
            (*(*(maze+current.line)+current.column))[1] = ' '; 
        
        else
            (*(*(maze+current.line)+current.column))[0] = ' '; 

        aux_matrix[options[r].line][options[r].column] = 0;
    }

    build_maze(0);
}

Cell* Maze::movement_options(Cell atual){

    Cell* options = NULL;
    tot_options = 0;

    // célula acima
    if(atual.line>0 && aux_matrix[atual.line-1][atual.column]==1){

        Cell aux;
        aux.line = atual.line-1;
        aux.column = atual.column;
        options = (Cell*)realloc(options,(++tot_options)*sizeof(Cell));
        options[tot_options-1] = aux;
    }

    // célula da direita
    if(atual.column<(size-1) && aux_matrix[atual.line][atual.column+1]==1){

        Cell aux;
        aux.line = atual.line;
        aux.column = atual.column+1;
        options = (Cell*)realloc(options,(++tot_options)*sizeof(Cell));
        options[tot_options-1] = aux;
    }

    // célula da esquerda
    if(atual.column>0 && aux_matrix[atual.line][atual.column-1]==1){

        Cell aux;
        aux.line = atual.line;
        aux.column = atual.column-1;
        options = (Cell*)realloc(options,(++tot_options)*sizeof(Cell));
        options[tot_options-1] = aux;
    }

    // célula abaixo
    if(atual.line<(size-1) && aux_matrix[atual.line+1][atual.column]==1){

        Cell aux;
        aux.line = atual.line+1;
        aux.column = atual.column;
        options = (Cell*)realloc(options,(++tot_options)*sizeof(Cell));
        options[tot_options-1] = aux;
    }

    return(options);
}

void Maze::print_maze(){

    // parede de cima (já com o ponto de entrada do labirinto)
    char* top = NULL;
    int tot = 0;

    for(int i=0; i<size; i++){

        top = (char*)realloc(top,(tot+2)*sizeof(char));
        tot += 2;
        top[tot-2] = ' ';

        if(i==initial_cell)
            top[tot-1] = ' ';
        else
            top[tot-1] = '_';
    }

    top[tot] = '\0';
    printf("%s\n",top);

    // imprimir o labirinto
    for(int i=0; i<size; i++){ // lines

        for(int j=0; j<size; j++) // columns
            printf("%s",maze[i][j]);

        printf("\n");
    }
}

void Maze::save_maze(){

    FILE *f = NULL;

    f = fopen("maze_blocks.txt","w");

    for(int i=0; i<((size*2)+1); i++){

        for(int j=0; j<((size*2)+1); j++)
            putc(matrix[i][j],f);
        putc('\n',f);
    }

    fclose(f);
}

void Maze::build_maze_matrix(float frequencia){

    int i, j, tot = 0, r = 0;
    int* columns = NULL;
    int* lines = NULL;
    float num_paredes = 0.0, num_buracos = 0.0;
    char matrix_temp[(size*2)+1][(size*2)+1];

    // pontos de referências (lines)
    for(i=1; i<((size*2)+1); i=i+2){

        lines = (int*)realloc(lines,(++tot)*sizeof(int));
        lines[tot-1] = i;
    }

    tot = 0;

    // pontos de referências (columns)
    for(i=1; i<((size*2)+1); i=i+2){

        columns = (int*)realloc(columns,(++tot)*sizeof(int));
        columns[tot-1] = i;
    }

    // inicializar a matriz
    for(i=0; i<((size*2)+1); i++){

        for(j=0; j<((size*2)+1); j++){

            matrix[i][j] = 'X';
            matrix_temp[i][j] = 'X';
        }
    }

    // construir as paredes e espaços livres
    for(i=0; i<size; i++){

        for(j=0; j<size; j++){
            
            matrix[lines[i]][columns[j]] = ' ';
            matrix_temp[lines[i]][columns[j]] = ' ';

            if(j==0){ // caso especial
                
                if((*((*(maze+i))+j))[2]=='|'){ // célula à direita
                    
                    matrix[lines[i]][columns[j]+1] = 'X';
                    matrix_temp[lines[i]][columns[j]+1] = 'X';
                }
                
                else{
                    
                    matrix[lines[i]][columns[j]+1] = ' ';
                    matrix_temp[lines[i]][columns[j]+1] = ' ';
                }
                
                if((*((*(maze+i))+j))[1]=='_'){ // célula abaixo
                    
                    matrix[lines[i]+1][columns[j]] = 'X';
                    matrix_temp[lines[i]+1][columns[j]] = 'X';
                }

                else{
                    
                    matrix[lines[i]+1][columns[j]] = ' ';
                    matrix_temp[lines[i]+1][columns[j]] = ' ';
                }
            }

            else{

                if((*((*(maze+i))+j))[1]=='|'){ // célula à direita
                    
                    matrix[lines[i]][columns[j]+1] = 'X';
                    matrix_temp[lines[i]][columns[j]+1] = 'X';
                }
                
                else{

                    matrix[lines[i]][columns[j]+1] = ' ';
                    matrix_temp[lines[i]][columns[j]+1] = ' ';
                }
                
                if((*((*(maze+i))+j))[0]=='_'){ // célula abaixo
                    
                    matrix[lines[i]+1][columns[j]] = 'X';
                    matrix_temp[lines[i]+1][columns[j]] = 'X';
                }

                else{

                    matrix[lines[i]+1][columns[j]] = ' ';
                    matrix_temp[lines[i]+1][columns[j]] = ' ';
                }
            }
        }
    }
    
    do{
        r = rand() % ((size*2)-2);
    } while(matrix[1][r+1]=='X');

    initial_cell = r+1; 

    do{   
        r = rand() % ((size*2)-2);
    } while((r+1)==initial_cell or matrix[((size*2)-1)][r+1]=='X');

    final_cell = r+1;

    matrix[0][initial_cell] = ' ';
    matrix[((size*2))][final_cell] = ' ';
    matrix_temp[0][initial_cell] = ' ';
    matrix_temp[((size*2))][final_cell] = ' ';

    for(i=1; i<((size*2)); i++){

        for(j=1; j<((size*2)); j++){

            if(matrix[i][j]=='X')
                num_paredes++;
        }
    }

    // definir onde estão os buracos
    do{
        num_buracos = 0;
        for(i=0; i<((size*2)+1); i++){

            for(j=0; j<((size*2)+1); j++){

                matrix[i][j] = matrix_temp[i][j];
            }
        }

        for(i=1; i<(size*2); i++){

            for(j=1; j<(size*2); j++){

                if(matrix[i][j]==' ') // chão, não interessa
                    continue;
                
                r = rand() % 10;
                
                if(r<((int)(frequencia*10.0))){
                    
                    matrix[i][j] = 'O';
                    num_buracos++;
                }
            }
        }

    }while((num_buracos/num_paredes)<(frequencia-0.05) or (num_buracos/num_paredes)>(frequencia+0.05));

    // imprimir a matriz
    for(i=0; i<((size*2)+1); i++){

        for(j=0; j<((size*2)+1); j++)
            printf("%c",matrix[i][j]);

        printf("\n");
    }
}

int Maze::all_visited(){

    int i,j;

    for(i=0; i<size; i++){

        for(j=0; j<size; j++){

            if(aux_matrix[i][j]==1)
                return(0);
        }
    }

    return(1);
}

void Maze::maze_coordinates(){

    char e;
    float* cube = NULL;
    float cube_color = (0/255.0), floor_color = (255/255.0);
    int i = 0, j = 0, k = 0, tot = 0, controlo = 0, floor_control = 0;

    float base[] = { // base do labirinto (1º cubo)

         ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)),-1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)), 1.0, ((float)((size*2)+1)),
         ((float)((size*2)+1)), 1.0, ((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)), 1.0,((float)(((size*2)+1)-2)),

         ((float)((size*2)+1)),-1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)),   ((float)((size*2)+1)),-1.0,((float)(((size*2)+1)-2)), // chão
         ((float)((size*2)+1)), 1.0, ((float)(((size*2)+1)-2)),   ((float)((size*2)+1)),-1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)),

         ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)), 1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)), 1.0,((float)(((size*2)+1)-2)),
         ((float)((size*2)+1)),-1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)),-1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)),-1.0,((float)(((size*2)+1)-2)), // chão

         ((float)(((size*2)+1)-2)), 1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)),-1.0, ((float)((size*2)+1)),   ((float)((size*2)+1)),-1.0, ((float)((size*2)+1)),
         ((float)((size*2)+1)), 1.0, ((float)((size*2)+1)),   ((float)((size*2)+1)),-1.0,((float)(((size*2)+1)-2)),   ((float)((size*2)+1)), 1.0,((float)(((size*2)+1)-2)),

         ((float)((size*2)+1)),-1.0,((float)(((size*2)+1)-2)),   ((float)((size*2)+1)), 1.0, ((float)((size*2)+1)),   ((float)((size*2)+1)),-1.0, ((float)((size*2)+1)),
         ((float)((size*2)+1)), 1.0, ((float)((size*2)+1)),   ((float)((size*2)+1)), 1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)), 1.0,((float)(((size*2)+1)-2)),

         ((float)((size*2)+1)), 1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)), 1.0,((float)(((size*2)+1)-2)),  ((float)(((size*2)+1)-2)), 1.0, ((float)((size*2)+1)),
         ((float)((size*2)+1)), 1.0, ((float)((size*2)+1)),  ((float)(((size*2)+1)-2)), 1.0, ((float)((size*2)+1)),   ((float)((size*2)+1)),-1.0, ((float)((size*2)+1)),
    };

    for(i=0; i<((size*2)+1); i++){ // obter as coordenadas de cada cubo/espaço livre do labirinto

        for(j=0; j<((size*2)+1); j++){

            if(matrix[i][j]=='X'){ // bloco

                for(k=0; k<108; k++){

                    if(controlo==0){ // alterar a coordenada x

                        cube = (float*)realloc(cube,(++tot)*sizeof(float));
                        cube[tot-1] = base[k] - (j*2);
                    }

                    else if(controlo==1){ // manter a coordenada y

                        cube = (float*)realloc(cube,(++tot)*sizeof(float));
                        cube[tot-1] = base[k];
                    }

                    else if(controlo==2){ // alterar a coordenada z

                        cube = (float*)realloc(cube,(++tot)*sizeof(float));
                        cube[tot-1] = base[k] - (i*2);
                        controlo = -1;
                    }

                    controlo++;
                }

                for(k=0; k<tot; k++){

                    cube_coordinates = (float*)realloc(cube_coordinates,(++tot_coordinates)*sizeof(float));
                    cube_coordinates[tot_coordinates-1] = cube[k];
                    cube_colors = (float*)realloc(cube_colors,(++tot_colors)*sizeof(float));
                    cube_colors[tot_colors-1] = cube_color;
                }
                
                free(cube);
                cube = NULL;
                tot = 0;
            }

            else if(matrix[i][j]==' '){ // chão

                while(floor_control!=54){

                    for(k=18+floor_control; k<27+floor_control; k++){

                        if(controlo==0){ // alterar a coordenada x

                            cube = (float*)realloc(cube,(++tot)*sizeof(float));
                            cube[tot-1] = base[k] - (j*2);
                        }

                        else if(controlo==1){ // manter a coordenada y

                            cube = (float*)realloc(cube,(++tot)*sizeof(float));
                            cube[tot-1] = base[k];
                        }

                        else if(controlo==2){ // alterar a coordenada z

                            cube = (float*)realloc(cube,(++tot)*sizeof(float));
                            cube[tot-1] = base[k] - (i*2);
                            controlo = -1;
                        }

                        controlo++;
                    }

                    floor_control += 27;
                }

                floor_control = 0;

                for(k=0; k<tot; k++){

                    cube_coordinates = (float*)realloc(cube_coordinates,(++tot_coordinates)*sizeof(float));
                    cube_coordinates[tot_coordinates-1] = cube[k];
                    cube_colors = (float*)realloc(cube_colors,(++tot_colors)*sizeof(float));
                    cube_colors[tot_colors-1] = floor_color;
                }
                
                free(cube);
                cube = NULL;
                tot = 0;
            }

            else{ // buraco

                continue;
            }
        }
    }
}