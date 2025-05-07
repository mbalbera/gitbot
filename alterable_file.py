my_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(test, group) for group in chunks_of_five(my_array)]

    for future in as_completed(futures):
        result = future.result()
