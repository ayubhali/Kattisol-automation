#include <stdio.h>

int main()
{
    double footballfield = 0.09144;
    int num;
    double result;

    scanf("%d", &num);

    result = num * footballfield;

    printf("%.5f", result);

    return 0;
}