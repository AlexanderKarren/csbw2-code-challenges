# Time complexity: O(n)
# Space complexity: O(n)

# Singly-linked lists are already defined with this interface:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        return str(self.value)


def remove_kth_from_end(head, k):
    print(head, k)
    # we will store the index of each node in a hash table
    index_dict = {}
    current = head
    # index will go up each iteration of loop
    i = 0
    
    while current is not None:
        index_dict.update({i: current})
        i += 1
        current = current.next
        
    if k <= 0 or k > i:
        return head

    index_to_remove = i - k

    prev = index_dict.get(index_to_remove - 1)
    item_to_remove = index_dict.get(index_to_remove)
    next = index_dict.get(index_to_remove + 1)
    
    # if item to remove is head,
    if item_to_remove is index_dict.get(0):
        # return next, making the following node the new head
        return next
    
    prev.next = next
    
    return head

sll = ListNode(20)
current = sll
i = 19

while i >= 11:
    current.next = ListNode(i)
    current = current.next
    i -= 1

print(remove_kth_from_end(sll, 4))

current = sll

while current is not None:
    print(current.value)
    current = current.next