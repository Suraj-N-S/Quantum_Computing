import stim 

circuit = stim.Circuit() 

# initializing Alice qubit_0 to |+> 
circuit.append("H",[0]) 

# circuit.append("X",[0]) # to initialize qubit_0 to |1>

# creating bell state between Alice (qubit_1) and Bob (qubit_2) 
circuit.append("H",[1])
circuit.append("CX",[1,2]) 

# inverting bell state for qubit_0 and qubit_1 
circuit.append("CX",[0,1])
circuit.append("H",[0])

# measuring in computational basis
circuit.append("M",[0,1])

# Making changes to Bob's bit
circuit.append("CX",[stim.target_rec(-1),2]) # here rec is the array that contains the measured values 
# here 2(right most argument) is the qubit_no to which we apply the X operation if rec[-1] equals 1

# rec[-1] is the latest measurement and in this case corresponds to measurement of qubit_1
# rec[-2] is the measurement before rec[-1] corresponding to measurement of qubit_0 int his case


circuit.append("CZ",[stim.target_rec(-2),2]) 

circuit.append("M",[2]) # to measure Bob's bit

print(circuit) 

sampler = circuit.compile_sampler()
samples = sampler.sample(shots=100) 

samples = samples.astype(int) 

# for Bob's bit
count_0 = 0
count_1 = 0

for row in samples :
    if row[2]== 0:
        count_0+=1

    else:
        count_1+=1

# print(samples[:,2]) # column_2 (3rd column) that corresponds to qubit_2 (Bob's bit)
print(f"Count of 0 : {count_0} | Count of 1 : {count_1}") # print only the count of 0s and 1s occurred
# to know the distribution of 0s and 1s when measured

