import unittest
from src.priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_push_pop(self):
        self.pq.push("item1", 1)
        self.pq.push("item2", 2)
        self.assertEqual(self.pq.pop(), "item2")
        self.assertEqual(self.pq.pop(), "item1")

    def test_peek(self):
        self.pq.push("item1", 1)
        self.pq.push("item2", 2)
        self.assertEqual(self.pq.peek(), "item2")
        self.assertEqual(self.pq.size(), 2)

    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.pq.push("item1", 1)
        self.assertFalse(self.pq.is_empty())

    def test_size(self):
        self.assertEqual(self.pq.size(), 0)
        self.pq.push("item1", 1)
        self.pq.push("item2", 2)
        self.assertEqual(self.pq.size(), 2)

    def test_pop_empty(self):
        with self.assertRaises(IndexError):
            self.pq.pop()

    def test_peek_empty(self):
        with self.assertRaises(IndexError):
            self.pq.peek()

if __name__ == "__main__":
    unittest.main()
