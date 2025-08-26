# app.py
import streamlit as st
import matplotlib.pyplot as plt
import time
import numpy as np
import networkx as nx
import json

# Load quiz data
with open("quiz/quiz_data.json", "r") as f:
    quiz_data = json.load(f)

# Initialize session state for XP and completed items
# XP and progress initialization
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "quiz_progress" not in st.session_state:
    st.session_state.quiz_progress = {}
if "completed_algorithms" not in st.session_state:
    st.session_state.completed_algorithms = set()
if "completed_sections" not in st.session_state:
    st.session_state.completed_sections = set()
if "completed_quizzes" not in st.session_state:
    st.session_state.completed_quizzes = set()



# Custom CSS
st.markdown("""
    <style>
        body {
            background-color: #000000;
            color: #ffffff;
        }
        .stButton > button {
            background: linear-gradient(45deg, #ff416c, #ff4b2b);
            color: white;
            border: none;
            padding: 0.6em 1.2em;
            border-radius: 12px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            margin: 5px;
        }
        .stButton > button:hover {
            background: linear-gradient(45deg, #1e90ff, #00bfff);
            transform: scale(1.05);
        }
        .question-box {
            background: #1c1c1c;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 0px 15px rgba(255,255,255,0.2);
            margin-bottom: 20px;
        }
        h2 {
            color: #00ffcc;
            text-align: center;
            margin-bottom: 20px;
        }
        h1{
            color: #00ffcc;
            text-align: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)



# # ------------------ Sidebar Navigation ------------------
st.sidebar.title("Algorithm Visualizer")

category = st.sidebar.selectbox("Choose Category", ["Sorting", "Trees", "Graphs"])  #, "Dynamic Programming"

choice = None

if category == "Sorting":
    choice = st.sidebar.radio("Sorting Algorithms", ["Bubble Sort", "Insertion Sort", "Heap Sort", "Quick Sort"])
elif category == "Trees":
    choice = st.sidebar.radio("Tree Algorithms", ["Binary Search Tree", "AVL Tree", "Segment Tree"])
elif category == "Graphs":
    choice = st.sidebar.radio("Graph Algorithms", ["DFS", "BFS", "Dijkstra", "Kruskal"])
# elif category == "Dynamic Programming":
#     choice = st.sidebar.radio("DP Algorithms", ["Knapsack", "LCS", "Floyd Warshall"])




# ------------------ Main Content Area ------------------


st.set_page_config(page_title="Algorithm Visualizer", page_icon="📊", layout="centered")

st.title("ALGO PLAY")
# st.subheader("Bubble Sort")

# -- import algorithm functions --

# ------bubble sort ------
from algorithms.sorting import bubble_sort_steps
# ----- insertion sort -------
from algorithms.sorting import insertion_sort_steps
# ------ heap sort ------
from algorithms.sorting import heap_sort_steps
# ------ quick sort ------
from algorithms.sorting import quick_sort_steps
# ------ BST ------
from algorithms.BST_trees import bst_build_steps
# ------ AVL ------
from algorithms.avl_trees import avl_build_steps
# ------ Segment Tree ------
from algorithms.segment_trees import segment_steps
# ------ DFS ------ 
from algorithms.graph import dfs_build_steps
# ------ BFS ------
from algorithms.graph import bfs_build_steps
# ------- Dijkstra ------
from algorithms.graph import dijkstra_build_steps
# ------ kruskal -----
from algorithms.graph import kruskal_build_steps

# ------------------ Bubble Sort Section ------------------

# import algorithm functions


if choice == "Bubble Sort":
    st.header("Bubble Sort")

    # Notes
    st.subheader("Understanding Bubble Sort")
    st.markdown("""
    Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. This process is repeated until the list is sorted.
                

**How It Works**

 - Start at the beginning of the list.
 - Compare the first two elements:
   - If the first is greater than the second, swap them.
   - Otherwise, move to the next pair.


 - Repeat this process for all elements in the list.
 - After each pass, the largest unsorted element "bubbles up" to its correct position.
 - Continue until no swaps are needed, indicating the list is sorted.
                

**Key Characteristics**

 - *Time Complexity:*
   - Best Case (Already Sorted): O(n)
   - Average Case: O(n^2)
   - Worst Case: O(n^2)


 - *Space Complexity:* O(1) (In-place sorting)
 - *Stability:* Stable (does not change the relative order of equal elements)
 - *Suitability:* Inefficient for large datasets.

    """)

    st.subheader("Visualizing Bubble Sort")

    if "array" not in st.session_state:
        st.session_state.array = []

    # Input Options
    option = st.radio("Choose Input Method:", ["Enter manually", "Generate Random Array "])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 64, 34, 25, 12, 22, 11, 90)",
            "64,34,25,12,22,11,90"
        )
        try:
            st.session_state.array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Initial Array:", st.session_state.array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")

    else:
        size = st.slider("Array Size", 5, 20, 10)
        if st.button("Generate Random Array 🎲"):
            st.session_state.array = np.random.randint(1, 100, size).tolist()
        if st.session_state.array:
            st.write("### Random Array:", st.session_state.array)


    # visualization
    if st.session_state.array and st.button("Start Visualization"):
        steps, explanations = bubble_sort_steps(list(st.session_state.array))
        chart = st.empty()
        explain_box = st.empty()

        for k, (step, indices) in enumerate(steps):
            fig, ax = plt.subplots(figsize=(8, 4))
            
            # Bars with highlight
            bar_colors = ["skyblue"] * len(step)
            if indices:
                bar_colors[indices[0]] = "orange"  # comparing element
                bar_colors[indices[1]] = "red"     # compared with

            ax.bar(range(len(step)), step, color=bar_colors)
            ax.set_title(f"Step {k+1}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(0.6)

        st.success("Bubble Sort Completed!")

# ---- insertion sort section ----



elif choice == "Insertion Sort":
    st.header("Insertion Sort")

    # Notes
    st.subheader("Understanding Insertion Sort")
    st.markdown("""
    Insertion Sort builds the sorted list one element at a time by picking each element and inserting it into its correct position among the already sorted elements.
    
    **How It Works**
    
    - Start with the second element, considering the first as sorted.
    - Pick the current element (key).
    - Compare it with elements before it:
      - Shift larger elements one position to the right.
      - Insert the key in the correct position.
    - Repeat until the array is sorted.
    
    **Key Characteristics**
    
    - *Time Complexity:*
      - Best Case (Already Sorted): O(n)
      - Average Case: O(n²)
      - Worst Case: O(n²)
    - *Space Complexity:* O(1) (In-place sorting)
    - *Stability:* Stable
    - *Suitability:* Works well for small or nearly sorted datasets.
    """)

    st.subheader("Visualizing Insertion Sort")

    if "array" not in st.session_state:
        st.session_state.array = []

    # Input Options
    option = st.radio("Choose Input Method:", ["Enter manually", "Generate Random Array "])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 12, 11, 13, 5, 6)",
            "12,11,13,5,6"
        )
        try:
            st.session_state.array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Initial Array:", st.session_state.array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")

    else:
        size = st.slider("Array Size", 5, 20, 10)
        if st.button("Generate Random Array 🎲"):
            st.session_state.array = np.random.randint(1, 100, size).tolist()
        if st.session_state.array:
            st.write("### Random Array:", st.session_state.array)

    # visualization
    if st.session_state.array and st.button("Start Visualization"):
        steps, explanations = insertion_sort_steps(list(st.session_state.array))
        chart = st.empty()
        explain_box = st.empty()

        for k, (step, indices) in enumerate(steps):
            fig, ax = plt.subplots(figsize=(8, 4))

            # Highlight current comparisons
            bar_colors = ["skyblue"] * len(step)
            if indices:
                for idx in indices:
                    if idx < len(step):
                        bar_colors[idx] = "orange"

            ax.bar(range(len(step)), step, color=bar_colors)
            ax.set_title(f"Step {k+1}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(0.6)

        st.success("Insertion Sort Completed!")


# ---- heap sort -------
elif choice == "Heap Sort":
    st.header("Heap Sort")

    # Notes
    st.subheader("Understanding Heap Sort")
    st.markdown("""
    Heap Sort is a comparison-based sorting algorithm that uses a **binary heap data structure**.

    **How It Works**
    1. Build a max heap from the input data.
    2. The largest element is stored at the root.
    3. Swap it with the last element of the heap.
    4. Reduce the heap size and heapify the root.
    5. Repeat until the heap is empty and array is sorted.

    **Key Characteristics**
    - *Time Complexity:*
      - Best Case: O(n log n)
      - Average Case: O(n log n)
      - Worst Case: O(n log n)
    - *Space Complexity:* O(1) (In-place sorting)
    - *Stability:* Not stable
    - *Suitability:* Works well for large datasets where stability is not required.
    """)

    st.subheader("Visualizing Heap Sort")

    if "array" not in st.session_state:
        st.session_state.array = []

    # Input Options
    option = st.radio("Choose Input Method:", ["Enter manually", "Generate Random Array "])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 4,10,3,5,1)",
            "4,10,3,5,1"
        )
        try:
            st.session_state.array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Initial Array:", st.session_state.array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")

    else:
        size = st.slider("Array Size", 5, 15, 7)
        if st.button("Generate Random Array 🎲"):
            st.session_state.array = np.random.randint(1, 100, size).tolist()
        if st.session_state.array:
            st.write("### Random Array:", st.session_state.array)

    # # Heapify and Heap Sort functions
    

    # Draw tree visualization
    # import networkx as nx
    def draw_heap_tree(arr, highlight=None):
        G = nx.Graph()
        n = len(arr)

        for i in range(n):
            if 2*i+1 < n:
                G.add_edge(arr[i], arr[2*i+1])
            if 2*i+2 < n:
                G.add_edge(arr[i], arr[2*i+2])

        pos = nx.spring_layout(G, seed=42)
        colors = ["lightgreen" if highlight == val else "skyblue" for val in arr]

        nx.draw(G, pos, with_labels=True, node_size=1500, node_color=colors,
                font_size=12, font_weight="bold")

    # Visualization execution
    if st.session_state.array and st.button("Start Visualization"):
        steps, explanations = heap_sort_steps(list(st.session_state.array))
        chart = st.empty()
        explain_box = st.empty()

        for k, step in enumerate(steps):
            fig, ax = plt.subplots(figsize=(8, 5))
            draw_heap_tree(step)
            ax.set_title(f"Step {k+1}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(0.8)

        st.success("Heap Sort Completed!")


# ---------------- QUICK SORT ----------------
elif choice == "Quick Sort":
    st.header("Quick Sort")

    # Notes / Theory Section
    st.subheader("Understanding Quick Sort")
    st.markdown("""
    Quick Sort is a **Divide and Conquer** algorithm.  
    It works by selecting a **pivot element**, partitioning the array around it,
    and then recursively sorting the left and right partitions.

    **How It Works**
    - Pick a pivot (usually last, first, or random element).
    - Partition the array:
      - Elements smaller than pivot → left side.
      - Elements greater than pivot → right side.
    - Recursively apply Quick Sort on left and right partitions.
    - Combine results to get a sorted array.

    **Key Characteristics**
    - *Time Complexity*:
        - Best / Average Case: O(n log n)
        - Worst Case (already sorted, poor pivot): O(n²)
    - *Space Complexity*: O(log n) (recursive stack)
    - *Stability*: Not stable
    - *Suitability*: Great for large datasets, very fast in practice.
    """)

    # ---------------- Input Section ----------------
    st.subheader("Visualizing Quick Sort")

    if "quick_array" not in st.session_state:
        st.session_state.quick_array = []

    option = st.radio("Choose Input Method for Quick Sort:", ["Enter manually", "Generate Random Array "])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 10, 7, 8, 9, 1, 5)",
            "10,7,8,9,1,5"
        )
        try:
            st.session_state.quick_array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Initial Array:", st.session_state.quick_array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")

    else:
        size = st.slider("Array Size", 5, 20, 10, key="quick_size")
        if st.button("Generate Random Array 🎲", key="quick_generate"):
            st.session_state.quick_array = np.random.randint(1, 100, size).tolist()
        if st.session_state.quick_array:
            st.write("### Random Array:", st.session_state.quick_array)



    # ---------------- Visualization ----------------
    if st.session_state.quick_array and st.button("Start Quick Sort Visualization"):
        arr_copy = list(st.session_state.quick_array)
        steps, explanations, highlights = quick_sort_steps(arr_copy)

        chart = st.empty()
        explain_box = st.empty()

        for k, step in enumerate(steps):
            fig, ax = plt.subplots(figsize=(8, 4))
            bar_colors = ["skyblue"] * len(step)

            # Highlight pivot in RED
            if "pivot" in highlights[k]:
                pivot_idx = highlights[k]["pivot"]
                if 0 <= pivot_idx < len(step):
                    bar_colors[pivot_idx] = "red"

            # Highlight comparisons in ORANGE
            if "compare" in highlights[k]:
                for idx in highlights[k]["compare"]:
                    if 0 <= idx < len(step):
                        bar_colors[idx] = "orange"

            ax.bar(range(len(step)), step, color=bar_colors)
            ax.set_title(f"Step {k+1}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(0.7)

        st.success("Quick Sort Completed")


# -------------------- Trees --------------------------------------

# ----- BST -------
elif choice == "Binary Search Tree":
    # 

    # Notes / Theory Section
    st.subheader("Understanding Binary Search Tree")
    st.markdown("""
    A **Binary Search Tree (BST)** is a binary tree where:  
    - The **left child** contains values **less** than the parent.  
    - The **right child** contains values **greater** than the parent.  

    **Operations Supported**  
    - Insert  
    - Search  
    - Delete  

    **Time Complexity**  
    - Average: O(log n)  
    - Worst (skewed tree): O(n)  
    """)

    # ---------------- Input Section ----------------
    st.subheader("Visualizing Binary Search Tree")
    if "bst_array" not in st.session_state:
        st.session_state.bst_array = []

    option = st.radio("Choose Input Method for BST:", ["Enter manually", "Generate Random Array "])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 50, 30, 70, 20, 40, 60, 80)",
            "50,30,70,20,40,60,80"
        )
        try:
            st.session_state.bst_array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Input Array:", st.session_state.bst_array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")
    else:
        size = st.slider("Array Size", 5, 15, 7, key="bst_size")
        if st.button("Generate Random Array 🎲", key="bst_generate"):
            st.session_state.bst_array = np.random.randint(1, 100, size).tolist()
        if st.session_state.bst_array:
            st.write("### Random Array:", st.session_state.bst_array)

    # ---------------- Visualization ----------------
    if st.session_state.bst_array and st.button("Start BST Visualization"):
        

        arr_copy = list(st.session_state.bst_array)
        root, steps, explanations = bst_build_steps(arr_copy)

        chart = st.empty()
        explain_box = st.empty()

        def draw_tree(node, graph=None, pos=None, x=0, y=0, layer=1):
            if graph is None:
                graph = nx.DiGraph()
                pos = {}
            graph.add_node(node.key)
            pos[node.key] = (x, y)
            if node.left:
                graph.add_edge(node.key, node.left.key)
                draw_tree(node.left, graph, pos, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                draw_tree(node.right, graph, pos, x + 1 / layer, y - 1, layer + 1)
            return graph, pos

        # Draw after each insertion
        inserted = []
        for k, val in enumerate(arr_copy):
            inserted.append(val)
            root_partial, _, _ = bst_build_steps(inserted)
            G, pos = draw_tree(root_partial)

            fig, ax = plt.subplots(figsize=(8, 5))
            nx.draw(G, pos, with_labels=True, arrows=False, node_size=1000,
                    node_color="skyblue", font_size=10, font_weight="bold", ax=ax)
            ax.set_title(f"Step {k+1}: Insert {val}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(1)

        st.success("BST Construction Completed ")

# ------ AVL TREE ---------

elif choice == "AVL Tree":

    
    # ---------------- Notes / Theory ----------------
    st.subheader("Understanding AVL Tree")
    st.markdown("""
    An **AVL Tree** is a **self-balancing Binary Search Tree (BST)** where the difference 
    in heights of left and right subtrees (called **balance factor**) is at most 1.  

    **Balancing Operations:**  
    - **LL Rotation** → Right Rotate  
    - **RR Rotation** → Left Rotate  
    - **LR Rotation** → Left-Right Rotate  
    - **RL Rotation** → Right-Left Rotate  

    **Time Complexity**  
    - Search: O(log n)  
    - Insert: O(log n)  
    - Delete: O(log n)  
    """)

    # ---------------- Input Section ----------------
    st.subheader("Visualizing AVL Tree")

    if "avl_array" not in st.session_state:
        st.session_state.avl_array = []

    option = st.radio("Choose Input Method for AVL Tree:", ["Enter manually", "Generate Random Array"])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 10, 20, 30, 40, 50, 25)",
            "10,20,30,40,50,25"
        )
        try:
            st.session_state.avl_array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Input Array:", st.session_state.avl_array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")
    else:
        size = st.slider("Array Size", 5, 15, 7, key="avl_size")
        if st.button("Generate Random Array 🎲", key="avl_generate"):
            st.session_state.avl_array = np.random.randint(1, 100, size).tolist()
        if st.session_state.avl_array:
            st.write("### Random Array:", st.session_state.avl_array)

    # ---------------- Visualization ----------------
    if st.session_state.avl_array and st.button("Start AVL Visualization"):
        arr_copy = list(st.session_state.avl_array)
        root, steps, explanations = avl_build_steps(arr_copy)

        chart = st.empty()
        explain_box = st.empty()

        def draw_tree(node, graph=None, pos=None, x=0, y=0, layer=1):
            if node is None:
                return graph, pos
            if graph is None:
                graph = nx.DiGraph()
                pos = {}
            graph.add_node(node.key)
            pos[node.key] = (x, y)
            if node.left:
                graph.add_edge(node.key, node.left.key)
                draw_tree(node.left, graph, pos, x - 1 / layer, y - 1, layer + 1)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                draw_tree(node.right, graph, pos, x + 1 / layer, y - 1, layer + 1)
            return graph, pos

        # Draw after each insertion
        inserted = []
        for k, val in enumerate(arr_copy):
            inserted.append(val)
            root_partial, _, _ = avl_build_steps(inserted)
            G, pos = draw_tree(root_partial)

            fig, ax = plt.subplots(figsize=(8, 5))
            nx.draw(G, pos, with_labels=True, arrows=False, node_size=1000,
                    node_color="lightgreen", font_size=10, font_weight="bold", ax=ax)
            ax.set_title(f"Step {k+1}: Insert {val}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(1)

        st.success("AVL Tree Construction Completed")


# ------- segment tree -------
elif choice == "Segment Tree":
    

    # ---------------- Notes / Theory ----------------
    st.subheader("Understanding Segment Tree")
    st.markdown("""
    A **Segment Tree** is a binary tree used for **range queries** and **updates**.  
    - Each **leaf node** represents a single element of the array.  
    - Each **internal node** stores information (like sum, min, max) for a **range of elements**.  

    **Applications**  
    - Range Sum Queries  
    - Range Minimum / Maximum Queries  
    - Interval Problems  

    **Time Complexity**  
    - Build: O(n)  
    - Query: O(log n)  
    - Update: O(log n)  
    """)

    # ---------------- Input Section ----------------

    st.subheader("Visualizing Segment Tree")

    if "segment_array" not in st.session_state:
        st.session_state.segment_array = []

    option = st.radio("Choose Input Method for Segment Tree:", ["Enter manually", "Generate Random Array"])

    if option == "Enter manually":
        user_input = st.text_input(
            "Enter numbers separated by commas (e.g. 1,3,5,7,9,11)",
            "1,3,5,7,9,11"
        )
        try:
            st.session_state.segment_array = [int(x.strip()) for x in user_input.split(",") if x.strip()]
            st.write("### Input Array:", st.session_state.segment_array)
        except ValueError:
            st.error("⚠️ Please enter only integers separated by commas.")
    else:
        size = st.slider("Array Size", 5, 15, 7, key="seg_size")
        if st.button("Generate Random Array 🎲", key="seg_generate"):
            st.session_state.segment_array = np.random.randint(1, 50, size).tolist()
        if st.session_state.segment_array:
            st.write("### Random Array:", st.session_state.segment_array)

    # ---------------- Visualization ----------------
    if st.session_state.segment_array and st.button("Start Segment Tree Visualization"):
        arr_copy = list(st.session_state.segment_array)
        tree, steps, explanations = segment_steps(arr_copy)

        chart = st.empty()
        explain_box = st.empty()

        

        built_nodes = set()

        for k, (idx, val) in enumerate(steps):
            built_nodes.add(idx)  # reveal one node per step

            G = nx.DiGraph()
            pos = {}

            def dfs(node_idx, x=0, y=0, layer=1):
                if node_idx not in built_nodes or node_idx >= len(tree) or tree[node_idx] is None:
                    return
                G.add_node(node_idx, label=str(tree[node_idx]))
                pos[node_idx] = (x, y)
                left, right = 2*node_idx+1, 2*node_idx+2
                if left in built_nodes:
                    G.add_edge(node_idx, left)
                    dfs(left, x - 1/layer, y - 1, layer+1)
                if right in built_nodes:
                    G.add_edge(node_idx, right)
                    dfs(right, x + 1/layer, y - 1, layer+1)

            dfs(0)
            labels = {n: str(tree[n]) for n in G.nodes}
            fig, ax = plt.subplots(figsize=(8,5))
            nx.draw(G, pos, with_labels=True, labels=labels, arrows=False,
                    node_size=1000, node_color="lightgreen", font_size=10, ax=ax)
            ax.set_title(f"Step {k+1}: Insert node {val}")
            chart.pyplot(fig)
            explain_box.info(explanations[k])
            time.sleep(0.8)

        st.success("Segment Tree Construction Completed")


# ---- DFS Visualization ----
elif choice == "DFS":
    st.header("Depth First Search (DFS)")

    st.markdown("""
    **Theory:**  
    Depth First Search (DFS) is a graph traversal algorithm that explores as far as possible along each branch before backtracking.  
    It uses a recursive or stack-based approach.

    - **Time Complexity:** O(V + E) where V = vertices, E = edges  
    - **Applications:** Topological sorting, detecting cycles, solving puzzles (mazes, Sudoku), connected components.
    """)

    # Input graph as adjacency list
    st.subheader("Enter Graph")
    graph_input = st.text_area("Enter adjacency list (format: A:B,C on each line)", "A:B,C\nB:D\nC:E\nD:\nE:")

    start_node = st.text_input("Enter Start Node", "A")

    if st.button("Run DFS"):
        # Parse input into adjacency list dictionary
        graph = {}
        for line in graph_input.strip().split("\n"):
            if ":" in line:
                node, neighbors = line.split(":")
                graph[node.strip()] = [n.strip() for n in neighbors.split(",") if n.strip()]
            else:
                graph[line.strip()] = []

        
        steps, explanations = dfs_build_steps(graph, start_node.strip())

        # Visualization
        # import networkx as nx
        # import matplotlib.pyplot as plt
        # import time

        chart = st.empty()
        explain_box = st.empty()

        G = nx.DiGraph(graph)
        pos = nx.spring_layout(G, seed=42)  # consistent layout

        visited_nodes = set()

        for i, node in enumerate(steps):
            visited_nodes.add(node)

            fig, ax = plt.subplots(figsize=(6, 4))
            nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=1000, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color="lightblue", node_size=1000, ax=ax)

            ax.set_title(f"Step {i+1}: {explanations[i]}")
            chart.pyplot(fig)
            explain_box.info(explanations[i])
            time.sleep(0.8)

        st.success("DFS Traversal Completed ")

# ----- BFS -----

elif choice == "BFS":
    st.header("Breadth First Search (BFS)")

    st.markdown("""
    **Theory:**  
    Breadth First Search (BFS) is a graph traversal algorithm that explores neighbors level by level, using a queue.  
    It ensures that the shallowest nodes are visited first before deeper nodes.

    - **Time Complexity:** O(V + E) where V = vertices, E = edges  
    - **Applications:** Shortest path in unweighted graphs, web crawling, peer-to-peer networks, GPS navigation.
    """)

    # Input graph as adjacency list

    st.subheader("Enter Graph")
    graph_input = st.text_area("Enter adjacency list (format: A:B,C on each line)", "A:B,C\nB:D,E\nC:F\nD:\nE:\nF:")

    start_node = st.text_input("Enter Start Node", "A")

    if st.button("Run BFS"):
        # Parse input into adjacency list dictionary
        graph = {}
        for line in graph_input.strip().split("\n"):
            if ":" in line:
                node, neighbors = line.split(":")
                graph[node.strip()] = [n.strip() for n in neighbors.split(",") if n.strip()]
            else:
                graph[line.strip()] = []

        
        steps, explanations = bfs_build_steps(graph, start_node.strip())

        # Visualization
        

        chart = st.empty()
        explain_box = st.empty()

        G = nx.DiGraph(graph)
        pos = nx.spring_layout(G, seed=42)  # consistent layout

        visited_nodes = set()

        for i, node in enumerate(steps):
            visited_nodes.add(node)

            fig, ax = plt.subplots(figsize=(6, 4))
            nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=1000, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color="lightgreen", node_size=1000, ax=ax)

            ax.set_title(f"Step {i+1}: {explanations[i]}")
            chart.pyplot(fig)
            explain_box.info(explanations[i])
            time.sleep(0.8)

        st.success("BFS Traversal Completed ")


#------ Dijkstra -----
elif choice == "Dijkstra":
    st.header("Dijkstra's Algorithm")

    st.markdown("""
    **Theory:**  
    Dijkstra's Algorithm is a shortest path algorithm for weighted graphs with **non-negative edge weights**.  
    It uses a priority queue (min-heap) to always expand the nearest unvisited node first.

    - **Time Complexity:** O((V + E) log V) with a min-heap  
    - **Applications:** GPS navigation, network routing, pathfinding in games.
    """)

    # Input graph as weighted adjacency list
    st.subheader("Enter Weighted Graph")
    graph_input = st.text_area("Enter adjacency list (format: A:B:4,C:2 on each line)", "A:B:4,C:2\nB:D:5\nC:D:8,E:10\nD:E:2\nE:")

    start_node = st.text_input("Enter Start Node", "A")

    if st.button("Run Dijkstra"):
        # Parse graph input into dictionary
        graph = {}
        for line in graph_input.strip().split("\n"):
            if ":" in line:
                parts = line.split(":")
                node = parts[0].strip()
                neighbors = parts[1:]
                graph[node] = {}
                for n in neighbors:
                    if n.strip():
                        neigh, weight = n.split(",")[0], n.split(",")[-1] if "," in n else n
                # Parse format "B:4,C:2"
                node, rest = line.split(":")[0].strip(), line.split(":")[1:]
                graph[node] = {}
                if rest:
                    for neigh_part in ":".join(rest).split(","):
                        if neigh_part.strip():
                            neigh, weight = neigh_part.split(":")
                            graph[node][neigh.strip()] = int(weight.strip())
            else:
                graph[line.strip()] = {}

        
        steps, explanations, distances = dijkstra_build_steps(graph, start_node.strip())

        # Visualization

        chart = st.empty()
        explain_box = st.empty()

        G = nx.DiGraph()
        for u in graph:
            for v, w in graph[u].items():
                G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G, seed=42)

        visited_nodes = set()

        for i, node in enumerate(steps):
            visited_nodes.add(node)

            fig, ax = plt.subplots(figsize=(6, 4))
            edge_labels = nx.get_edge_attributes(G, "weight")

            nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=1000, ax=ax)
            nx.draw_networkx_nodes(G, pos, nodelist=visited_nodes, node_color="lightblue", node_size=1000, ax=ax)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

            ax.set_title(f"Step {i+1}: {explanations[i]}")
            chart.pyplot(fig)
            explain_box.info(explanations[i])
            time.sleep(1)

        st.success("Dijkstra Completed")
        st.write("Final Distances:", distances)


# ------- Kruskal's Algorithm -------

elif choice == "Kruskal":
    st.header("Kruskal's Algorithm - Minimum Spanning Tree")

    st.markdown("""
    **Theory:**  
    Kruskal’s Algorithm finds a **Minimum Spanning Tree (MST)** for a connected, weighted, undirected graph.  
    It sorts edges by weight and adds them one by one, **avoiding cycles** using the Disjoint Set Union (DSU).

    - **Time Complexity:** O(E log E)  
    - **Applications:** Network design, clustering, road construction planning.
    """)

    st.subheader("Enter Graph Edges")
    st.markdown("Format: u v w (each edge on new line)")

    edge_input = st.text_area("Enter edges:", "0 1 4\n0 2 3\n1 2 1\n1 3 2\n2 3 4\n3 4 2\n4 5 6")
    num_nodes = st.number_input("Number of vertices", min_value=1, value=6, step=1)

    if st.button("Run Kruskal"):
        edges = []
        for line in edge_input.strip().split("\n"):
            u, v, w = map(int, line.split())
            edges.append((w, u, v))

        
        steps, explanations = kruskal_build_steps(edges, num_nodes)

        # Visualization
        chart = st.empty()
        explain_box = st.empty()

        G = nx.Graph()
        for w, u, v in edges:
            G.add_edge(u, v, weight=w)

        pos = nx.spring_layout(G, seed=42)
        edge_labels = nx.get_edge_attributes(G, "weight")

        mst_edges = set()

        for i, (curr_edges, explanation) in enumerate(zip(steps, explanations)):
            fig, ax = plt.subplots(figsize=(6, 4))
            mst_edges = [(u, v) for (u, v, w) in curr_edges]

            nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=800, ax=ax)
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

            # highlight MST edges
            nx.draw_networkx_edges(G, pos, edgelist=mst_edges, edge_color="blue", width=3, ax=ax)

            ax.set_title(f"Step {i+1}: {explanation}")
            chart.pyplot(fig)
            explain_box.info(explanation)
            time.sleep(1)

        st.success("Kruskal Completed")


# ---- quiz ----- 
algo_name = choice  
questions = quiz_data[choice]

ALGORITHM_SECTIONS = {
    "Sorting": ["Bubble Sort", "Insertion Sort", "Heap Sort", "Quick Sort"],
    "Trees": ["Binary Search Tree", "AVL Tree", "Segment Tree"],
    "Graphs": ["DFS", "BFS", "Dijkstra", "Kruskal"],
    # "Dynamic Programming": ["Knapsack", "LCS", "Floyd Warshall"]
}

if algo_name not in st.session_state.quiz_progress:
    st.session_state.quiz_progress[algo_name] = {
        "answered": 0,
        "total": len(questions)
    }

# ---------------- XP + Progress Function ----------------
def check_answer(selected, correct, algo_name):
    if selected == correct:
        st.success("✅ Correct!")
        st.session_state.xp += 1
    else:
        st.error("❌ Wrong!")

    # Update progress
    st.session_state.quiz_progress[algo_name]["answered"] += 1

    # Check if quiz finished
    if st.session_state.quiz_progress[algo_name]["answered"] == st.session_state.quiz_progress[algo_name]["total"]:
        if algo_name not in st.session_state.completed_algorithms:
            st.session_state.xp += 100
            st.session_state.completed_algorithms.add(algo_name)
            st.balloons()
            st.info(f"🎉 You completed {algo_name}! (+100 XP)")

    for section, algos in ALGORITHM_SECTIONS.items():
        if algo_name in algos:  # find section of current algo
            if all(a in st.session_state.completed_algorithms for a in algos):
                if section not in st.session_state.completed_sections:
                    st.session_state.xp += 200
                    st.session_state.completed_sections.add(section)
                    st.success(f"🔥 {section} section completed! (+200 XP)")

# ---------------- QUIZ LOGIC ----------------
if "quiz_started" not in st.session_state:
    st.session_state.quiz_started = False
if "current_q" not in st.session_state:
    st.session_state.current_q = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "selected_algo" not in st.session_state:
    st.session_state.selected_algo = choice

# Reset state if algorithm changes
if st.session_state.selected_algo != choice:
    st.session_state.quiz_started = False
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.selected_algo = choice

st.header(f"{choice} Quiz")

if not st.session_state.quiz_started:
    if st.button("Start Quiz"):
        st.session_state.quiz_started = True
else:
    if st.session_state.current_q < len(questions):
        q = questions[st.session_state.current_q]

        st.subheader(f"Q{st.session_state.current_q+1}: {q['question']}")
        selected_option = st.radio(
            "Options", q["options"], key=f"{algo_name}_{st.session_state.current_q}"
        )

        if st.button("Next"):
            # ✅ Call XP + Progress update here
            check_answer(selected_option, q["answer"], algo_name)  #, "sorting"

            # Keep quiz score as well
            if selected_option == q["answer"]:
                st.session_state.score += 1

            st.session_state.current_q += 1
            st.rerun()
    else:
        st.success(f"🎉 Quiz Finished! Your Score: {st.session_state.score}/{len(questions)}")
        if st.button("Restart Quiz"):
            st.session_state.quiz_started = False
            st.session_state.current_q = 0
            st.session_state.score = 0
            st.session_state.quiz_progress[algo_name]["answered"] = 0
            st.rerun()




# Landing Page for XP

def landing_page():
    st.title("🏆 My Progress Dashboard")
    st.markdown(f"### Current XP: **{st.session_state.xp}**")

    # Progress bar (example leveling system)
    level = st.session_state.xp // 1000 + 1
    st.progress(st.session_state.xp % 1000 / 1000)

    st.subheader(f"🎯 Level {level}")
    st.write("✅ Completed Algorithms:", list(st.session_state.completed_algorithms))
    st.write("✅ Completed Sections:", list(st.session_state.completed_sections))
    st.write("✅ Completed Quizzes:", list(st.session_state.completed_quizzes))

with st.sidebar:
    st.header("Dashboard")
    # bubble sort, insertion sort, etc.
    if st.button("🏆 My XP"):
        landing_page()

