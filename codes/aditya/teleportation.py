import stim
import sys


circuit = stim.Circuit()

circuit.append("I", [0])

#Making the mixed state
circuit.append("H", [1])
circuit.append("CNOT", [1,2])


#Bell state measurement
circuit.append("CNOT", [0,1])
circuit.append("H", [0])

#Measuring Alice's Qubit
circuit.append("M", [0])
circuit.append("M", [1])

circuit.append("CX", [stim.target_rec(-1), 2])
circuit.append("CZ", [stim.target_rec(-2), 2])

circuit.append("M", [2])

sampler = circuit.compile_sampler()
sample = sampler.sample(shots=1)[0]

print(f"Bob's final state Q2={int(sample[2])}")




