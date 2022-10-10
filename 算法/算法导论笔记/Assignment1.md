# Assignment-1

<center> Yifu TIAN 121090517@link.cuhk.edu.cn </center>

<center> 2022/9/27 </center>

### 2.3-4

First we find the time complexity of basic operations. For the worst case, it will take $$n-1$$ times to finish inserting A[n], so it takes $$\Theta(n)$$ time.

Then for the recursive cases, the scale decreases every time, which is $$T(n-1)$$. 

Therefore, the recurrence
$$
T(n)=
\begin{cases}
\Theta(1) & if \quad n=1,\\
T(n-1) + \Theta(n)&if \quad n>1.
\end{cases}
$$

### 2.4

**a.** $$(2,1),(3,1),(8,6),(8,1),(6,1)$$

**b.** The array $$[n,n-1,...2,1]$$ has the most inversions $$\sum_{i=1}^{n-1}=\frac{n(n-1)}{2}$$

**c.** The running time of insertionSort is $$c\sum_{i=1}^n T(i)$$ , where $$\sum_{i=1}^n T(i)$$ is the number of inversions in $A$, $$c$$ is a constant. 

```python
def insertionSort(arr):
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
    return arr
```

 In the 5th line, we notice that the while loop will begin if j>=0 and key < arr[j]. It implies that key = arr[i] < arr[j] and i > j. Then it will execute the loop $T(j)$ times. So each for loop, the number of constant time steps of insertion sort is $\sum_{j=1}^nT(j)$ which is exactly the inversion number of $A$.

**d.**

```python
import math

# countInversions(A, l, r)
def countInversions(A, l, r):
    if len(A) < 2: return None
	else:
        mid = math.floor((l+r)/2)
        # recursion begin
        left = countInversions(A, l, mid)
        right = countInversions(A, mid+1, r)
        res = mergeInversions(A, l, mid, r) + left + right
        return res
# mergeInversions(A, l, mid, r)
def mergeInversions(A, l, mid, r):
    n1, n2 = mid - l + 1, r - mid
    Left, Right = [0*(n1+1)], [0*(n2+1)] # divide
    for m in range(1, n1+1):
        Left[m] = A[l + m - 1]
	for n in range(1, n2+1):
        Right[n] = A[mid + n]
    L[n1+1] = float("inf")
    R[n2+1] = float("inf")
    i, j = 1, 1
    res = 0
    for k in range(l, r+1): # conquer
        if Left[i] <= Right[j]:
            A[k] = Left[i]
            i += 1
        else:
            res += n1 - i + 1
            A[k] = Right[j]
            j += 1
	return res
    
```

### 3.1.5

By the definition of $f=\Theta(g(n))$, we have
$$
0 \le c_1g(n) \le f(n) \le c_2g(n) \quad for\quad n>n_0.
$$
From $f(n)=\Omega(g(n))$ and $f(n)=O(g(n))$, we have
$$
0 \le c_3g(n) \le f(n)\quad for\quad all\quad n \ge n_1,\\
0 \le f(n) \le c_4g(n)\quad for\quad all\quad n \ge n_2.
$$
Take $n_3=\max(n_1,n_2)$, then we get
$$
0 \le c_3g(n) \le f(n) \le c_4g(n) \quad for\quad all\quad n>n_3.
$$
which satisfies the definition of $\Theta$

### 3.4

**b.**

Find a counterexample, $n^2+n \neq \Theta(\min(n^2, n))=\Theta(n)$

**c.**

From $f(n)=O(g(n))$, we have
$$
0 \le f(n) \le cg(n) \quad for \quad all\quad n \geq n_0
$$
then
$$
\lg(f(n)) \le \lg(cg(n)) = \lg c+\lg(g(n))\quad \#
$$
We need to find a constant $c'$ to satisfy
$$
\lg(f(n)) \leq c'\lg(g(n))
$$
By the #, we have
$$
\lg(f(n))\le\lg c+\lg(g(n))\le c'\lg(g(n)) \\
c' \ge 1+\frac{\lg c}{\lg(g(n))}
$$
take $c'=1+\lg c$ since $\lg(g(n))\ge1$ for some sufficiently large $n$.

Hence we proved.

### 4.3-3

By the master method, we have
$$
a=1,b=2,\\
\rightarrow f(n)=\Theta(n^{\lg1})=\Theta(1),\\
\rightarrow T(n)=\Theta(\lg n)
$$

### 4.5.1

a. By the master method, $T(n)=\Theta(n^4)$

b. By the master method, $T(n)=\Theta(n)$

c. By the master method, $T(n)=\Theta(n^2\lg n)$

d. By the master method, $T(n)=\Theta(n^2)$

e. By the master method, $T(n)=\Theta(n^{\lg  7})$

f. By the master method, $T(n)=\Theta(\sqrt{n}\lg n)$

g. Let $d={m}\mod{2}$, 
$$
\begin{aligned}
T(n) &= \sum_{j-1}^{j=\frac{n}{2}}(2j+d)^2\\
&=\sum_{j=1}^{\frac{n}{2}}4j^2+4jd+d^2\\
&=\frac{n(n+2)(n+1)}{6}+\frac{n(n+2)d}{2}+\frac{d^2n}{2}\\
&=\Theta(n^3)
\end{aligned}
$$

