from typing import Optional
from listnode import ListNode
from .approaches import Segregate

# 🎯 Solution — public entry point for the Partition List problem.
# 🔀 Delegates the partitioning logic to the selected Segregate approach.
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 🚦 Create the selected approach with the list and partition value.
        segregate: Segregate = Segregate(head=head, x=x)

        # 🔗 Execute the approach and return the partitioned linked list.
        return segregate.partition()
