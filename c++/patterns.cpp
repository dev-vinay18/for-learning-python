#include<iostream>
using namespace std;

// int main(){                                         // square pattern
//     int n = 3;
//     int num =1;

//     for(int i = 0; i < n; i++){
//         for(int j = 0;j < n; j++){
//             cout << num << " ";
//             num++;
//         }    
//         cout << "\n";
//     }
    
//     return 0;
// }

// int main(){
//     int n = 3;
//     char ch = 'A';
//     int valuech = 0;

//     for(int i = 0; i < n; i++){
//         for(int j = 0; j < n; j++){
//             char currentchar = ch + valuech;
//             cout <<currentchar << " ";
//             valuech++;
            
//         }
//         cout << endl;
//     }
//     return 0;
// }

// int main(){
//     int n = 3;
//     char ch = 'A';
//     int h = 0;

//     for(int i= 0;i < n; i++){
//         for(int j = 0;j < n; j++){
//             // char ch = ch + 1;
//             char ne = ch + h;
//             cout << ne << " " ;
//             h++;
            
//         }
//         cout << '\n';
//     }

// }

// int main() {
//     int n = 4;

//     for(int i = 0;i < n ;i++){
//         for (int j = 0;j < i+1;j++){
//             cout << "* ";
//         }
//         cout << endl;
//     }
//     return 0;
// }

// int main () {                                                // question for practice.
//     int n = 4;
//     // char ch = '1';
//     // int t = 1;

//     for(int i = 1;i <= n;i++){
//         for(int j = 1;j <= n;j++){
//             // int t = 1;
//             cout << j << " ";
//             // t++;
//         }
//         cout << endl;
//     }
//     return 0;
// }

// int main () {
//     int n = 4;

//     for(int i = 0;i < n;i++){
//         for(int j = 0;j < i + 1;j++){
//             cout << (i+1) << " ";
//         }
//         cout << endl ;
//     }
//     return 0;
// }

int main(){
    int n = 4;
    char ch = 'A';
    int t = 0;

    for(int i = 0;i < n;i++){
        char y = ch + t;
        for(int j = 0;j < i + 1;j++){
            cout << y ;
            t++;
        }
        cout << "\n";
    }
    return 0;
}