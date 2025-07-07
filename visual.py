import matplotlib.pyplot as plt
import numpy as np

# Helper function to update the plot
def update_plot(bars, arr, highlight=[]):
    for bar, val in zip(bars, arr):
        bar.set_height(val)
        bar.set_color('red' if val in highlight else 'blue')
    plt.pause(0.1)

# Bubble Sort
def bubble_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title("Bubble Sort Visualization")
    
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            update_plot(bars, arr, highlight=[arr[j], arr[j + 1]])

    plt.show()

# Selection Sort
def selection_sort_visualize(arr):
    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title("Selection Sort Visualization")

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            update_plot(bars, arr, highlight=[arr[j], arr[min_idx]])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_plot(bars, arr, highlight=[arr[i]])

    plt.show()

# Insertion Sort
def insertion_sort_visualize(arr):
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title("Insertion Sort Visualization")

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            update_plot(bars, arr, highlight=[arr[j]])
            j -= 1
        arr[j + 1] = key
        update_plot(bars, arr, highlight=[arr[j + 1]])

    plt.show()

# Quick Sort
def quick_sort_visualize(arr, bars=None, start=0, end=None):
    if end is None:
        fig, ax = plt.subplots()
        bars = ax.bar(range(len(arr)), arr, color='blue')
        ax.set_title("Quick Sort Visualization")
        end = len(arr)

    if start < end - 1:
        pivot_index = partition(arr, start, end, bars)
        quick_sort_visualize(arr, bars, start, pivot_index)
        quick_sort_visualize(arr, bars, pivot_index + 1, end)

def partition(arr, start, end, bars):
    pivot = arr[end - 1]
    i = start
    for j in range(start, end - 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        update_plot(bars, arr, highlight=[arr[j], arr[end - 1]])
    arr[i], arr[end - 1] = arr[end - 1], arr[i]
    update_plot(bars, arr, highlight=[arr[i]])
    return i

# Heap Sort
def heap_sort_visualize(arr):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[l] > arr[largest]:
            largest = l
        if r < n and arr[r] > arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            update_plot(bars, arr, highlight=[arr[i], arr[largest]])
            heapify(n, largest)

    n = len(arr)
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr, color='blue')
    ax.set_title("Heap Sort Visualization")

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        update_plot(bars, arr, highlight=[arr[i]])
        heapify(i, 0)

    plt.show()

# Test and visualize all sorts
data = np.random.randint(1, 50, 20)  # Generate random array

bubble_sort_visualize(data.copy())
selection_sort_visualize(data.copy())
insertion_sort_visualize(data.copy())
# merge_sort_visualize(data.copy())
quick_sort_visualize(data.copy())
heap_sort_visualize(data.copy())