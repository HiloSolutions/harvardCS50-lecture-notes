#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;
    do
    {
        start = get_int("Start population: \n");
    }
    while (start < 9);

    // TODO: Prompt for end size
    int end;
    do
    {
        end = get_int("End population: \n");
    }
    while (end < start);

    // TODO: Calculate number of years until we reach threshold
    int years = 0;
    int current = start;
    while (current < end)
    {
        current = current + (current / 3) - (current / 4);
        years++;
    }
    // TODO: Print number of years
    printf("Start size: %d\n", start);
    printf("End Size: %d\n", end);
    printf("Years: %d\n", years);
}