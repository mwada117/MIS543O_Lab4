import random, time

from BasicTest import *

"""
This tests random packet delay. We randomly decide to delay about half of the
packets that go through the forwarder in either direction by 1.5 seconds.
"""
class RandomDelayTest(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.choice([True, False]):
                time.sleep(1)
                self.forwarder.out_queue.append(p)
            else:
                self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []