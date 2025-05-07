from concurrent.futures import ThreadPoolExecutor, as_completed

def chunks_of_five(arr):
    for i in range(0, len(arr), 5):
        yield arr[i:i + 5]


my_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(test, group) for group in chunks_of_five(my_array)]

    for future in as_completed(futures):
        result = future.result()
