#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <locale.h>

int main() {
  setlocale(LC_ALL, "rus");
  float a = 0, b = 1, x0 = 0, y0 = 1, h, x = 0, y = 0;
  h = (b-a)/10;
  printf("¬ведите x0 \n");
  scanf("%f", &x0);
  printf("¬ведите y0 \n");
  scanf("%f", &y0);
  y = y0;
  while(x < b-h){
    y = y + h*(y*(1-x));
    printf("x = %.1f \t", x);
    printf("y = %f \t\n", y);
    x = x + h;
  }
  return 0;
}
