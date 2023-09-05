#include <stdio.h>

/**
main - A program that perform the addition of matrix
Return - 0 for sucess else for failure
*/

int main(void)
{
    int rows, cols, i, j;
    int matrix_A[rows][cols], matrix_B[rows][columns], sum[rows][cols];

    printf("Addition of matrix must be same order.\n");

    printf("Enter the number of rows for matrix 'A' and  matrix 'B'.\n");
    scanf("%d", &rows);
    printf("Enter the number of columns for matrix 'A' and matrix 'B'.\n");
    scanf("%d", %cols);

    printf("Enter the elements of matrix 'A':\n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
            scanf("%d", matrix_A[i][j]); 
    }

    printf("Enter the elements of matrix 'B':\n");
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
            scanf("%d", matrix_B[i][j]); 
    }

    /* Adding the matrices*/
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
            sum[i][j] = matrix_A[i][j] + matrix_B[i][j];
    }

    /* Displaying the result of the addition*/

    printf("Result of addition\n")
    for (i = 0; i < rows; i++)
    {
        for (j = 0; j < cols; j++)
        {
            printf("%d", sum[i][j]);
        }
        putchar(10);  
    }

    return (0);

}