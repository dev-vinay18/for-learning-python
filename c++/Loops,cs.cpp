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

int main()  {                                       // Q. for gatting grade A,B,C .
    int marks;
    cout << "enter marks :";
    cin >> marks;

    if(marks >= 90)  {
        cout << "A\n";
    } else if (marks >= 80 && marks <90) {
        cout << "B\n";
    } else {
        cout << "C\n";
    }

    return 0;
}




