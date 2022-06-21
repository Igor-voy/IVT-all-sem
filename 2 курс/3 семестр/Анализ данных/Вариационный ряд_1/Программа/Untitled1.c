#include <stdlib.h>
#include <stdio.h>
#include <locale.h>
#include <math.h>

int main()
{
    setlocale(LC_ALL, "rus");
    int n, m;
    double min_v, max_v, h, k, len, h_1;
    printf("Введите объем выборки \n");
    scanf("%d", &n);
    double a[n];
    printf("Выборка \n");
    for(int i = 0 ; i < n; i++)
    {
        scanf("%lf", &a[i]);
    }
    system("cls");
    min_v = a[0];
    for(int i = 0; i < n; i++)
    {
        if(a[i] < min_v)
        {
            min_v = a[i];
        }
    }
    max_v = a[0];
    for(int i = 0; i < n; i++)
    {
        if(a[i] > max_v)
        {
            max_v = a[i];
        }
    }
    k = 1.0 + 3.322*log10(n);
    len = (max_v - min_v)/k;
    h = min_v - 0.5;
    printf("Интервалы: \n");
    while(h < max_v + 1.0)
    {
        m = 0;
        h_1 = h + len;
        for(int i = 0; i < n; i++)
        {
            if((h < a[i]) && (a[i] < h_1))
            {
                m++;
            }
        }
        printf("[ %lf ; %lf ) \t Частота варианты = %d\n", h, h_1, m);
        h = h_1;
    }
    system("pause");
}

