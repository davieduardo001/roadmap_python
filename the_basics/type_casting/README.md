Type casting in Python refers to converting a variable from one data type to another. Python provides built-in functions for type casting:

1. **Integer (`int()`)**: Converts a variable to an integer.
   ```python
   x = int(5.6)  # x becomes 5
   y = int("10")  # y becomes 10
   ```

2. **Float (`float()`)**: Converts a variable to a floating-point number.
   ```python
   x = float(3)  # x becomes 3.0
   y = float("5.67")  # y becomes 5.67
   ```

3. **String (`str()`)**: Converts a variable to a string.
   ```python
   x = str(10)  # x becomes '10'
   y = str(3.14)  # y becomes '3.14'
   ```

4. **List (`list()`)**: Converts an iterable (like a string or a tuple) to a list.
   ```python
   x = list("abc")  # x becomes ['a', 'b', 'c']
   y = list((1, 2, 3))  # y becomes [1, 2, 3]
   ```

5. **Tuple (`tuple()`)**: Converts an iterable to a tuple.
   ```python
   x = tuple([1, 2, 3])  # x becomes (1, 2, 3)
   ```

6. **Set (`set()`)**: Converts an iterable to a set (removes duplicates).
   ```python
   x = set([1, 2, 2, 3])  # x becomes {1, 2, 3}
   ```

7. **Boolean (`bool()`)**: Converts a value to a boolean (`True` or `False`).
   ```python
   x = bool(1)  # x becomes True
   y = bool(0)  # y becomes False
   ```

Type casting is useful when dealing with data that needs to be processed in a specific format.