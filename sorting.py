import abc
import random
import sys
import time
from strategy import BubbleSort
from strategy import QuickSort
from strategy import SelectionSort

class SortingContext:
	def __init__(self, sorting_strategy):
		self._sorting_strategy = sorting_strategy

	def sort(self, values):
		print("Unsorted values: ", values)
		
		print("%s is sorting the values" % self._sorting_strategy.label)

		sorting_start = time.time()
		self._sorting_strategy.sort(values)
		sorting_finish = time.time()
		elapsed_time = sorting_finish - sorting_start
		
		print("Sorted values: ", values)
		
		print("Sorting took %f seconds to complete" % elapsed_time)

def main():
	values = [random.randint(1, 100) for i in range(int(sys.argv[1]))]

	sorting_algorithm = None

	if sys.argv[2] == "bubble":
		sorting_algorithm = SortingContext(BubbleSort())
	elif sys.argv[2] == "quick":
		sorting_algorithm = SortingContext(QuickSort())
	elif sys.argv[2] == "selection":
		sorting_algorithm = SortingContext(SelectionSort())
	else:
		sys.exit("You have to specify a valid sorting algorithm!")
	
	sorting_algorithm.sort(values)

if __name__ == "__main__":
	main()
