from typing import Optional
from .ttypes import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        206. 反转链表
        https://leetcode.cn/problems/reverse-linked-list/

        递归实现.
        递归的要点, 就是假设递归已经处理了剩余规模的数据.
        然后处理边界和后置数据.
        """
        if head is None:
            return None
        if head.next is None:  # 很关键
            return head
        new_head = self.reverseList(head.next)  # 假设head.next已经完成了反转
        head.next.next = head  # 原来的head.next此时已经变为结尾, 但是由于指针仍有效, 因此可以通过head.next找到新结尾, 然后把head挂上去
        head.next = None  # 置空结尾
        return new_head

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        206. 反转链表
        https://leetcode.cn/problems/reverse-linked-list/

        迭代实现: 双指针
        """
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next  # 暂存快指针
            curr.next = prev  # 修正指向
            prev = curr  # 向前移动
            curr = nxt
        return prev


    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        92. 反转链表 II
        https://leetcode.cn/problems/reverse-linked-list-ii/
        """
        k = right - left + 1  # 包含right, 因此+1

        dummy = ListNode(nxt=head)

        prev = dummy
        start = prev.next

        while left > 1:  # 编号从1开始
            prev = start  # 需要记录前驱, 处理非开头反转
            start = start.next
            left -= 1
        prev.next = self.reverseFirstK(start, k)

        return dummy.next

    def reverseFirstK(self, head: ListNode, k: int) -> ListNode:
        """
        反转前k个
        """
        if head is None:
            return head
        if k == 1:
            return head

        new_head = self.reverseFirstK(head.next, k - 1)  # 假设后面k-1个(如果有), 已经完成了反转
        last = head.next.next  # head.next这时已经变成结尾, 而head.next.next 其实为 K个 之后的那个, 可能为空
        head.next.next = head  # 将head挂到结尾
        head.next = last  # 修正结尾之后的(K个之后的)

        return new_head

    def reverseFirstK2(self, head: ListNode, k: int) -> ListNode:
        """
        反转前k个
        迭代实现
        """
        prev = None
        curr = head

        while k > 0:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            k -= 1
        head.next = curr  # 此时head已经在结尾, 将K个之后的串起来

        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        25. K 个一组翻转链表
        https://leetcode.cn/problems/reverse-nodes-in-k-group/
        """
        dummy = ListNode(nxt=head)

        prev = dummy
        curr = prev.next
        while self.remainK(curr, k):
            prev.next = self.reverseFirstK(curr, k)
            prev = curr
            curr = prev.next

        return dummy.next

    def remainK(self, head: ListNode, k: int) -> bool:
        cnt = 0;
        while head is not None:
            head = head.next
            cnt += 1
            if cnt >= k:
                return True
        return False

    def swapPairs(self, head: ListNode) -> ListNode:
        """
        24. 两两交换链表中的节点
        https://leetcode.cn/problems/swap-nodes-in-pairs/

        2个一组
        """
        return self.reverseKGroup(head, 2)
