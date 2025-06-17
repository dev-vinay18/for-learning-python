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

int main(){
    int n = 3;
    char ch = 'A';

    for(int i= 0;i < n; i++){
        for(int j = 0;j < n; j++){
            ch = ch + 1;
            cout << ch ;
            ch++;
            
        }
        cout << '\n';
    }

}