/*
This interface exports an enumerated type called Direction whose elements are the four compass points:
North, East, West, South
*/
//头文件本身不参与编译.头文件中只放变量和函数的声明,而不能放它们的定义.
//一个头文件的内容实际上被引入到多个不同的.cpp文件中
//头文件只能存放变量或函数的声明,而不要放定义
//这个规则有三个例外
//1.头文件可以写const对象的定义,因为全局const对象默认没有extern声明
//所以只在当前文件中有效,对其他文件来说不可见,所以不会导致多重定义
//2.头文件可以写类的定义.类的定义中包含着数据成员和函数成员:数据成员要等到具体的对象被创建时才会被分配空间,但函数成员时需要在一开始就被定义的
//一般的做法时, 把类的定义放在头文件中,把函数成员的实现代码放在一个.cpp文件中
//也可以直接把函数成员的实现代码写进类的定义
#ifndef _direction_h
#define _direction_h

#include <string>

enum Direction
{
    North,
    East,
    West,
    South
};

Direction leftFrom(Direction dir);

Direction rightFrom(Direction dir);

std::string directionToString(Direction);

#endif