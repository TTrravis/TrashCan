#ifndef _random_h
#define _random_h

int randomInteger(int low, int high);
// 输入上界high和下界low, 生成随机整数

double randomReal(double low, double high);
// 输入上界high和下界low, 生成随机浮点数

bool randomChance(double p);
// 以某个特定的概率模拟一个随机事件.
//输入0.5, 来模拟抛硬币事件

void setRandomSeed(int seed);

#endif _random_h