#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height, row, col, space;
    do
    {
        height = get_int("Enter height here:  ");
    }
    while (height < 1 || height > 8);

    for (row = 0; row < height ; row++)
    {
        for (space = 0; space < height - row - 1; space++)
        {
            printf(" ");
        }
        for (col = 0; col <= row ; col++)
        {
            printf("#");
        }
        printf("\n");
    }
}

