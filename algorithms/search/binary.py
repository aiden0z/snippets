import random
from typing import List


class BinarySearch:

    def sort(self, array: List):
        new = array[:]
        self._quick_sort(new, 0, len(array) - 1)
        return new

    def _quick_sort(self, array: List, low: int, high: int):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)

    def _partition(self, array: List, low: int, high: int):
        i = low - 1
        pivot = array[high]

        for j in range(low, high):
            if array[j] < pivot:
                i = i + 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def search(self, array: List, target: int):
        array = self.sort(array)
        return array, self._binary_search(array, 0, len(array), target)

    def _binary_search(self, array: List, low: int, high: int, target: int):
        while low <= high:
            mid = (low + high) // 2
            print((low, high), mid)
            if array[mid] > target:
                high = mid - 1
            elif array[mid] < target:
                low = mid + 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    array = random.choices(range(100), k=10)
    target = array[random.choice(range(0, len(array) - 1))]
    print(f"search target {target} in array {array}\n", BinarySearch().search(array, target))
