#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;

void Random (int **a, int M)
{
    for (int i = 0; i < M; i++)
        for (int j = 0; j < M; j++)
        a[i][j] = (rand()%100) + 1;
} 
 
void Set (int **a, int M)
{
    for (int i = 0; i < M; i++)
        for (int j = 0; j < M; j++)
        cin >> a[i][j];
} 
 
int *Create (int **a, int M, int n)
{    
    int*b = new int[n], p=0;
    
    for (int i = 0; i < M; i++)
        for (int j = 0; j < M; j++)
        if (i + j <= M - 1) b[p++] = a[i][j];
        return b;
}

void Sort(int *b, int n)
{
    for (int i = 0; i < n - 1; i++)    
        for (int j = 0; j < n - i - 1; j++)        
            if (b[j] < b[j + 1]) swap(b[j], b[j + 1]);
}

void Modification (int **a, int M, int *b)
{
    int p=0;
    for (int i = 0; i < M; i++)
        for (int j = 0; j < M; j++)
        if (i + j <= M - 1) a[i][j]=b[p++];
        else a[i][j]*=-1;
}

void Print (int **a, int M)
{
    for (int i = 0; i < M; i++)
    {
        for (int j = 0; j < M; j++)       
        cout << setw(4) << a[i][j] << " ";        
    cout << "\n";
    }
} 

int main()
{
    int M, n, foo, *b;

    do {
        cin >> M;
    } while (M < 2 || M > 5);

    n = (M * M + M) / 2;
    int **a = new int*[M];
    for (int i = 0; i < M; i++) a[i] = new int[M];

    cin >> foo;
    if (foo == 1) Random(a, M);
    else Set(a, M);

    Print(a,M);
    cout << endl;
    b = Create(a, M, n);
    Sort(b, n);
    Modification(a, M, b);
    Print(a, M);  

}