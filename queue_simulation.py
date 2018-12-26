import numpy as np
from queue import Queue


class QueueSimulation:
    def __init__(self, process_rate, min_req_rate, max_req_rate, queue_capacity=-1):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
        self.queue = Queue(queue_capacity)

    def step(self, reqs):
        results = []
        loss_req = 0
        loss_1 = self.queue.size() - self.process_rate
        try:
            results += self.queue.remove(self.process_rate)
        except TypeError:
            pass
        if loss_1 < 0:
            loss_2 = len(reqs) + loss_1
            results += reqs[: -loss_1] if loss_2 > 0 else reqs
            self.queue.insert(reqs[-loss_1:], is_list=True)
            if loss_2 > 0:
                loss_req += loss_2 - self.queue.size()
        else:
            temp_size = self.queue.size()
            self.queue.insert(reqs, is_list=True)
            loss_req += len(reqs) - self.queue.size() + temp_size
        return results, loss_req

    def run(self, iterations):
        self.queue.clear()
        loss_req = 0
        for _ in range(iterations):
            loss_req += self.step(list(" " * np.random.randint(self.min_req_rate, self.max_req_rate + 1)))[1]
        return (loss_req + self.queue.size()) / iterations
    
