#include <iostream>
#include <conio.h>
#include <stdlib.h>

using namespace std;

int main()
{
    int N;
    char foo;
     while (true) {
        cin >> N;
        if ((N < 2) || (N > 5)) continue;
        else break;
    }
    int** ppX = new int*[N];

    cin >> foo;

    if (foo != 'r') {
        for (int i = 0; i < N; i++)
        {
            ppX[i] = new int[N];
            for (int j = 0; j < N; j++)
                cin >> ppX[i][j];
        }
    }
    else {
        for (int i = 0; i < N; i++)
        {
            ppX[i] = new int[N];
            for (int j = 0; j < N; j++)
                ppX[i][j] = (rand() % (100)) + 1;
        }
    }
    
 
    for (int z1 = 0; z1 < N; z1++)
    {
        for (int z2 = 0; z2 < N; z2++)
            printf("%d ",ppX[z1][z2]);
        printf("\n");
    }
 
    printf("\n");

 
    int d = 0, *pV = new int[N * N];
    for (int q1 = 0; q1 < N; q1++)
        for (int q2 = 0; q2 < N; q2++)
            pV[d++] = ppX[q1][q2];
 
    for (int m1 = 0; m1 < N * N; m1++)
        for (int m2 = m1; m2 < N * N; m2++)
            if (pV[m2] > pV[m1]) {
                int temp = pV[m1];
                pV[m1] = pV[m2];
                pV[m2] = temp;
            }
 
    int x1 = 0, x2 = 0;
    for (int n1 = 0; n1 < N * N; n1++)
    {
        if (x2 >= N) { x2 = 0; x1++; }
        ppX[x1][x2++] = pV[n1];
    }
 
    for (int r1 = 0; r1 < N; r1++)
    {
        for (int r2 = 0; r2 < N; r2++)
            printf("%d ",ppX[r1][r2]);
        printf("\n");
    }
 
    return 0;
}


// by: teqnot 
// under CC BY 4.0