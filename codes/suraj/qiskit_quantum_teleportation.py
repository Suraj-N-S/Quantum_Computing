import numpy as np
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector 
from qiskit.quantum_info import DensityMatrix, partial_trace

qc = QuantumCircuit(3,3) 

# q_2 and q_1 on Alice side , q_0 on Bob side 

print("Enter the amplitudes for Alice's qubit :")
alpha_0 = int(input("Enter the amplitude for |0> : "))
alpha_1 = int(input("Enter the amplitude for |1> : "))
print("\n")

qc.initialize([alpha_0,alpha_1],2) # initializing the state for Alice qubit_2 

# qc.initialize([1/np.sqrt(2),1/np.sqrt(2)],2)

# Creating Bell state between Alice and Bob using q_1 and q_0 

qc.h(1)
qc.cx(1,0) 

# Measuring q_2 and q_1 
# First inverting the bell basis to computational basis

qc.cx(2,1)
qc.h(2) 

qc.measure([1,2],[1,2]) 

with qc.if_test((1,1)): # checking if classical bit 1(left argument) is equal to 1(right argument)
    qc.x(0) 

with qc.if_test((2,1)):
    qc.z(0) 

print(qc.draw())

qc.save_density_matrix() # save the density matrix of the quantum state

sim = AerSimulator() 

result = sim.run(qc,shots=1).result() 

dm = result.data(0)["density_matrix"] # to get(retrieve) the density matrix that was saved in experiment 0(i.e qc)

dm = DensityMatrix(dm) # converted into qiskit density matrix

bob = partial_trace(dm,[1,2]) # discard qubit_1 and qubit_2 , retain qubit_0 (bob's qubit) 

print("\nThe Statevector for the Teleported state is :")
print(bob.to_statevector()) # print it as statevector






