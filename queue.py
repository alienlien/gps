#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import queue


class Queue(queue.Queue):

    def __init__(self, rate=0.0):
        self.rate = rate

    def get_rate(self):
        return self.rate

    def set_rate(self, rate):
        self.rate = rate
