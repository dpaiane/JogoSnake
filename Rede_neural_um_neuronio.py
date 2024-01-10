import math
input = 1 
output_desire = 0 # saida desejada
input_weight = 0.5 # peso
learning_rate = 0.1 # taxa de aprendizagem

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0
    
error = math.inf

print("Entrada ", input, "Desejado ", output_desire)
interation = 0

bias = 1
bias_weight = 0.5
while not error == 0:
    interation += 1
    print("--- Interações ", interation)
    print("Peso ", input_weight)
    sum =  (input * input_weight) + (bias * bias_weight)
    output = activation(sum)

    print ("Saida ",output)
    error = output_desire - output
    print("Erro", error)

    if not error == 0:
        input_weight = input_weight + (learning_rate * input * error)
        bias_weight = bias_weight + (learning_rate * bias * error)
print("### A rede aprendeu")