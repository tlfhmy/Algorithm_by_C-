#include <iostream>
#include <random>
#include <time.h>
using namespace std;

int main()
{
    int n = 6;
    int p[] = {31, 41, 59, 26, 41, 58};
    srand(time(NULL));

    for (int i = 1; i < n; i++)
    {
        cout << "\n";
        for (int i = 0; i < n; i++)
        {
            cout << p[i] << " ";
        }
        cout << "\n";
        int key = p[i];
        int j = i - 1;
        while (j > -1 & p[j] > key)
        {
            p[j + 1] = p[j];
            j -= 1;
        }
        p[j + 1] = key;
    }
}