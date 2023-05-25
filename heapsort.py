# import heapq

# # Function to perform the sorting using
# # heaop sort
# def heap_sort(arr):
# 	heapq.heapify(arr)
# 	result = []
# 	while arr:
# 		result.append(heapq.heappop(arr))
# 	return result

# # Driver Code
# arr = [60, 20, 40, 70, 30, 10]
# print("Input Array: ", arr)
# print("Sorted Array: ", heap_sort(arr))
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    result= []
    while arr:
        result.append(heapq.heappop(arr))
    return result

arr = [2,43,546,2,23,2,222,22]
print("input array is:",arr)
print("sorted array is:",heap_sort(arr))