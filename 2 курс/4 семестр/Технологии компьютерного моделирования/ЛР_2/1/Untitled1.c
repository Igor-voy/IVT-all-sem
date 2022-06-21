#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "rus");
    float T = 83, Ts = 22, r = 0.003, t, h;
    int n;
    printf("Введите количество разбиений \n");
    scanf("%d", &n);
    h = (Ts-T)/n;
    while(T > Ts){
        t = t+h*((-r)*(T-Ts));
        T +=h;
        printf("t = %f \t", t);
        printf("T = %f \n", T);
    }
    return 0;
}
