# segment.py
import math

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.size = 2 * (2**math.ceil(math.log2(self.n))) - 1
        self.tree = [0] * self.size
        self.steps = []
        self.explanations = []
        self.build(arr, 0, self.n - 1, 0)

    # def build(self, arr, l, r, idx):
    #     if l == r:
    #         self.tree[idx] = arr[l]
    #         self.steps.append((idx, arr[l]))
    #         self.explanations.append(f"Leaf node at index {l}: value = {arr[l]}")
    #         return arr[l]

    #     mid = (l + r) // 2
    #     left_val = self.build(arr, l, mid, idx * 2 + 1)
    #     right_val = self.build(arr, mid + 1, r, idx * 2 + 2)

    #     self.tree[idx] = left_val + right_val
    #     self.steps.append((idx, self.tree[idx]))
    #     self.explanations.append(f"Internal node [{l}, {r}] = {left_val} + {right_val} = {self.tree[idx]}")
    #     return self.tree[idx]

# def segment_steps(arr):
#     seg_tree = SegmentTree(arr)
#     return seg_tree.tree, seg_tree.steps, seg_tree.explanations
# # 
# segment.py
# def segment_steps(arr):
#     n = len(arr)
#     size = 1
#     while size < n:  # find nearest power of 2
#         size *= 2
#     size *= 2  # total size of segment tree array

#     tree = [None] * size
#     steps = []
#     explanations = []

#     def build(idx, l, r):
#         if l == r:
#             tree[idx] = arr[l]
#             steps.append((idx, tree[idx]))
#             explanations.append(f"Leaf node: arr[{l}] = {arr[l]}")
#             return tree[idx]
#         mid = (l + r) // 2
#         left_val = build(2 * idx + 1, l, mid)
#         right_val = build(2 * idx + 2, mid + 1, r)
#         tree[idx] = left_val + right_val
#         steps.append((idx, tree[idx]))
#         explanations.append(f"Node [{l}, {r}] = {left_val} + {right_val} = {tree[idx]}")
#         return tree[idx]

#     build(0, 0, n - 1)
#     return tree, steps, explanations


# segment.py
def segment_steps(arr):
    import math
    n = len(arr)
    height = math.ceil(math.log2(n))
    size = 2 * (2**height) - 1
    tree = [None] * size
    steps = []
    explanations = []

    def build_iterative(idx, l, r):
        if l == r:
            tree[idx] = arr[l]
            steps.append((idx, tree[idx]))
            explanations.append(f"Leaf node: arr[{l}] = {arr[l]}")
            return tree[idx]
        mid = (l + r) // 2
        left_val = build_iterative(2*idx+1, l, mid)
        right_val = build_iterative(2*idx+2, mid+1, r)
        tree[idx] = left_val + right_val
        steps.append((idx, tree[idx]))
        explanations.append(f"Node [{l},{r}] = {left_val} + {right_val} = {tree[idx]}")
        return tree[idx]

    build_iterative(0, 0, n-1)
    return tree, steps, explanations
