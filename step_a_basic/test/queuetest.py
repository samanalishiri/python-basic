from unittest import TestCase

from step_a_basic.datastructure.queue import PriorityQueue


class QueueTest(TestCase):

    def test_priority_queue(self):
        PriorityQueue() \
            .push('B', 2) \
            .push('D', 5) \
            .push('A', 1) \
            .push('E', 3) \
            .push('C', 4) \
            .print()
