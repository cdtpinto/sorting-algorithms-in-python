import abc

class SortingStrategy(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def sort(self, values):
		pass

class BubbleSort(SortingStrategy):
	label = "Bubble Sort"

	def sort(self, values):
		for i in range(len(values)):
			for j in range(0, len(values)-i-1):
				if values[j] > values[j+1]:
					values[j], values[j+1] = values[j+1], values[j]

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

class SelectionSort(SortingStrategy):
	label = "Selection Sort"

	def sort(self, values):
		for i in range(len(values)):
			min_index = i
			for j in range(i+1, len(values)):
				if values[min_index] > values[j]:
					min_index = j
			values[i], values[min_index] = values[min_index], values[i]
