#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int M, N;
    char foo;
    
    while (true) {
        cin >> M;
        if ((M < 2) || (M > 5)) continue;
        else break;
    }

    int matr[M][M];
    cin >> foo;
    cin >> N;

    if (foo == 'r') {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) matr[i][j] = 1 + (rand() % 100);
    }
    else {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) cin >> matr[i][j];
    }

    for (int i = 1; i < M; i++){
        for (int i = 1; i < M; i++) {
            if (matr[i-1][i-1] > matr[i][i]) {
                int buff = matr[i][i];
                matr[i][i] = matr[i - 1][i -1];
                matr[i - 1][i - 1] = buff;
            }
        }
    }

    cout << matr[N][N] << endl << endl;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            if (j != i) matr[i][j] *= -1;
            cout << matr[i][j] << " ";
        }
        cout << endl;
    }

}