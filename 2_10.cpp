#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

int main()
{
    int M, buff;
    char foo;
    vector<int> arr1;
    vector<int> arr2;
    
    while (true) {
        cin >> M;
        if ((M < 2) || (M > 5)) continue;
        else break;
    }

    int matr[M][M];
    cin >> foo;

    if (foo == 'r') {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) matr[i][j] = 1 + (rand() % 100);
    }
    else {
        for (int i = 0; i < M; i++)
            for (int j = 0; j < M; j++) cin >> matr[i][j];
    }

    for (int i = 0; i < M; i++) {
        for (int j = 0; j < M; j++) cout << matr[i][j] << " ";
        cout << endl;
    }
    cout << endl;

    for (int i = 0; i < M; i++) {
        buff = 0;
        for (int j = 0; j < M; j++) {
            buff += matr[i][j];
        }
        arr1.push_back(buff);
    }

    for (int i = 0; i < M; i++) {
        buff = 0;
        for (int j = 0; j < M; j++) {
            buff += matr[j][i];
        }
        arr2.push_back(buff);
    } 

    sort(arr1.begin(), arr1.end(), greater<int>());
    sort(arr2.begin(), arr2.end());
    arr1.insert(arr1.end(), arr2.begin(), arr2.end());
    for (int i = 0; i < arr1.size(); i++) cout << arr1[i] << " ";
}


// by: teqnot 
// under CC BY 4.0