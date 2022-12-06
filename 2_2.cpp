#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int M, N, row;
    char foo;
    
    while (true) {
        cin >> M;
        if ((M < 2) || (M > 5)) continue;
        else break;
    }

    int matr[M][M];
    cin >> foo;
    cin >> N;
    cin >> row;

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
                if (matr[j][k] > matr[j - 1][k]) {
                    int buff = matr[j][k];
                    matr[j][k] = matr[j - 1][k];
                    matr[j - 1][k] = buff;
                }
            }
        }
    }

    cout << matr[row][N] << " <-" << endl;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            cout << matr[i][j] << " ";
        }
        cout << endl;
    }
}