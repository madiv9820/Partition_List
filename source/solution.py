from typing import Optional, List
from listnode import ListNode

# 🚦 Segregate Approach
# 📦 First collect values into two groups — values < x and values >= x.
# 🔗 Then rebuild a new linked list by joining both groups in order.
# 🔒 Values are collected in traversal order, so relative order is preserved.
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        # 🟢 Values smaller than x.
        # 🔵 Values greater than or equal to x.
        less_values: List[int] = []
        greater_equal_values: List[int] = []

        # 🔍 Traverse the original list and segregate values into their groups.
        current_node: ListNode = head
        while current_node:
            if current_node.val < x:
                less_values.append(current_node.val)
            else:
                greater_equal_values.append(current_node.val)

            current_node = current_node.next

        # 🏗️ Rebuild the linked list from the two ordered groups.
        head: Optional[ListNode] = None
        tail: Optional[ListNode] = None

        # 🟢 Add all values smaller than x first.
        for value in less_values:
            if not head:
                head = tail = ListNode(value)
            else:
                tail.next = ListNode(value)
                tail = tail.next

        # 🔵 Append all values greater than or equal to x.
        for value in greater_equal_values:
            if not head:
                head = tail = ListNode(value)
            else:
                tail.next = ListNode(value)
                tail = tail.next

        # 🎯 Return the newly constructed partitioned list.
        return head
