#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

float f(float x, float y){
    return y*(1-x);
}

int main(){
    setlocale(LC_ALL, "rus");
    float a, b, n, x, y, h, k1, k2, k3, k4, dy;
    printf("¬ведите левый предел: ");
    scanf("%f", &a);
    printf("¬ведите правый предел: ");
    scanf("%f", &b);
    printf("¬ведите количество разбиений: ");
    scanf("%f", &n);
    printf("¬ведите x: ");
    scanf("%f", &x);
    printf("¬ведите y: ");
    scanf("%f", &y);
    h = (b-a)/n;
    while(x < b){
        k1 = f(x, y);
        k2 = f(x+h/2, y+h*k1/2);
        k3 = f(x+h/2, y+h*k2/2);
        k4 = f(x+h, y+h*k3);
        dy = h/6*(k1+2*k2+2*k3+k4);
        y += dy;
        printf("x = %f \t y = %f \n", x, y);
        x +=h;
    }
    return 0;
}
