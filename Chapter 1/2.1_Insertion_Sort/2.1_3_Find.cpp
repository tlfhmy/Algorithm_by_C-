#include <iostream>
#include <random>
#include <time.h>

using namespace std;

int main()
{
    cout << "Please enter the number of random numbers" << endl;
    int n(0);

    cin >> n;

    int *p = new int[n];
    
    srand(time(NULL));

    for(int i=0; i < n; i++){
        p[i] = rand() % (2*n);
    }

    cout << "Array generatted:" << endl;
    for(int i = 0; i < n; i++){
        cout << p[i] << " ";
    }
    cout << endl;

    int m(0);
    cout << "Please enter the number you want to find: ";
    cin >> m;

    bool Found = false;
    int index = 0;

    for(int i = 0; i < n; i++){
        if(p[i] == m){
            index = i;
            Found = true;
            break;
        }
    }

    if(Found){
        cout << "Element " << m << " found in Array as index " << index << endl;
    }
    else{
        cout << "Element " << m << " is not found in Array." << endl;
    }

    return 0;
}