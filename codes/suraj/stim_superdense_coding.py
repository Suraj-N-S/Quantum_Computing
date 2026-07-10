import stim 

circuit = stim.Circuit() 

# qubit_1 for Alice and qubit_0 for Bob 

a = int(input("Enter bit(LSB) for a : "))
b = int(input("Enter bit(MSB) for b : "))

# creating the bell state
circuit.append("H",[0])
circuit.append("CX",[0,1])

if a:
    circuit.append("X",[0])

if b:
    circuit.append("Z",[0]) 

# inverting the bell basis 
circuit.append("CX",[0,1])
circuit.append("H",[0])

circuit.append("M",[0,1])

print(circuit) 

sampler = circuit.compile_sampler()

samples = sampler.sample(shots=5) 

samples = samples.astype(int) 

print(samples)


