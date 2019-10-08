import random


class QuickSort:

    def sort(self, array: list):
        new = array[:]
        self._quick_sort(new, 0, len(array) - 1)
        return new

    def _quick_sort(self, array: list, low: int, high: int):
        if low < high:
            pi = self._partition(array, low, high)
            self._quick_sort(array, low, pi - 1)
            self._quick_sort(array, pi + 1, high)

    def _partition(self, array: list, low: int, high: int):
        i = low - 1
        # pivot can pick in different ways:
        # 1. Always pick first element as pivot.
        # 2. Always pick last element as pivot (implemented below).
        # 3. Pick a random element as pivot.
        # 4. Pick median as pivot.
        pivot = array[high]

        for j in range(low, high):
            # if current element is smaller than the pivot
            if array[j] < pivot:
                # increment index of smaller element
                i = i + 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1


if __name__ == '__main__':
    array = random.choices(range(100), k=10)
    assert sorted(array) == QuickSort().sort(array)
