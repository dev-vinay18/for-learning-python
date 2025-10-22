#include<iostream>
using namespace std;

// int Nfactorial(int n) {
//     int SumN = 1;

//     for(int i= 1;i <= n;i++){
//         SumN *= i; 
//     }
//     return SumN;
// }

// int main() {

//     cout << Nfactorial(7) << endl;
//     return 0;
// }

// int minN(int a,int b){
    
//     if(a < b){
//         return a;
//     }else {
//         return b;
//     }
    
// }

// int main() {
//     cout << minN(5,7) << endl;
// }

// int SumofdDigit (int num){
//     int DigitSum = 0;

//     while(num > 0){
//         int LastDigit = num % 10;
//         num /= 10 ;

//         DigitSum += LastDigit;
//     }
//     return DigitSum;
// }

// int main (){
//     cout << SumofdDigit(2345) << endl;
// }

int factorial(int n){

    int facN = 1;
    for (int i = 1;i <= n;i++){
        facN *= i;
    }
    return facN;
}

int nCr(int n ,int r){

    int fac_n = factorial(n);
    int fac_r = factorial(r);
    int fac_nmr = factorial(n-r);

    return fac_n / (fac_r * fac_nmr);

}

int main (){
    int n = 8, r = 2;
    cout << nCr(n,r) << endl;
}