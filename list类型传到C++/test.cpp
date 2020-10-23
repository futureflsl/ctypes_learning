
#include "stdio.h"
extern "C"{
    void show_matrix(double *matrix, int rows, int columns);
}
void show_matrix(double *matrix, int rows, int columns)
{
    int i, j;
	
    for (i=0; i<rows; i++) {
        for (j=0; j<columns; j++) 
            printf("matrix[%d][%d] = %.3lf ", i, j, matrix[i*columns+ j]);
        printf("\n");
    }
	
}

//g++ -fPIC -shared test.cpp -o test.so
