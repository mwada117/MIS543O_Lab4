import random

from BasicTest import *

"""
This tests random packet duplication. We randomly decide to duplicate about half of the
packets that go through the forwarder in either direction.
"""
class RandomDuplicationTest(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.choice([True, False]):
                self.forwarder.out_queue.append(p)
                self.forwarder.out_queue.append(p)
            else:
                self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []