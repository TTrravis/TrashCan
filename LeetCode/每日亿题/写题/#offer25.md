# 合并两个排序的链表

> 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

## 我的解法---辅助栈

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 辅助栈
        if l1 is None and l2 is None: return None
        stack = []
        while l1:
            stack.append(l1.val)
            l1 = l1.next
        while l2:
            stack.append(l2.val)
            l2 = l2.next
        stack.sort()
        head = ListNode(stack[0])
        tail = head
        for i in range(1,len(stack)):
            tail.next = ListNode(stack[i])
            tail = tail.next
        return head
```

这种解法时间复杂度和空间复杂度都不是很好, 由于是对两个有序链表进行合并,很自然地想到用双指针去优化

## 双指针

- 在此题中, 初始状态合并链表中没有节点, 因此循环第一轮时无法将节点添加到合并链表中.

- 解决方案: **初始化一个辅助节点dum作为合并链表的伪头节点**将各节点添加至dum之后

  ### 算法流程

  1. 初始化: 伪头节点dum, 节点cur指向dum
  2. 循环合并: 当l1或l2为空时跳出;
     1. 当l1.val<l2.val时, cur的后继节点指定为l1, 并l1向前走一步
     2. 当l1.val>=l2.val时, cur的后继节点指定为l2, 并l2向前走一步
     3. 节点cur向前走一步, 即cur=cur.next
  3. 合并剩余尾部: 跳出时有两种情况:l1为空或l2为空
     	1. 若l1!=null, 则将l1添加至节点cur之后
     	1. 否则, 将l2添加至节点cur之后
  4. 返回值: 合并链表在伪头节点dum之后, 因此返回dum.next即可

### 复杂度分析

- 时间复杂度: O(M+N):M,N分别为链表l1,l2的长度, 合并操作需遍历两链表
- 空间复杂度: O(1):节点引用dum, cur使用常数大小的额外空间

### 代码实现

```python
class Solution:
    def mergeTwoLists(self, l1:ListNode, l2:ListNode)->ListNode:
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2 # 三元表达式写法
        return dum.next # 注意一开始的时候创建了一个伪头节点, 所以这里需要返回dum.next
```

