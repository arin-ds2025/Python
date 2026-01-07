#include<bits/stdc++.h>
using namespace std;

int fib(short x){
    if(x<=1) return x;
    else return fib(x-2) + fib(x-1);
}

int main(){
    for(short i = 0; i<10; i++){
        cout<<fib(i)<<"  ";
    }
}
