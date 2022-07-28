#include "calculate.h"
#include <ctime>
#include <iostream>
using namespace std;
int main(){
    Test t;
    int start = clock();
    t.calculate();
    int end = clock();
    cout << "Time is" << end - start << endl;
}