# 删除链表的节点
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。
## 我的解法--遍历
```Python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        cur = head # 创建一个副本
        if cur.val == val:
            cur = cur.next
            return cur
        while cur.next.val != val and cur.next:
            cur = cur.next
        if cur.next.val == val:
            cur.next = cur.next.next
        
        return head
```

## 看看别人的解法--双指针
```Java
class Solution{
    public ListNode deleteNode(ListNode head, int val){
        if (head.val == val){
            return head.next;
        }
        // 双指针初始化
        ListNode pre = head, cur = head.next
        while (cur != None && cur.val != val){
            pre = cur;
            cur = cur.next;
        }
        if (cur != None){
            pre.next = cur.next;
        }
        return head;
    }
}
```
## 递归大法好
```Python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val: return head.next
        head.next = self.deleteNode(head.next, val)
        return head
```