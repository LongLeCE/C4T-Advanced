from queue_simulation import QueueSimulation

sim = QueueSimulation(5, 4, 7, 2)
assert(hasattr(sim, "process_rate"))
assert(hasattr(sim, "min_req_rate"))
assert(hasattr(sim, "max_req_rate"))
assert(hasattr(sim, "step"))
assert(hasattr(sim, "run"))

results, lost_count = sim.step(["A", "B", "C", "D"])
assert(results == ["A", "B", "C", "D"])
assert(lost_count == 0)

results, lost_count = sim.step(["E", "F", "G", "H", "I", "K"])
assert(results == ["E", "F", "G", "H", "I"])
assert(lost_count == 0)

results, lost_count = sim.step(["L", "M", "N", "O", "P", "Q"])
assert(results == ["K", "L", "M", "N", "O"])
assert(lost_count == 0)

results, lost_count = sim.step(["R", "S"])
assert(results == ["P", "Q", "R", "S"])
assert(lost_count == 0)

results, lost_count = sim.step(["T", "U", "V", "W", "X", "Y"])
assert(results == ["T", "U", "V", "W", "X"])
assert(lost_count == 0)

results, lost_count = sim.step(["Z", "0", "1", "2", "3", "4", "5"])
assert(results == ["Y", "Z", "0", "1", "2"])
assert(lost_count == 1)

results, lost_count = sim.step(["6", "7", "8", "9", "10", "11", "12", "13"])
assert(results == ["3", "4", "6", "7", "8"])
assert(lost_count == 3)

lost_requests_rate = sim.run(100000)
print(lost_requests_rate)
assert(lost_requests_rate < 0.6)
