#include <stdio.h>

int main()
{
    int improvements;
    int numimprovyearly;

    scanf_s("%d\n%d",&improvements,&numimprovyearly);

    int temp = (improvements / numimprovyearly);

    int year = 2022 + temp;

    printf("%d", year);

    return 0;
}