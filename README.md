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

### 🚦 Approaches

Partition List is fundamentally about **rearranging nodes around a boundary, not sorting them**. Every node belongs to one of two lanes: values **smaller than `x`** go into the first lane, while values **greater than or equal to `x`** go into the second. The two approaches differ mainly in **how they build those lanes**: **`Segregate`** temporarily stores values and constructs a new list, while **`Rewire`** directly rearranges the existing nodes by changing their links. Both preserve the relative order within each partition.

- **📦 Segregate**

    - **💡 Intuition**

        Think of the list as passing through a sorting station with two buckets. As each node arrives, we place its value into either the **`< x`** bucket or the **`>= x`** bucket.

        Once the entire list has been inspected, we rebuild the linked list by joining the two buckets.

        The important part is that values enter each bucket **in their original order**, so the partition remains stable.

    - **🔹 Steps**

        1. 🔍 Traverse the original linked list.
        2. 🟢 Store values **`< x`** in the **`less`** group.
        3. 🔵 Store values **`>= x`** in the **`greater/equal`** group.
        4. 🏗️ Create a new linked list from the **`less`** group.
        5. 🔗 Append the **`greater/equal`** group.
        6. 🎯 Return the newly constructed list.

    - **📝 Pseudocode**

        ```
        create empty less group
        create empty greater/equal group

        for each node in list:
            if node.value < x:
                add value to less group
            else:
                add value to greater/equal group

        create new list from less group
        append greater/equal group

        return new list
        ```
    
    - **📊 Complexity**

        - **⏱️ Time: `O(n)`**
        - **💾 Space: `O(n)`**

- **🔗 Rewire**

    - **💡 Intuition**

        Why copy values when the linked list already gives us exactly what we need? 😄

        Instead of creating buckets of values, we create **two linked-list chains using the original nodes themselves**.

        Every node is detached from its old position and attached to the appropriate chain. Once traversal is complete, we simply connect the two chains.

        This turns the problem into a pointer-rewiring exercise.

    - **🔹 Steps**

        1. 🔍 Traverse the original list once.
        2. 💾 Save the next node before changing the current node's link.
        3. ✂️ Detach the current node from its original position.
        4. 🟢 Append it to the **`< x`** chain if its value is smaller than **`x`**.
        5. 🔵 Otherwise, append it to the **`>= x`** chain.
        6. 🔗 Connect the two chains.
        7. 🎯 Return the head of the combined list.

    - **📝 Pseudocode**

        ```
        create empty smaller chain
        create empty greater/equal chain

        current = head

        while current exists:
            save next node
            detach current

            if current.value < x:
                append current to smaller chain
            else:
                append current to greater/equal chain

            current = saved next node

        connect smaller chain to greater/equal chain

        return smaller chain if it exists
        otherwise return greater/equal chain
        ```

    - **📊 Complexity**
    
        - **⏱️ Time: `O(n)`**
        - **💾 Space: `O(1)`**

#### ⚖️ Approach Comparison

| Approach         | Core Idea                   |   Time |  Space | New Nodes |
| ---------------- | --------------------------- | -----: | -----: | --------- |
| 📦 **Segregate** | Store values → rebuild list | **`O(n)`** | **`O(n)`** | ✅ Yes     |
| 🔗 **Rewire**    | Rearrange existing nodes    | **`O(n)`** | **`O(1)`** | ❌ No      |

**In short:** **`Segregate`** is the straightforward **collect-and-rebuild** strategy, while **`Rewire`** takes the more linked-list-oriented route of **reuse-and-reconnect**. 🔥

---
