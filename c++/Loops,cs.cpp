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
// }

// int main(){                                                 // Ternary Operator / statements
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

int main() {                                                // for finding largest out of 3 numbers
    int A,B,C;
    cout << "enter A :";
    cin >> A;
    cout << "enter B :";
    cin >> B;
    cout << "enter C :";
    cin >> C;

    if((A >= B) && (A >= C)) {
        cout << A;
    }else if ((B >= A) && (B >= C)){
        cout << B;
    }else {
        cout << C;
    }
    cout << endl;
}

