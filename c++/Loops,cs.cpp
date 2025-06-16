#include <iostream>
using namespace std;

// int main() {                                    // conditional statements.  Q. For finding even and odd number
//     int n;
//     cout << "enter number :" ;
//     cin >> n;

//     if ( n%2 == 0 ) {
//         cout << "even number\n";
//     } else {
//         cout << "odd number\n";
//     }
//     return 0;
// } 

// int main()  {                                       // Q. for gatting grade A,B,C .
//     int marks;
//     cout << "enter marks :";
//     cin >> marks;

//     if(marks >= 90)  {
//         cout << "A\n";
//     } else if (marks >= 80 && marks <90) {
//         cout << "B\n";
//     } else {
//         cout << "C\n";
//     }

//     return 0;
// }

// int main() {                                            // find char lowercase or uppercase
//     char ch;
//     cout << "enter ch : ";
//     cin >> ch;

//     if(ch >= 'a' && ch <= 'z') {
//         cout << "lowercase\n";
//     } else {
//         cout << "uppercase\n";
//     }
//     returnn 0;
// }

// int main(){                                                 // Ternary Operator / statements      Q is find the number is positive or negative.      
//     int n = 23;

//     cout << (n >= 0 ? "positive" : "negative") << endl;
//     return 0;

// } 

// int main() {                                                    // while loop (for counting numbers to n.)
//     int n = 10;
//     int count = 1;

//     while (count <= n ) {
//         cout << count << " ";
//         count++;
//     }
//     cout << endl;
//     return 0;

// }

// int main() {                                                        // for finding odd or even for n.
//     int n ;
//     cout << "number :";
//     cin >> n;

//     if(n%2 == 0) {
//         cout << "even number";
//     } else {
//         cout << "odd number";
//     }
//     cout << endl;
// }

// int main() {                                                // for finding largest out of 3 numbers
//     int A,B,C;
    // cout << "enter A :";
    // cin >> A;
    // cout << "enter B :";
    // cin >> B;
    // cout << "enter C :";
    // cin >> C;
//     cout << "Enter three numbers: ";
//     cin >> A >> B >> C;

//     if((A >= B) && (A >= C)) {
//         cout << A;
//     }else if ((B >= A) && (B >= C)){
//         cout << B;
//     }else {
//         cout << C;
//     }
//     cout << endl;
// }

// int main() {                                 // using for loop for finding n numbers
//     int n = 1000;

//     for(int i = 1 ; i <= n ; i++) {
//         cout << i << " ";
//     }
//     cout << endl;
//     return 0;
// }

// int main() {                                    // sum of numbers from 1 to n
//     int n = 10;
//     int sum = 0;

//     for(int i = 1 ; i <= n; i++){
//         sum += i;
//     }
//     cout << "total sum : " << sum << endl;
//     return 0;

// }

// int main() {                                        // sum of numbers from 1 to n by using for loop
//     int n = 3;
//     int sum = 0;
//     int i = 1;

//     while (i <= n){
//         sum += i;
//         i++;
//     }
//     cout << "total sum : " << sum << endl;
//     return 0;
// }

// int main() {                                        // use of Break key woard.
//     int n = 7;
//     int sum = 0;
//     int i = 1;

//     while (i <= n){
//         sum += i;
//         i++;
//         if (i == 2){
//             break;
//         }
//     }
//     cout << "total sum : " << sum << endl;
//     return 0;
// }

// int main(){                                              // sum of odd number.
//     int n = 9;
    // int sum = 0;

//     for( int i = 1; i <= n; i++){
//         if(i%2 != 0){
//             cout << i << " ";
//         }
//     }
//     cout << endl;
//     return 0;
// }

// int main (){                                                // by diff method
//     int n = 9;

//     for( int i = 1; i <= n; i += 2){
//         cout << i << " ";
//     }
//     cout << endl;
//     return 0;

// int main() {
//     int n = 21;
//     int oddsum = 0;

//     for( int i =1 ; i <= n ; i++ ){
//         if(i%2 != 0){
//         oddsum += i ;
//         }
//     }
//     cout << oddsum << endl;
// } 

// int main() {
//     int n = 100;
//     int oddsum = 0;
//     int i = 1;

//     while ( i <= n ){
//         if(i%2 != 0){
//             oddsum += i;
//         }
//         i++;
//     }
//     cout << oddsum << endl ;
    
//     return 0;
    
// }

// int main () {                                            // Do while loop example Q.

//     int n = 10;
//     int i = 1;

//     do {
//         cout << i << " ";
//         i++;
//     }while(i <= n);

//     cout << endl;
//     return 0;
// }

// int main () {                                           // Q.check no. is prime or not by for loop  (Most important logic)
//     int n = 45;
//     bool isPrime = true ;

//     for (int i = 2; i<=n-1 ; i++){
//         if(n%i == 0){
//             isPrime = false;
//             break;
//         }
//     }
//     if(isPrime == true){
//         cout << "prime no." << endl;
//     } else {
//         cout <<"non prime no." <<endl;
//     }
    
//     return 0;
// }

// int main(){
//     int n = 67;
//     bool isPrime = true;

//     for (int i = 2; i*i <= n ; i++){
//         if(i%n == 0){
//             isPrime = false;
//             break;
//         }
//     }
    
//     if(isPrime == true){
//         cout << "Prime no.\n";
//     }else {
//         cout << "Non prime no.\n";
//     }
// }

// int main() {                                                // sum of all numbers from 1 to n which are divisible by 3.
//     int n =37;

//     for (int i = 1; i <= n; i++ ){
//         if(i%3 == 0){
//             cout << i << " ";
//         }
//     }
//     cout << endl;
//     return 0;
// }

// int main() {                                            // print factorial of a number N.
//     int n = 5;
//     int sum = 1;
    
//     for(int i = 1 ; i <= n ; i++ ) {
//         sum *= i ;
//     }

//     cout << sum << endl ;
//     return 0;
// }
 
 int main() {
    int n = 5;
    for (int i = 1 ; i <= n ; i++ ){
        int m = 5;
        for (int j = 1 ; j <= m; j++){
            cout << "*";
        }
        cout << endl; 
    }
    return 0;
 }