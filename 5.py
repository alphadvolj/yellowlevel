class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if not headA or not headB:
        return None

    def get_length(head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    lenA = get_length(headA)
    lenB = get_length(headB)

    ptrA = headA
    ptrB = headB

    if lenA > lenB:
        for _ in range(lenA - lenB):
            ptrA = ptrA.next
    else:
        for _ in range(lenB - lenA):
            ptrB = ptrB.next

    while ptrA and ptrB:
        if ptrA == ptrB:
            return ptrA
        ptrA = ptrA.next
        ptrB = ptrB.next

    return None


if __name__ == "__main__":
    intersecting_node = ListNode(8)
    intersecting_node.next = ListNode(4)
    intersecting_node.next.next = ListNode(5)

    listA = ListNode(4)
    listA.next = ListNode(1)
    listA.next.next = intersecting_node

    listB = ListNode(5)
    listB.next = ListNode(6)
    listB.next.next = ListNode(1)
    listB.next.next.next = intersecting_node

    intersection_node = getIntersectionNode(listA, listB)

    if intersection_node:
        print(f"Пересекаются в '{intersection_node.val}'")
    else:
        print("Нет пересечения")