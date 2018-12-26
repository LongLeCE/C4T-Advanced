import numpy as np
from queue import Queue


class QueueSimulation:
    def __init__(self, process_rate, min_req_rate, max_req_rate, queue_capacity):
        self.process_rate = process_rate
        self.min_req_rate = min_req_rate
        self.max_req_rate = max_req_rate
        self.queue = Queue(queue_capacity)

    def step(self, reqs):
        results = []
        loss_req = 0
        loss_1 = self.queue.size() - self.process_rate
        if loss_1 < 0:
            loss_2 = len(reqs) + loss_1
            if loss_2 > 0:
                for _ in range(self.queue.size()):
                    results += self.queue.remove()
                results += reqs[0: -loss_1]
                self.queue.clear()
                for j in range(loss_2):
                    self.queue.insert(reqs[j - loss_1])
                loss_req += loss_2 - self.queue.size()
            else:
                for _ in range(self.queue.size()):
                    results += self.queue.remove()
                results += reqs
        else:
            for _ in range(self.process_rate):
                results.append(self.queue.remove())
            temp_size = self.queue.size()
            for k in range(len(reqs)):
                self.queue.insert(reqs[k])
            loss_req += len(reqs) - self.queue.size() + temp_size
        return results, loss_req

    def run(self, iterations):
        self.queue.clear()
        loss_req = 0
        for _ in range(iterations):
            reqs = list(" " * np.random.randint(self.min_req_rate, self.max_req_rate + 1))
            loss_req += self.step(reqs)[1]
        return (loss_req + self.queue.size()) / iterations
    
