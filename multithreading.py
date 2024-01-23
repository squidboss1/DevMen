import threading
import multiprocessing
import random
import time


def bubble_sort(arr):
    n = len(arr)
    swapped = False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            return


def threaded_sort(data_to_sort, sorting_function, number_of_threads):
    list_of_threads_objects = []
    data_size_sum = len(data_to_sort)
    data_portion_for_each_thread = data_size_sum // number_of_threads

    for i in range(number_of_threads):
        start_index = i * data_portion_for_each_thread
        end_index = start_index + data_portion_for_each_thread if i < number_of_threads - 1 else data_size_sum
        thread = threading.Thread(target=sorting_function, args=(data_to_sort[start_index:end_index],))
        list_of_threads_objects.append(thread)
        thread.start()

    for thread in list_of_threads_objects:
        thread.join()


def multiprocess_sort(data_to_sort, sorting_function, number_of_processes):
    with multiprocessing.Pool(processes=number_of_processes) as pool:
        pool.map(sorting_function, data_to_sort)


def measure_sorting_time(data_to_sort, sorting_function, number_of_threads, number_of_processes):
    start_time_threads = time.time()

    if number_of_threads < 1:
        sorting_function(data_to_sort.copy())
    else:
        threaded_sort(data_to_sort.copy(), sorting_function, number_of_threads)

    end_time_threads = time.time()
    elapsed_time_threads = end_time_threads - start_time_threads

    start_time_processes = time.time()

    if number_of_processes < 1:
        sorting_function(data_to_sort.copy())
    else:
        multiprocess_sort(data_to_sort.copy(), sorting_function, number_of_processes)

    end_time_processes = time.time()
    elapsed_time_processes = end_time_processes - start_time_processes

    return elapsed_time_threads, elapsed_time_processes


if __name__ == "__main__":
    number_of_arrays = 10
    array_size = 100
    data = [[random.randint(1, 1000) for _ in range(array_size)] for _ in range(number_of_arrays)]

    num_threads = 2
    num_processes = 2

    time_threads, time_processes = measure_sorting_time(data, bubble_sort, num_threads, num_processes)

    print(f"Time with {num_threads} threads: {time_threads} seconds")
    print(f"Time with {num_processes} processes: {time_processes} seconds")

    time_difference = abs(time_threads - time_processes)
    print(f"Difference in time: {time_difference} seconds")
