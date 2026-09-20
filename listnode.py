from typing import Optional

# 🔗 ListNode — the basic building block of a singly linked list.
# 📦 Each node stores a value and a reference to the next node in the chain.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val: int = val                  # 📌 Value carried by this node.
        self.next: Optional[ListNode] = next  # ➡️ Link to the next node, or None at the end.
