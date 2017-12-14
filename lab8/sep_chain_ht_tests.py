import unittest
import sep_chain_ht
class TestLab8(unittest.TestCase):
    def test_MyHashTable(self):
        h1 = sep_chain_ht.MyHashTable()
        hash_table = [[]for i in range(11)]
        self.assertEqual(h1.table_size,11)
        self.assertEqual(h1.size, 0)
        self.assertEqual(h1.collisions, 0)
        self.assertEqual(h1.hash_table,hash_table)
    def test_insert(self):
        h1 = sep_chain_ht.MyHashTable()
        h1.insert(0,'a')
        h1.insert(1,'b')
        h1.insert(11,'c')
        self.assertEqual(h1.hash_table[0][0],(0,'a'))
        self.assertEqual(h1.hash_table[0][1],(11,'c'))
        h1.insert(11,'d')
        self.assertEqual(h1.hash_table[0][1],(11,'d'))
        self.assertEqual(h1.hash_table[1][0],(1,'b'))

    def test_remove(self):
        h1 = sep_chain_ht.MyHashTable()
        h1.insert(1,'t')
        h1.insert(15,'w')      
        h1.insert(12,'q')
        self.assertEqual(h1.remove(15),(15,'w'))
        self.assertEqual(h1.get_size(),2)
        self.assertEqual(h1.hash_table[1][1],(12,'q'))
        self.assertEqual(h1.hash_table[1][0],(1,'t'))
        with self.assertRaises(LookupError):
            h1.remove(15)
    def test_get(self):
        h1 = sep_chain_ht.MyHashTable()
        h1.insert(1,'x')
        h1.insert(4,'y')
        self.assertEqual(h1.get(1),(1,'x'))
        self.assertEqual(h1.get(4),(4,'y'))
        with self.assertRaises(LookupError):
            h1.get(2)
    def test_get_size(self):
        h1 = sep_chain_ht.MyHashTable()
        h1.insert(4,'a')
        h1.insert(14,'b')
        h1.insert(2,'c')
        self.assertEqual(h1.get_size(),3)

    def test_get_collisions(self):
        h1 = sep_chain_ht.MyHashTable()
        h1.insert(1,'b')
        h1.insert(1,'v')
        h1.insert(12,'m')
        self.assertEqual(h1.get_collisions(),2)

if __name__ == "__main__":
    unittest.main()
