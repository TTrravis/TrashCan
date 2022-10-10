# 从头到尾打印链表
链表只能 从前至后 访问每个节点，而题目要求 倒序输出 各节点值，这种 先入后出 的需求可以借助 栈 来实现。

## 流程
1. 入栈:遍历链表, 将各节点值push入栈
2. 出栈:将各节点值pop出栈, 存储到数组中并返回
```Python
class Solution:
    def reversePrint(self, head:ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
```