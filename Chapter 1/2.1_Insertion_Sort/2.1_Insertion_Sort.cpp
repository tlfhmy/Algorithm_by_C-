#include <iostream>
#include <random>
#include <time.h>
using namespace std;

int main()
{
    int n = 0;
    cout << "Please enter number of random numbers:";
    cin >> n;
    int *p = new int[n];
    srand(time(NULL));
    for(int i=0; i < n; i++){
        p[i] = rand() % (2*n);
    }

    cout << "\n";
    for(int i = 0; i < n; i++){
        cout << p[i] << " ";
    }
    cout << "\n";

    for(int i = 1; i < n; i++){
        int key = p[i];
        int j = i - 1;
        while(j > -1 && p[j] > key){
            p[j+1] = p[j];
            j -= 1;
        }
        p[j+1] = key;
    }

    cout << "\n";
    for(int i = 0; i < n; i++){
        cout << p[i] << " ";
    }
    cout << "\n";
}