#include <iostream>
#include <random>
#include <time.h>

using namespace std;

int RightSon(int i){
    return 2*i + 2;
}
int LeftSon(int i){
    return 2*i + 1;
}
int Parent(int i){
    return (i-1)/2;
}

void Max_Heap_Maintence(int *p,int size, int i){
    int l = LeftSon(i);
    int r = RightSon(i);
    int largest = i;
    if(l <= size-1 && p[l] > p[i]){
        largest = l;
    }
    else{
        largest = i;
    }
    if(r <= size-1 && p[r] > p[largest]){
        largest = r;
    }
    if(largest != i){
        int tmp = p[i];
        p[i] = p[largest];
        p[largest] = tmp;
        Max_Heap_Maintence(p, size, largest);
    }
}

void Build_Max_Heap(int *p, int size){
    for(int i = (size)/2-1; i >= 0; i--){
        Max_Heap_Maintence(p, size, i);
    }
}

void Heap_Sort(int *p, int size){
    Build_Max_Heap(p,size);
    for(int i = size-1; i >= 0; i--){
        int tmp = p[0];
        p[0] = p[i];
        p[i] = tmp;
        Max_Heap_Maintence(p, i, 0);
    }
}

int main()
{
    int n = 0;
    cout << "Please enter the number of random numbers:";
    cin >> n;
    srand(time(NULL));
    int *a = new int[n];
    for(int i = 0; i < n; i++){
        a[i] = rand()%n;
    }
    Heap_Sort(a,n);
    for(int i=0; i<n;i++){
        cout << a[i] << " ";
    }
    return 0;
}