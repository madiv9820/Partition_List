# [🚦 Two Lanes, One Linked List](https://leetcode.com/problems/partition-list/description/?envType=study-plan-v2&envId=top-interview-150)

### 🚦 Story: Two Queues, One Linked List

Imagine a security checkpoint where people are divided into two queues based on an age limit 🎫. Everyone younger than the limit goes into the first queue, while everyone else goes into the second queue. The important rule? **Nobody changes their position within their own queue!** 😄

### 🧩 Question

Given the **`head`** of a linked list and a value **`x`**, **partition the list** so that:

* 🟢 All nodes with values **less than `x`** come first.
* 🔵 All nodes with values **greater than or equal to `x`** come after.
* 🔒 The **original relative order** of nodes must be preserved within both partitions.

> ⚠️ **Partitioning is not sorting!** We only separate the nodes into two groups; we do not rearrange their order within those groups.

#### 🧪 Partition in Action

- **📌 Example 1 — Two Groups, Same Order**

    ```text
    Input:  head = [1,4,3,2,5,2], x = 3
    Output: [1,2,2,4,3,5]
    ```

    Here:

    ```text
    Less than 3:       1 → 2 → 2
    Greater/equal 3:   4 → 3 → 5
    ```

    Combining both groups:

    ```text
    1 → 2 → 2 → 4 → 3 → 5
    ```

    Notice that **`4 → 3 → 5`** remains in the **same relative order** as the original list. 🔒

- **📌 Example 2 — Simple Partition**

    ```text
    Input:  head = [2,1], x = 2
    Output: [1,2]
    ```

    Here:

    ```text
    Less than 2:       1
    Greater/equal 2:   2
    ```

    So the final list becomes:

    ```text
    1 → 2
    ```

#### 📏 Constraints

* 🔢 Number of nodes: **`0 ≤ n ≤ 200`**
* 🔹 Node value: **`-100 ≤ Node.val ≤ 100`**
* 🎯 Partition value: **`-200 ≤ x ≤ 200`**

#### 🎯 Goal

Rearrange the linked list into **two stable partitions** — **`< x`** first and **`≥ x`** second — while keeping the original order inside each partition intact. 🚦

---
