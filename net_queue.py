#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue
import uuid


class NetQueue(queue.Queue):

    def __init__(self, id="", rate=0.0):
        self.rate = rate
        if id == "":
            self.id = uuid.uuid4()
        super(NetQueue, self).__init__()

    def __unicode__(self):
        max_size = q.maxsize if q.maxsize > 0 else 'Infinity'
        return '[ID: {id}, Rate: {rate}, Size: {size}, Max: {max_size}]' \
            .format(id=self.id, rate=self.rate,
                size=self.qsize(), max_size=max_size)

    def __str__(self):
        return self.__unicode__()

if __name__ == '__main__':
    q = NetQueue(rate=0.5)
    q.put('test')
    q.put([1, 2, 3])
    print(q.get())
    print('Queue:', q)
