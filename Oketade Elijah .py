  1.       try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
   
 2.       try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content) 
            except PermissionError:
        print("Error: Permission denied!")
        
 3.        try:
    account.withdraw(1500)
except InsufficientBalanceError as e:
    print("Error:", str(e))


4. try:
        result = a + b
        print("Result:", result)
    except TypeError:
        print("Error: Invalid data type!")

5. try:
        large_list = [i for i in range(10**9)]
    except MemoryError:
        print("Error: Out of memory!")

6. try:
        sys.exit(0)
    except SystemExit:
        print("Error: Program exit!")

7.try:
        recursive_function(n-1)
    except RuntimeError:
        print("Error: Maximum recursion depth exceeded!")
  
  8.    try:
        result = dct[key]
        print("Result:", result)
    except KeyError:
        print("Error: Key not found!")

9.  try:
    input("Press Enter to continue...")
    raise EOFError
except EOFError:
    print("Error: End of file!")
```
10. try:
    print(person.age)
except AttributeError:
    print("Error: Attribute not found!")
