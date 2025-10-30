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

// int factorial(int n){

//     int facN = 1;
//     for (int i = 1;i <= n;i++){
//         facN *= i;
//     }
//     return facN;
// }

// int nCr(int n ,int r){

//     int fac_n = factorial(n);
//     int fac_r = factorial(r);
//     int fac_nmr = factorial(n-r);

//     return fac_n / (fac_r * fac_nmr);

// }

// int main (){
//     int n = 8, r = 2;
//     cout << nCr(n,r) << endl;
// }

// int primenum(int n){
//     bool isprime = true ;

//     for (int i = 2; i < n-1;i++){
//         if(n % i == 0){
//             isprime = false;
//             break;
//         }
//         // return 0;
//     }
//     if(isprime == false){
//         cout << "non prime\n ";
//     }else{
//         cout << "prime\n";
//     }
//     return 0;
// }

// int main(){
    
//     cout << primenum(67) << endl;
// }

// int primenum(int n){
//     bool Isprime = true;

//     for (int i = 2;i < n-1;i++){
//         if(n % i == 0){
//             Isprime = false;
//             break;
//         }
//     }

//     if(Isprime == true){
//         cout << n << " " ;
//     }

//     // cout << endl;
//     return 0;
// }
// int nthprimenums (int n){

//     for(int i = 2; i <= n; i++ ){
//         primenum(i);
//         // return i;
//     }
//     cout << endl;
//     return 0 ;
    
// }

// int main (){
//     cout << nthprimenums(56) << endl;
// }

// int nthfibo(int n){
    
//     int a = 0,b = 1,next;

//     if(n == 0){
//         cout << a;
//     }else if (n == 1){
//         cout << b;
//     }else{
//         for(int i = 2;i <= n ;i++){
//             next = a + b ;
//             a = b;
//             b = next;

            
//         }
//         cout << b;
//         cout << endl;
//     }
//     return 0;
// }

// int main(){
//     cout << nthfibo(6) <<endl;
// }

// int decToBinary(int decnum){                                     // decimal to binary
//     int ans = 0, power = 1;

//     while(decnum > 0){
//         int rem = decnum % 2;
//         decnum /= 2;

//         ans += (rem * power);
//         power *= 10;
//     }
//     return ans;
// }

// int main(){
//     // cout << decToBinary(89) << endl;
//     // cout << decToBinary(335) << endl;

//     for(int i = 1;i <= 10;i++){
//         cout << decToBinary(i) << endl;

//     }
// }

int binToDec(int binnum){
    int ans = 0,power = 1;

    while (binnum > 0)
    {
        int rem = binnum % 10;
        ans += (rem * power);

        binnum /= 10;
        power *= 2;
    }
    return ans;
    
}

int main(){
    cout << binToDec(101) << endl;
}