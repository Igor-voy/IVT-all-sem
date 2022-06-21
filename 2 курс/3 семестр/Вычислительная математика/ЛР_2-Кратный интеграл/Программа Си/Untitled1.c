#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>
#define pi 3.14
#define a 0
#define b pi/2
#define c 0
#define d pi/4

int main()
{
    setlocale(LC_ALL, "rus");
    int nx, ny;
    double hx, hy, sx, sy, x, y, Iy, Ix;
    printf("Введите количество разбиений по Ox \n");
    scanf("%d", &nx);
    printf("Введите количество разбиений по Oy \n");
    scanf("%d", &ny);
    hy = (d-c)/ny;
    hx = (b-a)/nx;
    printf("Шаг по Oy: %lf \n", hy);
    printf("Шаг по Ox: %lf \n", hx);
    sx = 0.0;
    sy = 0.0;
    x = a;
    Iy = 0.0;
    Ix = 0.0;
    while(x <= b-hx)
    {
        y = c;
        sy = 0;
        while(y <=d-hy)
        {
            sy+=fabs(sin(x+y));
            y+=hy;
        }
        Iy = hy*sy;
        sx+=Iy;
        x+=hx;
    }
    Ix = hx*sx;
    printf("I = %lf \n", Ix);
    system("pause");
    return 0;
}
