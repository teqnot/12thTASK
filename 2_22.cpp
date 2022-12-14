#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool fib(int n){ 
    int y = 1, z = 1, b = 1;
	for (int i = 0; i <= n; i++){   
        z = y; 
        y = b;
        b = z + y;
        if (b == n) return false;
    }
    return true;
}

int main()
{
    int matrix[4][4];
    vector <int> arr;
    string foo;
    cin >> foo;

    if (foo == "r") {
        for (auto &i : matrix) {
            for (int & j : i) {
                j = rand() % 100 + 1;
            }
        }
    }
    else {
        for (int i = 0; i < 4; i++) 
            for (int j = 0; j < 4; j++) cin >> matrix[i][j];
    }

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << matrix[i][j] << " ";
            if (fib(matrix[i][j]) && matrix[i][j] != 0 && matrix[i][j] != 1) arr.push_back(matrix[i][j]);
        }
        cout << "\n";
    }

    cout << "\n";

    sort(arr.begin(), arr.end(), greater<int>());
    for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
}