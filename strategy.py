import abc

class SortingStrategy(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def sort(self, values):
		pass

class BubbleSort(SortingStrategy):
	label = "Bubble Sort"

	def sort(self, values):
		for num in range(len(values)-1, 0, -1):
			for i in range(num):
				if values[i] > values[i+1]:
					temp = values[i]
					values[i] = values[i+1]
					values[i+1] = temp

class QuickSort(SortingStrategy):
	label = "Quick Sort"

	def sort(self, values):
		QuickSort.sort_helper(values, 0, len(values)-1)

	def sort_helper(values, first, last):
		if first < last:
			split_point = QuickSort.partition(values, first, last)

			QuickSort.sort_helper(values, first, split_point-1)
			QuickSort.sort_helper(values, split_point+1, last)

	def get_pivot(values, first, last):
		mid = (first + last) // 2
		pivot = last

		if values[first] < values[mid]:
			if values[mid] < values[last]:
				pivot = mid
			elif values[first] < values[last]:
				pivot = first

		return pivot

	def partition(values, first, last):
		pivot_index = QuickSort.get_pivot(values, first, last)
		pivot_value = values[pivot_index]
		values[pivot_index], values[first] = values[first], values[pivot_index]
		border = first

		for i in range(first, last+1):
			if values[i] < pivot_value:
				border += 1
				values[i], values[border] = values[border], values[i]
		values[first], values[border] = values[border], values[first]

		return border
