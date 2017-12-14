import unittest
from  queues import QueueArray
from queues import QueueLinked

class TestQueueArray(unittest.TestCase):
   def test_num_in_queue(self):
       stk_a = QueueArray(10)
       stk_a.enqueue(3)
       self.assertEqual(stk_a.dequeue(), 3 )
       self.assertTrue(stk_a.is_empty())


   def test_2(self):
       stk_a = QueueArray(4)
       with self.assertRaises(IndexError):
           stk_a.dequeue()
       stk_a.enqueue(6)
       stk_a.enqueue(7)
       stk_a.enqueue(9)
       self.assertEqual(stk_a.dequeue(), 6)
       self.assertEqual(stk_a.dequeue(), 7)
       self.assertEqual(stk_a.dequeue(), 9)       

   def test_num_3(self):
       stk_a = QueueArray(4)
       stk_a.enqueue(6)
       stk_a.enqueue(7)
       stk_a.enqueue(8)
       stk_a.enqueue(9)
       self.assertTrue(stk_a.is_full())
       with self.assertRaises(IndexError):
           stk_a.enqueue(0)
       self.assertEqual(stk_a.num_in_queue(), 4 )
       self.assertEqual(stk_a.dequeue(), 6)
       self.assertEqual(stk_a.num_in_queue(), 3 )
       self.assertFalse(stk_a.is_empty())
 
   def test_linked(self):
       stk_a = QueueLinked(4)
       stk_a.enqueue(3)
       self.assertEqual(stk_a.num_in_queue(),1)
       self.assertEqual(stk_a.dequeue(), 3 )
       self.assertTrue(stk_a.is_empty())
   def test_linked2(self):
       stk_a = QueueLinked(4)
       with self.assertRaises(IndexError):
           stk_a.dequeue()
       stk_a.enqueue(6)
       stk_a.enqueue(7)
       stk_a.enqueue(9)
       self.assertEqual(stk_a.num_in_queue(),3)
       self.assertEqual(stk_a.dequeue(), 6)
       self.assertEqual(stk_a.num_in_queue(), 2)
       self.assertEqual(stk_a.dequeue(), 7)
       self.assertEqual(stk_a.dequeue(), 9)


if __name__ == "__main__":
    unittest.main()

