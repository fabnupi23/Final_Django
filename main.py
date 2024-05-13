  def binary_search(arr, target):
      low, high = 0, len(arr) - 1
      while low <= high:   # O(log n)
          mid = (low + high) // 2
          if arr[mid] == target:   # O(1)
              return mid   # O(1)
          elif arr[mid] < target:
              low = mid + 1   # O(1)
          else:
              high = mid - 1   # O(1)
      return -1   # O(1)
