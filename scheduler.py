#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import uuid
import math
from net_queue import NetQueue
from operator import attrgetter


class Scheduler():

    def __init__(self, capacity=1):
        self.queues = {}
        self.capacity = capacity

    def register(self, q, rate, name=""):
        if name in self.queues:
            raise Exception('Queue is already registered: {0}'.format(name))
        if name == "":
            name = uuid.uuid4()[:6] 
        self.queues[name] = GPSQueue(queue=q, rate=rate)

    def send_packets(self):
        queues = list(self.queues.values())
        queues.sort(key=attrgetter('deadline'))
        queues_selected = queues[:self.capacity]
        for q in queues_selected:
            q.deadline += math.ceil(1.0/q.rate)
            if q.queue.empty():
                logging.info('The queue is empty: {0}'.format(q.queue.ID))
                continue

            print('output:', q.queue.get())


class GPSQueue():

    def __init__(self, queue, rate=0.0, deadline=0):
        self.queue = queue
        self.rate = rate
        self.deadline = deadline

    def __unicode__(self):
        return '[GPS Queue: Rate: {0}, Deadline: {1}, Queue: {2}]'\
                .format(self.rate, self.deadline, self.queue)

    def __str__(self):
        return self.__unicode__()


def get_queue_names(capacity, param):
    """
    It returns the names of the queues to dequeue.
    """
    return []


if __name__ == '__main__':
    s = Scheduler(capacity=1)
    q_1 = NetQueue(rate=0.7)
    q_2 = NetQueue(rate=0.3)
    try:
        s.register(q_1, 0.7, q_1.ID)
        s.register(q_2, 0.3, q_2.ID)
        for i in range(0, 5):
            print('------[t = {0}]-------'.format(i))
            s.send_packets()
            for name in s.queues:
                print(s.queues[name])

    except Exception as err:
        raise Exception('Fail to register some queue: {0}'.format(err))
