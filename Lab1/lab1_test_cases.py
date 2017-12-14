import unittest
import lab1

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        tlist = [10, 9, 5 ,4, 9]
        self.assertEqual(lab1.max_list_iter(tlist),10)
        tlist = []
        with self.assertRaises(ValueError):  # magic - uses context manager
            lab1.max_list_iter(tlist)  

    def test_reverse_rec(self):
        self.assertEqual(lab1.reverse_rec("abcd"),"dcba")

    def test_bin_search(self): #a mid of 0 which should return the first index
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-5
        self.assertEqual( lab1.bin_search(0, 0, len(list_val)-5, list_val), 0 )
    
    def test_bin_search2(self): #an empty list which should return none
        list_val =[]
        low = 0
        high = 0
        self.assertEqual( lab1.bin_search(4, 0, 0, list_val), None )
    
    def test_bin_search3(self): # testing the whole list and finding the 4 in the list
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(4,0, len(list_val)-1,  list_val), 4 )
    
    def test_bin_search4(self):  # the target is the index of the mid
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(2, 0, len(list_val)-8, list_val),2  )
    
    def test_bin_search5(self):  # the target is not in the list
        list_val =[0,1,2,3,4,5,6,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual( lab1.bin_search(12, 0, len(list_val)-1, list_val),None  )
if __name__ == "__main__":
        unittest.main()

    
