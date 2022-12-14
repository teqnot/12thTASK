#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int M, N, col;
    char foo;
    
    while (true) {
        cin >> M;
        if ((M < 2) || (M > 5)) continue;
        else break;
    }

    int matr[M][M];
    cin >> foo;
    cin >> N;
    cin >> col;

    if (foo == 'r') {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) matr[i][j] = 1 + (rand() % 100);
    }
    else {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) cin >> matr[i][j];
    }

    for (int k = 0; k < M; k++) {
        for (int i = 0; i < M; i++) {
            for (int j = M - 1; j > i; j--) {
                if (matr[k][j] < matr[k][j - 1]) {
                    int buff = matr[k][j];
                    matr[k][j] = matr[k][j - 1];
                    matr[k][j - 1] = buff;
                }
            }
        }
    }

    cout << matr[col][N] << " <-" << endl;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            cout << matr[i][j] << " ";
        }
        cout << endl;
    }
}


// by: teqnot 
// under CC BY 4.0