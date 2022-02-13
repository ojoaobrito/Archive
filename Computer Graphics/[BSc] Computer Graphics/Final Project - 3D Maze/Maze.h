#include <string>

typedef struct{ // define uma célula do labirinto, num dado instante

    int line;
    int column;

} Cell;

using namespace std;

/* estes "if" servem de garantia, a declaração e definição desta classe só é feita uma vez */
#ifndef MAZE_H
#define MAZE_H

class Maze{

    public:
    int size; // tamanho do labirinto (size*size)
    int initial_cell = 0; // ponto de entrada do labirinto
    int final_cell = 0; // ponto de saída do labirinto
    int tot_coordinates = 0; // número de coordenadas OpenGL
    int tot_colors = 0; // número de cores
    float *cube_coordinates = NULL; // coordenadas dos blocos que compõem o labirinto
    float *cube_colors = NULL; // cor dos blocos do labirinto

    private:
    char ***maze = NULL; // representação interna do futuro labirinto
    int **aux_matrix = NULL; // 1 - célula ainda não foi visitada; 0 - célula já foi visitada
    Cell* path = NULL; // rota feita no curso da geração do labirinto
    char **matrix = NULL; // matriz que representa o labirinto, mas com blocos

    // variáveis auxiliares
    int tot = 0;
    int tot_options = 0;

    public:
    Maze(int size_in); // construtor
    void build_maze(int inicio); // método recursivo que constrói o labirinto
    Cell* movement_options(Cell atual); // método auxiliar, devolve as opções de movimento para uma dada célula
    void print_maze(); // método auxiliar, imprime o labirinto
    void save_maze(); // método auxiliar, guarda o labirinto, na representação por blocos, num ficheiro
    void build_maze_matrix(float frequencia); // método auxiliar, constrói o equivalente ao labirinto na forma de matriz (com blocos)
    int all_visited(); // método auxiliar, verifica se todas as células do labirinto já foram visitadas ou não
    void maze_coordinates(); // método que calcula as coordenadas OpenGL para os elementos do labirinto
};

#endif