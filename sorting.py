import abc
import random
import sys
import time
from strategy import BubbleSort

class SortingContext:
	def __init__(self, sorting_strategy):
		self._sorting_strategy = sorting_strategy

	def sort(self, list):
		print("Unsorted list: ", list)
		sorting_start = time.time()
		self._sorting_strategy.sort(list)
		sorting_finish = time.time()
		elapsed_time = sorting_finish - sorting_start
		print("Sorted list:   ", list)
		print("Sorting took %f seconds to complete" % elapsed_time)

def main():
	bubble_sort = BubbleSort()	

	list = [random.randint(1, 101) for i in range(int(sys.argv[1]))]

	if sys.argv[2] == "bubble":
		sorting_algorithm = SortingContext(bubble_sort)
		sorting_algorithm.sort(list)

if __name__ == "__main__":
	main()
