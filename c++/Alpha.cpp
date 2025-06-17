#include<iostream>
using namespace std;

int main() {

    char currentAlphabet = 'A';
    int currentNumber = 0;
    
    for (int i = 0; i <= 2; i++) {
        for (int j = 0; j <= 2; j++) {
            char currentCharacter = currentAlphabet + currentNumber;
            cout << currentCharacter << " ";
            currentNumber++;
        }
        cout << "\n";
    }
}