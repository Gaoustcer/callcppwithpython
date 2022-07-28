#include "calculate.h"
#include <cmath>
#include <random>
#include <iostream>
#include <stdlib.h>
using namespace std;
extern "C"{
    Test* Test_new(){return new Test();}
    void callfunction(Test* t){
        t -> calculate();
    }
}
double Test::calculate(){
    double result = 0;
    for(int i = 0;i < N*N*1000;i++){
        result += exp(sin(rand()))/cos(rand()); 
    }
    // default_random_engine e;
    // uniform_int_distribution<unsigned> u(0,9);
    // for(int i = 0;i < N*N;i++){
    //     cout << e() << endl;
    // }
}
// 819119369 143.17017
// 807092599 143
// 807092599 142