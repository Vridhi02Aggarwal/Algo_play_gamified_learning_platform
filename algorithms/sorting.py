# Bubble sort
def bubble_sort_steps(arr):
    a = arr.copy()
    steps = []
    explanations = []
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            steps.append((a.copy(), (j, j+1)))  # keep track of array + compared indices
            explanations.append(f"Comparing {a[j]} and {a[j+1]}")
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                explanations[-1] += f" → Swap {a[j]} and {a[j+1]}"
            else:
                explanations[-1] += " → No Swap"
    steps.append((a.copy(), None))
    explanations.append("Array fully sorted ")
    return steps, explanations


# Insertion Sort

def insertion_sort_steps(arr):
    a = arr.copy()
    steps = []
    explanations = []
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        explanations.append(f"Key = {key}")
        while j >= 0 and a[j] > key:
            steps.append((a.copy(), (j, i)))  # keep track of array + compared indices
            explanations.append(f"Comparing {a[j]} and {key} → Move {a[j]} to the right")
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        steps.append((a.copy(), (j + 1, i)))  # position where key is placed
        explanations.append(f"Place {key} at position {j + 1}")
    steps.append((a.copy(), None))
    explanations.append("Array fully sorted ")
    return steps, explanations

# ---------------- Heapify Function ----------------
def heapify(arr, n, i, steps, explanations):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        steps.append(arr.copy())
        explanations.append(f"Swapped {arr[largest]} with {arr[i]} to maintain heap property")
        heapify(arr, n, largest, steps, explanations)

def heap_sort_steps(arr):
    steps = [arr.copy()]
    explanations = ["Initial array before heapify"]
    n = len(arr)

    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, steps, explanations)

    # Extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        steps.append(arr.copy())
        explanations.append(f"Swapped {arr[0]} with {arr[i]} and reduced heap size")
        heapify(arr, i, 0, steps, explanations)

    return steps, explanations


    # ---------------- Quick Sort Step Tracker ----------------
# def quick_sort_steps(arr):
#     """Simulate quick sort step by step with partitions"""
#     steps = []
#     explanations = []

#     def partition(low, high):
#         pivot = arr[high]
#         i = low - 1
#         for j in range(low, high):
#             if arr[j] <= pivot:
#                 i += 1
#                 arr[i], arr[j] = arr[j], arr[i]
#             # Capture step
#             steps.append(list(arr))
#             explanations.append(f"Comparing with pivot={pivot}. Swapped if needed.")
#         arr[i+1], arr[high] = arr[high], arr[i+1]
#         steps.append(list(arr))
#         explanations.append(f"Placed pivot {pivot} at correct position.")
#         return i + 1

#     def quick_sort(low, high):
#         if low < high:
#             pi = partition(low, high)
#             quick_sort(low, pi - 1)
#             quick_sort(pi + 1, high)

#     quick_sort(0, len(arr)-1)
#     return steps, explanations


def quick_sort_steps(arr):
    """Simulate quick sort step by step with pivot and comparisons"""
    steps = []
    explanations = []
    highlights = []  # <-- store (pivot, comparisons)

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            # Record comparison
            steps.append(list(arr))
            explanations.append(f"Comparing arr[{j}]={arr[j]} with pivot={pivot}")
            highlights.append({"pivot": high, "compare": [j]})

            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                steps.append(list(arr))
                explanations.append(f"Swapped {arr[i]} and {arr[j]} since arr[{j}] <= pivot {pivot}")
                highlights.append({"pivot": high, "compare": [i, j]})

        arr[i+1], arr[high] = arr[high], arr[i+1]
        steps.append(list(arr))
        explanations.append(f"Placed pivot {pivot} at correct position {i+1}")
        highlights.append({"pivot": i+1, "compare": []})

        return i + 1

    def quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort(low, pi - 1)
            quick_sort(pi + 1, high)

    quick_sort(0, len(arr)-1)
    return steps, explanations, highlights
