import abc

class SortingStrategy(metaclass=abc.ABCMeta):

	@abc.abstractmethod
	def sort(self, list):
		pass

class BubbleSort(SortingStrategy):
	def sort(self, list):
		for num in range(len(list)-1, 0, -1):
			for i in range(num):
				if list[i] > list[i+1]:
					temp = list[i]
					list[i] = list[i+1]
					list[i+1] = temp
