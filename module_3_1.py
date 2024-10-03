calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [s.lower() for s in list_to_search]


print(string_info("Hello"))  # Output: (5, 'HELLO', 'hello')
print(is_contains("Urban", ["urbAn", "city", "town"]))  # Output: True
print(is_contains("Urban", ["city", "town"]))  # Output: False

print("Total function calls:", calls)  # Output: Total function calls: 3