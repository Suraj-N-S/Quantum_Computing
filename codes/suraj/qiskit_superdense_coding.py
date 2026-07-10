from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector 

a = int(input("Enter bit(LSB) for a : ")) # lsb
b = int(input("Enter bit(MSB) for b : ")) # msb 

qc = QuantumCircuit(2,2)  # qubit_1 is for Alice,qubit_0 is for Bob 

# Creating Bell stae betwen Alice and Bob 

qc.h(1) # hadamard gate to Alice qubit
qc.cx(1,0) # cnot ,control bit : Alice , target bit : Bob 

# sending classical bits "ba" (super-dense coding)

if a : 
    qc.x(1) 

if b : 
    qc.z(1)  

qc.barrier() 


print("\nStatevector in Bell Basis :\n")
print(Statevector.from_instruction(qc))


# inverting the bell basis to get computational basis 

qc.cx(1,0) 
qc.h(1) 

print("Statevector in Computational Basis :\n")
print(Statevector.from_instruction(qc))

qc.measure([0,1],[0,1]) 

print(qc.draw()) 

sim = AerSimulator() 

result = sim.run(qc,shots=10).result() 

print(result.get_counts())





