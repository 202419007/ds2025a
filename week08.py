def pre_order(node):  # 전위
    if node is None:
        return
    print(node.data, end="->")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):  # 중위
    if node is None:
        return
    in_order(node.left)
    print(node.data, end="->")
    in_order(node.right)


def post_order(node):  # 후위, node1
    if node is None:  # 지나감
        return
    post_order(node.left)  # 7~12 복제, node2(l) -> node4(l) -> None
    post_order(node.right)  # node4(r)
    print(node.data, end="->")  # hw(node4) -> node2(r)...반복


class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None

# BST
if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]  # 10
    root = node

    for number in numbers[1:]:  # 15
        node = TreeNode()
        node.data = number

        current = root  # current = 이동
        while True:
            if number < current.data:  # 작으면 left
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # 이동
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.left  # 이동

    print('BST 구성 완료')

    pre_order(root)  # 전위
    print()
    in_order(root)  # 중위
    print()
    post_order(root)  # 후위