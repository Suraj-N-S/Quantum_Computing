import stim
import sys

circuit = stim.Circuit()

circuit.append("H", [0])
circuit.append("CNOT", [0,1])


if (int(sys.argv[1]) == 1 and int(sys.argv[2]) == 1):
    circuit.append("Z", [0])
    circuit.append("X", [0])
elif (int(sys.argv[1]) == 1 and int(sys.argv[2]) == 0):
    circuit.append("Z", [0])
    circuit.append("I", [0])
elif (int(sys.argv[1]) == 0 and int(sys.argv[2]) == 1):
    circuit.append("I", [0])
    circuit.append("X", [0])

elif (int(sys.argv[2]) == 0 and int(sys.argv[1]) == 0):
    circuit.append("I", [0])
    circuit.append("I", [0])


circuit.append("CNOT", [0,1])
circuit.append("H", [0])
circuit.append("M", [0,1])

diagram = circuit.diagram('timeline-svg')

with open("my_circuit.svg", "w") as file:
    file.write(str(diagram))

sample = circuit.compile_sampler().sample(shots=1)

if (sample[0][0] == 1 and sample[0][1] == 1):
    print("Alice sent the bits 1 1")
elif (sample[0][0] == 1 and sample[0][1] == 0):
    print("Alice sent the bits 1 0")
elif (sample[0][0] == 0 and sample[0][1] == 1):
    print("Alice sent the bits 0 1")
elif (sample[0][0] == 0 and sample[0][1] == 0):
    print("Alice sent the bits 0 0")
