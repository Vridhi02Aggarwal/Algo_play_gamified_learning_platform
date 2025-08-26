# avl.py
class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height for balance factor


def avl_build_steps(arr):
    """
    Builds an AVL Tree step by step and records:
    - steps (key, action)
    - explanations (string explanation)
    - root node (final AVL structure)
    """

    steps, explanations = [], []

    def get_height(node):
        return node.height if node else 0

    def get_balance(node):
        return get_height(node.left) - get_height(node.right) if node else 0

    def right_rotate(y):
        x = y.left
        T2 = x.right

        # Rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(get_height(y.left), get_height(y.right))
        x.height = 1 + max(get_height(x.left), get_height(x.right))

        steps.append((y.key, "right_rotate"))
        explanations.append(f"Right rotation at {y.key} (Left-Left imbalance).")
        return x

    def left_rotate(x):
        y = x.right
        T2 = y.left

        # Rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(get_height(x.left), get_height(x.right))
        y.height = 1 + max(get_height(y.left), get_height(y.right))

        steps.append((x.key, "left_rotate"))
        explanations.append(f"Left rotation at {x.key} (Right-Right imbalance).")
        return y

    def insert(node, key):
        if not node:
            steps.append((key, "insert"))
            explanations.append(f"Inserted {key} as a new node.")
            return AVLNode(key)

        if key < node.key:
            steps.append((node.key, "traverse_left"))
            explanations.append(f"{key} < {node.key} → going left.")
            node.left = insert(node.left, key)
        elif key > node.key:
            steps.append((node.key, "traverse_right"))
            explanations.append(f"{key} > {node.key} → going right.")
            node.right = insert(node.right, key)
        else:
            explanations.append(f"{key} already exists in the AVL tree.")
            return node

        # Update height
        node.height = 1 + max(get_height(node.left), get_height(node.right))

        # Get balance factor
        balance = get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = left_rotate(node.left)
            steps.append((node.key, "left_right_case"))
            explanations.append(f"Left-Right case at {node.key}. First left rotate {node.left.key}, then right rotate {node.key}.")
            return right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = right_rotate(node.right)
            steps.append((node.key, "right_left_case"))
            explanations.append(f"Right-Left case at {node.key}. First right rotate {node.right.key}, then left rotate {node.key}.")
            return left_rotate(node)

        return node

    # Build AVL tree step by step
    root = None
    for val in arr:
        root = insert(root, val)

    return root, steps, explanations
