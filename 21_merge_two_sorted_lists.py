from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
        
        return dummy.next

# Пример использования
#list1 = ListNode(0)
list2 = ListNode(1)

list1 = []
list1.append(ListNode(1))

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

# Выводим значения объединенного списка
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
print("None")
