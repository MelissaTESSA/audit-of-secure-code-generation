Given a list of integers and an index to insert a new element, write a function to insert the element at the given index and shift the remaining elements to the right. You should not create a new list or use any built-in functions like `insert` or `append`. Function signature: `def insert_element(lst: list, index: int, element: int) -> list:`.
-----Examples-----
Input:
insert_element([1, 2, 3, 4], 1, 99)
Output:
[1, 99, 2, 3, 4]

Input:
insert_element([10, 20, 30], 3, 40)
Output:
[10, 20, 30, 40]

Input:
insert_element([100, 200], 0, 300)
Output:
[300, 100, 200]
