import unittest
# Assumption the provided array is sorted and rotatable
# Sample array:
# words = [
#     'ptolemaic',
#     'retrograde',
#     'supplant',
#     'undulate',
#     'xenoepist',
#     'asymptote',  # <-- rotates here!
#     'babka',
#     'banoffee',
#     'engender',
#     'karpatka',
#     'othellolagkage',
# ]

def find_rotation_point(words):
    # Find the rotation point in the list
  # Solution start
    first_word = words[0]
    low=0
    high = len(words)-1
    
    while low < high:
        mid=(low+high)//2
        if words[mid]>=first_word:
            # Rotation point is to the right
            low=mid+1
        else:
            # Rotation point is to the left or at mid
            high=mid
    return low
  # Solution end

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
