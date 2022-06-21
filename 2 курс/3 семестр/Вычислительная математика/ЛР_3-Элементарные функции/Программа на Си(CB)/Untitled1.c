#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <locale.h>
// Читает только первый символ (если введем 124, то прочитается "1")
char read_symbol()
{
	printf(">>>");
	char choice = (char)getchar();
	while (getchar() != '\n');
	return choice;
}
// Очистка консоли
void clear_console()
{
	system("cls");
}
// Главное меню
void print_menu()
{
	clear_console();
	printf("1. Многочленные приближения Чебышева\n");
	printf("2. Метод итераций\n");
	printf("3. Об авторе\n");
	printf("4. Выход\n");
}
// Вывод многочленного приближения
void print_polynomial_menu()
{
	clear_console();
	printf("1. Вычислить e^x\n");
	printf("2. Вычислить sin(x)\n");
	printf("3. Назад\n");
}
// Вывод метода итераций
void print_iteration_menu()
{
	clear_console();
	printf("1. Вычислить sqrt(x)\n");
	printf("2. Вычислить y = 1/sqrt(x)\n");
	printf("3. Назад\n");
}
// Вычисление exp
void computation_exp()
{
	double a[] = { 0.9999998, 1.0000000, 0.5000063, 0.1666674, 0.0416350, 0.0083298, 0.0014393, 0.0002040 };
	int k = 1;
	double e, x, C = a[0], U, P = 1;
	e = 2 * pow(10, -7);
	printf("Введите x, |x| <= 1\n");
	scanf("%lf", &x);
	x = fabs(x);
	do {
		P = P * x;
		U = P * a[k];
		C = C + U;
		if (k >= 7)
			break;
		else
			k++;
	} while (fabs(U) > e);
	printf("Результат = %lf \n", C);
	system("pause");
}
// вычисление sin
void computation_sin()
{
	double a[] = { 1.000000002, -0.166666589, 0.008333075, -0.000198107, 0.000002608 };
	int k = 1;
	double e, x, C, U, P = 1, pi = 3.14;
	printf("Введите x в градусах, |x| <= pi/2\n");
	scanf("%lf", &x);
	x = (pi * x) / 180;
	e = 6 * pow(10, -9);
	C = a[0] * x;
	do {
		P *= (x * x);
		U = P * a[k] * x;
		C += U;
		if (k >= 4)
			break;
		else
			k++;
	} while (fabs(U) > e);
	printf("Результат = %lf \n", C);
	system("pause");
}
// Подменю с многочленным приближением
void print_polynomial_step()
{
	while (1)
	{
		print_polynomial_menu();
		char choice = read_symbol();
		switch (choice)
		{
		case '1':
			clear_console();
			computation_exp();
			break;
		case '2':
			clear_console();
			computation_sin();
			break;
		case '3':
			return;
		}
	}
}
// Вычисление sqrt(x)
void computation_sqrt()
{
	double e, y_o, y, x, R;
	printf("Введите x \n");
	scanf("%lf", &x);
	printf("Введите y0 \n");
	scanf("%lf", &y_o);
	printf("Введите точность e \n");
	scanf("%lf", &e);
	printf("При x = %lf, y0 = %lf, e = %lf \n", x, y_o, e);
	R = 1;
	while (R > e)
	{
		y = (y_o + x / y_o) / 2;
		R = fabs(y - y_o);
		y_o = y;
	}
	printf("Результат = %lf \n", y);
	system("pause");
}
// Вычисление y = 1/sqrt(x)
void computation_y_sqrt()
{
	double e, y_o, y, x, R;
	printf("Введите x \n");
	scanf("%lf", &x);
	printf("Введите y0 \n");
	scanf("%lf", &y_o);
	printf("Введите точность e \n");
	scanf("%lf", &e);
	printf("При x = %lf, y0 = %lf, e = %lf \n", x, y_o, e);
	R = 1;
	while (R > e)
	{
		y = y_o / 2 * (3 - x * y_o * y_o);
		R = fabs(y - y_o);
		y_o = y;
	}
	printf("Результат = %lf \n", y);
	system("pause");
}
// Подменю с итерациями
void print_iteration_step()
{
	while (1)
	{
		print_iteration_menu();
		char choice = read_symbol();
		switch (choice)
		{
		case '1':
			clear_console();
			computation_sqrt();
			break;
		case '2':
			clear_console();
			computation_y_sqrt();
			break;
		case '3':
			return;
		}
	}
}

// Подменю об авторе
void about_author()
{
	clear_console();
	printf("Задание выполнил студент 2 курса ИВТ Войтенко Игорь\n");
	system("pause");
}

int main()
{
	setlocale(LC_ALL, "RUS");
	while (1)
	{
		print_menu();
		char choice = read_symbol();
		switch (choice)
		{
		case '1':
			print_polynomial_step();
			break;
		case '2':
			print_iteration_step();
			break;
		case '3':
			about_author();
			break;
		case '4':
			return 0;
		}
	}

	return 0;
}
