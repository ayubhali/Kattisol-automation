#include <stdio.h>

int main()
{

    int a;
    int b;
    int c;

    scanf_s("%d\n%d\n%d",&a, &b, &c);

    int min_time = c - a - b;

    printf("%d", min_time);

    return 0;
}