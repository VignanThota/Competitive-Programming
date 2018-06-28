import unittest


def contains(n, m):
    l=len(n)
    low=n[0]
    high=n[l-1]
    mid=n[l//2]
    flag=0
    if m in n:
		while (flag!=1):
		    if mid == m:
		        print('found at location : ',n.index(mid))
		        flag=1
		        return True
		    elif m>mid:
		        low=n[n.index(mid)+1]
		        mid=n[((n.index(low))+(l-1))//2]
		        if mid==m:
		            print('found at location : ',n.index(mid))
		            flag=1
		            return True
		    elif m<mid:
		        high=n[n.index(mid)-1]
		        mid=n[((n.index(low))+(n.index(high)))//2]
		        if mid==m:
		            print('found at location : ',n.index(mid))
		            flag=1
		            return True
    else:
	    print('element not available in list')
	    return False
    return False


















# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)
