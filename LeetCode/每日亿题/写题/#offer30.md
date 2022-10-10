# 剑指offer 30
写一个实现min的栈
* 没写过关于栈的题, 不会...
- 解题思路:
1. 普通栈的push()和pop()函数的复杂度为O(1); 而获取栈最小值min()函数需要遍历整个栈, 复杂度为O(N)
2. 借助辅助栈将min()函数复杂度降为O(1)
- 数据栈A: 用于存储所有元素
- 辅助栈B: 用于存储A中所有非严格降序元素的子序列, 则栈A的最小元素始终对应栈B的栈顶元素. 此时, min()函数只需要返回栈B的栈顶元素即可.
* 因此需要维护好栈B的元素, 使其保持是栈A的非严格降序元素的子序列, 即可实现min()函数的O(1)复杂度
-> 时间复杂度为O(1)
-> 空间复杂度为O(N)
```Python
class MinStack:
    def __init__(self):
        self.A, self.B = [], [] # 初始化两个栈

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x: # 辅助栈B为空或最后一个元素值大于等于x(为了保证非严格降序)
            self.B.append(x)
    def pop(self) -> None: # 要保持A, B的更新一致性
        if self.A.pop() == self.B[-1]: 
            self.B.pop()
    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1] # A中的最小元素对应B中的栈顶元素
```
