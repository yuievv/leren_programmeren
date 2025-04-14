def hello_function_town(times: int) -> str:
    return '\n'.join([f"Hello from function town {i + 1}!" for i in range(times)])

print(hello_function_town(3))
print(hello_function_town(10))
