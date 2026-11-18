from typing import List, Any

def insertionSort(lst: List[Any]) -> List[Any]:
    for i in range(len(lst)):
        j = i - 1
        while j >= 0:
            if lst[j] > lst[i]:
                tmp = lst[j]
                lst[j] = lst[i]
                lst[i] = tmp
                i -= 1
            j -= 1
    return lst

def sort_words(words: List[str]) -> List[str]:
    return insertionSort(words)

def sort_numbers(numbers: List[int]) -> List[int]:
    return insertionSort(numbers)

def sort_decimals(numbers: List[float]) -> List[float]:
    return insertionSort(numbers)



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
