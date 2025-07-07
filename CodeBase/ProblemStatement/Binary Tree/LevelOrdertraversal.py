from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder_traverse(self, root: Optional['TreeNode']) -> Optional['TreeNode']:
        if not root:
            return

        print(root.val, end=' ')
        self.preorder_traverse(root.left)
        self.preorder_traverse(root.right)


    def level_order_traversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_nodes)
        return res

    def preorder_traversal_iterative(self, root: Optional['TreeNode']) -> List[List[int]]:
        if not root:
            return []
        stk = [root]
        res = []
        while stk:
            ele = stk.pop()
            res.append(ele.val)
            if ele.right:
                stk.append(ele.right)
            if ele.left:
                stk.append(ele.left)
        return res

if __name__ == '__main__':
    sol = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.right = TreeNode(6)

    # sol.preorder_traverse(root)
    temp = sol.level_order_traversal(root)
    print()
    print(temp)
    temp1 = sol.preorder_traversal_iterative(root)
    print(temp1)