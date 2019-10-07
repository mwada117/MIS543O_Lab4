import random

from BasicTest import *

"""
This tests random packet duplication. We randomly decide to corrupt about half of the
packets that go through the forwarder in either direction.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""
class RandomDuplicationTest(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            if random.choice([True, False]):
                print "seqno = %s" % p.seqno
                self.forwarder.out_queue.append(p)
                print "seqno = %s" % p.seqno
                self.forwarder.out_queue.append(p)
            else:
                self.forwarder.out_queue.append(p)

        # empty out the in_queue
        self.forwarder.in_queue = []