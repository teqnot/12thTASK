#include <iostream>
#include <bits/stdc++.h>
#include <cmath>

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

    for (int i = 0; i < M - 1; i++){
        for (int j = i + 1; j < M; j++) {
            if (matr[j][M - 1 - j] < matr[i][M - 1 - i]) {
                swap(matr[i][M - 1 - i], matr[j][M - 1 - j]);
            }
        }
    }

    for (int i = 0; i < M; i++) {
        for (int j = M - 1; j >= 0; j--) {
            if (i + j != M - 1) matr[i][j] *= -1;
        }
    }

    cout << matr[abs(M - N)][N - 1] << endl;

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) {
            cout << matr[i][j] << " ";
        }
        cout << endl;
    }

}
