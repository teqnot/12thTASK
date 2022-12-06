#include <iostream>
#include <bits/stdc++.h>
#include <vector>

using namespace std;

void quicksort(int *mas, int first, int last)
{
    int mid, count;
    int f = first, l = last;
    mid = mas[(f + l) / 2]; //вычисление опорного элемента
    do
    {
        while (mas[f]<mid) f++;
        while (mas[l]>mid) l--;
        if (f <= l) //перестановка элементов
        {
            count = mas[f];
            mas[f] = mas[l];
            mas[l] = count;
            f++;
            l--;
        }
    } while (f<l);
    if (first<l) quicksort(mas, first, l);
    if (f<last) quicksort(mas, f, last);
}

int main()
{
    int board[8][8];
    char ans;
    vector<int> arr;
    int mas[32];

    cin >> ans;

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            board[i][j] = 1 + (rand() % 100);
        }
    }

    for (int i = 0; i < 8; i++) {
        for (int j = 0; j < 8; j++) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }

    if (ans == 'b') {
        for (int i = 0; i < 8; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < 8; j++) {
                    if (j % 2 != 0) arr.push_back(board[i][j]);
                }
            }
            else {
                for (int k = 0; k < 8; k++) {
                    if (k % 2 == 0) arr.push_back(board[i][k]);
                }
            }
        }
    }

    if (ans == 'w') {
        for (int i = 0; i < 8; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < 8; j++) {
                    if (j % 2 == 0) arr.push_back(board[i][j]);
                }
            }
            else {
                for (int k = 0; k < 8; k++) {
                    if (k % 2 != 0) arr.push_back(board[i][k]);
                }
            }
        }
    }

    for (int i = 0; i < 32; i++) mas[i] = arr[i];
    quicksort(mas, 0, 31);

    for (int i = 0; i < 32; i++) cout << mas[i] << endl;
}