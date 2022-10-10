#include<iostream>

using namespace std;

int main(int argc, const char * argv[]){

    // 通过const char * 初始化
    string s1 = "aaaa";

    // 构造函数初始化
    string s2("bbbbb");

    // 通过拷贝构造函数来初始化对象s3
    string s3 = s2;

    // 用10个'a'字符来初始化字符串
    string s4(10, 'a');

    return 0;
}