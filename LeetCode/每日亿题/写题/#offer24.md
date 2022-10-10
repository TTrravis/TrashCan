## 链表反转
纯不会...
```Python
# 方法一:双指针迭代
# 遍历链表, 并在访问各节点的时候修改next引用指向
# 时间复杂度O(N), 空间复杂度O(1)
class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        cur, pre = head, None # cur指向头节点, pre指向null
        while cur:
            tmp = cur.next # 暂存后继节点
            cur.next = pre # 修改引用指向
            pre = cur # 暂存当前节点
            cur = tmp # 访问下一节点
        return pre
```
```Python
class Solution:
    def reverseList(self, head:ListNode)->ListNode:
        cur, pre=head, None
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre
```
```Python
class Solution:
    def reverseList(self, head:ListNode)->ListNode:
        def recur(cur, pre):
            if not cur: return pre # 终止条件
            res = recur(cur.next, cur) # 递归后继节点
            cur.next = pre # 修改节点引用指向
            return res # 返回反转链表的头节点

        return recur(head, None)
```

## 补充
还有一种方法是利用辅助栈先倒序, 再将倒序后的栈转换为链表