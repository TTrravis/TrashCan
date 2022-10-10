/*字符串的遍历
-数组方式, 通过[]操作符遍历(不会抛出异常)
-at()方法遍历, 根据index取值(会抛出异常)
-通过STL迭代器遍历
*/
#include <iostream>
using namespace std;
int main(int argc, const char *argv[])
{
    //创建字符串对象
    string str("abcde");

    // 数组形式遍历(不会抛出异常, 程序直接中止)
    for (int i = 0; i < str.length(); i++)
    {
        cout << str[i] << endl;
    }

    // at方法遍历(会抛出异常, 程序可以处理异常)
    for (int i = 0; i < str.length(); i++)
    {
        cout << str[i] << endl;
    }

    // 迭代器遍历
    // 迭代器可以看作是一个字符的指针
    for (string::iterator it = str.begin(); it != str.end(); it++)
    {
        cout << *it << endl;
    }
}