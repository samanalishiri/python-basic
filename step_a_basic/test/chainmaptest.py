from unittest import TestCase

from step_a_basic.datastructure.chainmap import Chain


class ChainMapTest(TestCase):
    def test_chain_map(self):
        chain = Chain() \
            .forward(1) \
            .forward(2) \
            .forward(3)

        self.assertListEqual([{'node': 3}, {'node': 2}, {'node': 1}],
                             chain.collect(),
                             'ChainMapTest.test_chain_map is failed')
