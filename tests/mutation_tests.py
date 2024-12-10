import sys
import os

sys.path.insert(0,os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from priority_queue import PriorityQueue
class MutationTestCases(unittest.TestCase):
    def setUp(self):
        self.pq = PriorityQueue()

    def test_pop_mutation(self):
        """Simulate mutation: Always return 'MUTATION' when popping."""
        original_pop = self.pq.pop
        self.pq.pop = lambda: "MUTATION"

        self.pq.push("item1", 1)
        self.assertEqual(self.pq.pop(), "MUTATION")

        # Restore the original method
        self.pq.pop = original_pop

    def test_peek_mutation(self):
        """Simulate mutation: Always return 'MUTATION' for peek."""
        original_peek = self.pq.peek
        self.pq.peek = lambda: "MUTATION"

        self.pq.push("item1", 1)
        self.assertEqual(self.pq.peek(), "MUTATION")

        # Restore the original method
        self.pq.peek = original_peek

if __name__ == "__main__":
    unittest.main()
