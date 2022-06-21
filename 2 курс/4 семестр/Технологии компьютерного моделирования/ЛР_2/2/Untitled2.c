#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "rus");
    float R = 50, E = 300, L = 30, I = 0, t = 0, h;
    printf("¬ведите шаг \n");
    scanf("%f", &h);
    while(I < 1){
        t = t+h*(L/(E-R*I));
        I +=h;
        printf("t = %.4f \t", t);
        printf("T = %.4f \n", I);
    }
    return 0;
}
