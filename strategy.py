import abc


class SortingStrategy(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def sort(self, values):
		pass

class BubbleSort(SortingStrategy):
	def sort(self, values):
		for num in range(len(values)-1, 0, -1):
			for i in range(num):
				if values[i] > values[i+1]:
					temp = values[i]
					values[i] = values[i+1]
					values[i+1] = temp

class QuickSort(SortingStrategy):
	def sort(self, values):
		print("quick")