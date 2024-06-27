class UniqueNumbers:
  def __init__(self, nums):
      self.nums = nums
      self.unique_nums = []

  def remove_duplicates(self):
      for num in self.nums:
          if num not in self.unique_nums:
              self.unique_nums.append(num)

  def get_unique_numbers(self):
      self.remove_duplicates()
      return self.unique_nums

# Example usage:
nums = [1, 2, 3, 3, 4, 5, 34, 5, 6, 6]
unique_numbers = UniqueNumbers(nums)
print(unique_numbers.get_unique_numbers())

