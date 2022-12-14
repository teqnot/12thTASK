#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

bool prime(long long n){ 
	for(long long i=2;i<=sqrt(n);i++)
		if(n%i==0)
			return false;
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
            if (prime(matrix[i][j])) arr.push_back(matrix[i][j]);
        }
        cout << "\n";
    }

    sort(arr.begin(), arr.end(), greater<int>());
    for (int i = 0; i < arr.size(); i++) cout << arr[i] << " ";
}


// by: teqnot
// under CC BY 4.0