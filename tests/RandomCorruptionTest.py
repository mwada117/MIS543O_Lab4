import random

from BasicTest import *

"""
This tests random packet corruption. We randomly decide to corrupt about half of the
packets that go through the forwarder in either direction.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""
class RandomCorruptionTest(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.choice([True, False]):
                p.msg_type = "foo"
            self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []