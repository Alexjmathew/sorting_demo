from flask import Flask, render_template, request
import time

app = Flask(__name__)

# Sorting Algorithms Implementations
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def measure_time(sort_func, arr):
    start_time = time.time()
    sorted_arr = sort_func(arr.copy())
    end_time = time.time()
    return sorted_arr, end_time - start_time

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_numbers = request.form['numbers']
        try:
            numbers = [int(num) for num in input_numbers.split(',')]
            
            # Measure sorting performance
            bubble_sorted, bubble_time = measure_time(bubble_sort, numbers)
            quick_sorted, quick_time = measure_time(quick_sort, numbers)
            
            return render_template('index.html',
                               original=numbers,
                               bubble_sorted=bubble_sorted,
                               quick_sorted=quick_sorted,
                               bubble_time=f"{bubble_time:.6f}",
                               quick_time=f"{quick_time:.6f}")
        except ValueError:
            error = "Please enter comma-separated numbers (e.g., 5,3,8,1,2)"
            return render_template('index.html', error=error)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
