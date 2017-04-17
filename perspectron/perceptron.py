if __name = '__main__' : 


#initializing a single neuron neural network

neural_network = NeuralNetwork()
 
print('random synaptic weights : ')
print (neural_network.synaptic_weights)


#the training set, we have three input values and one output value

training_set_inputs = array([[0,0,1],[1,0,1],[0,0,1],[1,1,1],[0,0,0]])
training_set_outputs = array([[0,1,0,1,0]]).T

#training the neural network using a dataset using back propogation for 10,000 times and make small adjustments in weights 
#each cycle

neural_network(training_set_inputs, training_set_outputs, 10000 )

print('new synaptic weights after training :')
print(neural_network.synaptic_weights)

#testing the neural network

print('predicting')
print(neural_network.predict(array[1,0,0]))



#https://www.youtube.com/watch?v=p69khggr1Jo


