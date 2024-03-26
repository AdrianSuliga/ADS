#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void radix_sort(int T[], int n)
{
    int *B;
    int *C;

    B = malloc(sizeof(int) * n);
    C = malloc(sizeof(int) * n);

    for (int i = 0; i < n; i++)
    {
        C[i] = 0;
        B[i] = 0;
    }

    for (int i = 0; i < n; i++)
        C[T[i] % n]++;
    for (int i = 1; i < n; i++)
        C[i] += C[i - 1];

    for (int i = n - 1; i > -1; i--)
    {
        B[C[T[i] % n] - 1] = T[i];
        C[T[i] % n]--;
    }

    for (int i = 0; i < n; i++)
        C[i] = 0;

    for (int i = 0; i < n; i++)
        C[T[i] / n]++;
    for (int i = 1; i < n; i++)
        C[i] += C[i - 1];

    for (int i = n - 1; i > -1; i--)
    {
        T[C[B[i] / n] - 1] = B[i];
        C[B[i] / n]--;
    }
}

int main()
{
    int n = 0;
    printf("n=");
    scanf("%d", &n);

    int *T;
    T = malloc(sizeof(int) * n);

    srand(time(NULL));

    for (int i = 0; i < n; i++)
        T[i] = rand() % (n*n - 1) + 1;

    clock_t start = clock();
    radix_sort(T, n);
    clock_t end = clock();

    printf("Measured time: %lf\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}