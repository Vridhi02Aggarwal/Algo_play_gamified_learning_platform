# trees.py
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def bst_build_steps(arr):
    """
    Builds a Binary Search Tree step by step and records:
    - steps (key, action)
    - explanations (string explanation)
    - root node (final BST structure)
    """

    steps, explanations = [], []

    def insert_bst(root, key):
        if root is None:
            steps.append((key, "insert"))
            explanations.append(f"Inserted {key} as a new node.")
            return BSTNode(key)

        if key < root.key:
            steps.append((root.key, "traverse_left"))
            explanations.append(f"{key} < {root.key} → going left.")
            root.left = insert_bst(root.left, key)
        elif key > root.key:
            steps.append((root.key, "traverse_right"))
            explanations.append(f"{key} > {root.key} → going right.")
            root.right = insert_bst(root.right, key)
        else:
            explanations.append(f"{key} already exists in the BST.")
        return root

    # Build BST step by step
    root = None
    for val in arr:
        root = insert_bst(root, val)

    return root, steps, explanations
