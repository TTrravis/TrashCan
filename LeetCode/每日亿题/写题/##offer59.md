# 滑动窗口的最大值

> 给定一个数组nums和滑动窗口的大小k, 请找出所有滑动窗口里的最大值

## 我的题解(超出时间限制QAQ)

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return None
        res = []
        i = 0
        while i < len(nums)-k+1:
            res.append(max(nums[i:i+k]))
            i+=1
        return res
```

考虑到输入数据量过大, 所以此题一定要构建某种数据结构->队列

## 方法一: 优先队列

### 主要思路:

- 对于最大值, 我们可以想到一种非常合适的数据结构, 即优先队列(堆), 其中的大根堆可以帮助实时维护一系列元素中的最大值.
- 初始时, 我们将数组nums的前k个元素放入优先队列中. 每当我们向右移动窗口时, 我们就可以把一个新的元素放入优先队列中, 此时堆顶的元素就是堆中所有元素的最大值.
- 这个最大值可能不在滑动窗口中, 这个值在数组nums中的位置出现在滑动窗口左边界的左侧, 因此在后续向右移动窗口时, 这个值就可以永久地从优先队列中移除
- 不断地移除堆顶的元素, 直到它确实出现在滑动窗口. 此时的堆顶元素就是滑动窗口的最大值

```python
class Solution:
    def maxSlidingWindow(self, nums:List[int], k:int)->List[int]:
        n = len(nums)
        # Python默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        
        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1]<=i-k:
                heapq.heappop(q)
               ans.append(-q[0][0])
            
           return ans
```

### 复杂度分析

- 时间复杂度O(nlogn), 其中n是数组nums的长度;
- 空间复杂度O(n)

## 单调队列

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])
        
        return ans
```

链接：https://leetcode.cn/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof/solution/hua-dong-chuang-kou-de-zui-da-zhi-by-lee-ymyo/
来源：力扣（LeetCode）