#include <iostream>
using namespace std;

/* Function prototypes */
int combinations(int n, int k);
int fact(int n);

/* Main program */
int main(){
    int n, k;
    cout << "Enter the number of objections n:";
    cin >> n;
    cout << "Enter the number to be chosen k:";
    cin >> k;
    cout << "C(n,k) = " << combinations(n, k) << endl;
    return 0;
}

/* Function definitions */
int combinations(int n, int k){
    return fact(n) / (fact(n - k) * fact(k));
}

int fact(int n){
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}