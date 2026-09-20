from typing import Optional
from listnode import ListNode

# 🔗 Rewire Approach
# 🧩 Partitions the original linked list by rewiring existing node connections.
# 🟢 Nodes smaller than x form the left partition.
# 🔵 Nodes greater than or equal to x form the right partition.
# 🔒 Both partitions preserve the original relative ordering of their nodes.
# ♻️ No new ListNode objects are created; the existing nodes are reused.
class Rewire:
    """Partition a linked list in-place by rewiring existing node connections."""

    def __init__(self, head: Optional[ListNode], x: int) -> None:
        # 📌 Store the input list and partition value.
        self.head: Optional[ListNode] = head
        self.x: int = x

    def partition(self) -> Optional[ListNode]:
        """Rearrange the list so nodes < x precede nodes >= x."""

        # 📭 An empty list needs no partitioning.
        if not self.head:
            return self.head

        # 🟢 Head and tail of the nodes smaller than x.
        smaller_head: Optional[ListNode] = None
        smaller_tail: Optional[ListNode] = None

        # 🔵 Head and tail of the nodes greater than or equal to x.
        greater_equal_head: Optional[ListNode] = None
        greater_equal_tail: Optional[ListNode] = None

        # 🔍 Traverse the original list one node at a time.
        current_node: Optional[ListNode] = self.head

        while current_node:
            # 💾 Save the next node before changing the current node's link.
            next_node: Optional[ListNode] = current_node.next

            # ✂️ Detach the current node from its original position.
            current_node.next = None

            if current_node.val < self.x:
                # 🟢 Add the node to the smaller-than-x partition.
                if not smaller_head:
                    smaller_head = smaller_tail = current_node
                else:
                    smaller_tail.next = current_node
                    smaller_tail = current_node
            else:
                # 🔵 Add the node to the greater-than-or-equal-x partition.
                if not greater_equal_head:
                    greater_equal_head = greater_equal_tail = current_node
                else:
                    greater_equal_tail.next = current_node
                    greater_equal_tail = current_node

            # ➡️ Continue with the next node from the original list.
            current_node = next_node

        # 🔗 Join the two partitions while preserving their internal order.
        if smaller_tail: smaller_tail.next = greater_equal_head

        # 🔵 If no node is smaller than x, the right partition is the result.
        return smaller_head if smaller_head else greater_equal_head
