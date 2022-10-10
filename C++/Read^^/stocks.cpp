#include <iostream>
#include <cstring>

class Stock //声明类
{
private: // 私有数据成员(仅通过成员函数来作出修改)
    char company[30];
    int shares;
    double share_val;
    double total_val;
    void set_tot() { total_val = shares * share_val; } //内联函数
    //最简便的方法是：将内联定义放在定义类的头文件中。
public:
    void acquire(const char *co, int n, double pr);
    void buy(int num, double price);
    void sell(int num, double price);
    void update(double price);
    void show();
};

// 实现
void Stock::acquire(const char *co, int n, double pr)
{
    std::strncpy(company, co, 29);
    company[29] = '\0';
    if (n < 0)
    {
        std::cerr << "Number" << company << "shares";
        shares = 0;
    }
}
void Stock::buy(int num, double price)
{
    set_tot();
}