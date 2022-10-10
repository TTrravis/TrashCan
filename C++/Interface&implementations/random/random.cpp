#include<cstdlib>
#include<ctime>
#include "random.h"
#include<cmath>
using namespace std;

void initRandomSeed();

int randomInterger(int low, int high){
    double d = rand() / (double(RAND_MAX) + 1);// 归一化处理
    double s = d * (double(high) - low);// 量化
    return int(floor(low + s));// 翻译&取整
}

double randomReal(double low, double high){
    double d = rand() / (double(RAND_MAX) + 1);
    double s = d * (high - low);
    return low + s;
}

bool randomChance(double p){
    return randomReal(0, 1) < p;
}

void setRandomSeed(int seed){
    initRandomSeed();
    srand(seed);
}

void initRandomSeed(){
    static bool initialized = false;
    if (!initialized){
        srand(int(time(NULL)));
        initialized = true;
        // 如果没有被初始化, 就将初始值设置为某个用户难以预测的值(时间)
        // 编译器对initialized变量进行一次内存分配, 接下来为每一次initRandomSeed函数所共享
    }
}