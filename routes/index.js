/* ----------------------------------------------------------------------------+
|                                                                              |
|                     Neuralcomputing - Gabriel Sansigolo                      |
|                                                                              |
+-----------------------------------------------------------------------------*/

/*--------------------------------------------------+
| Var                                               |
+--------------------------------------------------*/
var express = require('express');
var brain = require('brain.js')
var fs = require('fs')
var router = express.Router();

/*--------------------------------------------------+
| Iris                                           |
+--------------------------------------------------*/
router.get('/iris', function(req, res) {

  // configuration to be used in the brain
  const config = {
    iterations: 1000,
    momentum: 0.01,
    learningRate: 0.1,
    binaryThresh: 0.5, // arbitary value
    hiddenLayers: [3], // the size of the hidden layers in the network
    activation: 'sigmoid' // activation function
  }

  // array to hold the training data after formatting
  var trainingData = []

  // initialise a new backpropogating neural network
  const net = new brain.NeuralNetwork(config)

  // load each line of the training data into a new index of an array
  var trainingFile = fs.readFileSync("data.csv").toString().split("\n")

  // iterate over each line of the training data, adding it to a new array for training later
  for (var i = 0; i < trainingFile.length; i++) {
    var entry = trainingFile[i]

    var values = entry.split(",")
    var points = [parseInt(values[0]), parseInt(values[1]), parseInt(values[2]), parseInt(values[3])]
  
    if (i <= 49) {
        trainingData.push({input: points, output: {setosa: 1}})
    }
    else if (i > 49 && i <= 99) {
        trainingData.push({input: points, output: {versicolor: 1}})
    }
    else if (i > 99 && i <= 149) {
        trainingData.push({input: points, output: {virginica: 1}})
    }
  }

  // console log the output of each iteration
  net.train(trainingData, {
    log: true
  })

  // test data - actually virginica
  var output = net.run([6,3,5,2])

  return res.json(output);
});

/*--------------------------------------------------+
| Poker Hand                                          |
+--------------------------------------------------*/
router.get('/poker', function(req, res) {
  
    // configuration to be used in the brain
    const config = {
      iterations: 1000,
      momentum: 0.1,
      learningRate: 0.3,
      binaryThresh: 0.5, // arbitary value
      hiddenLayers: [10], // the size of the hidden layers in the network
      activation: 'sigmoid' // activation function
    }
  
    // array to hold the training data after formatting
    var trainingData = []
  
    // initialise a new backpropogating neural network
    const net = new brain.NeuralNetwork(config)
  
    // load each line of the training data into a new index of an array
    var trainingFile = fs.readFileSync("poker-hand.csv").toString().split("\n")
  
    // iterate over each line of the training data, adding it to a new array for training later
    for (var i = 0; i < trainingFile.length; i++) {
      var entry = trainingFile[i]
  
      var values = entry.split(",")
      var points = [ parseInt(values[0]), parseInt(values[1]), parseInt(values[2]), parseInt(values[3]), parseInt(values[4]), parseInt(values[5]), parseInt(values[6]), parseInt(values[7]), parseInt(values[8]), parseInt(values[9])  ]
     
      if(parseInt(values[10]) == 9) {
        trainingData.push({input: points, output: {Royal_flush: 1}})
      }
      else if (parseInt(values[10]) == 8) {
        trainingData.push({input: points, output: {Straight_flush: 1}})
      }
      else if (parseInt(values[10]) == 7) {
        trainingData.push({input: points, output: {Four_of_a_kind: 1}})
      }
      else if (parseInt(values[10]) == 6) {
        trainingData.push({input: points, output: {Full_house: 1}})
      }
      else if (parseInt(values[10]) == 5) {
        trainingData.push({input: points, output: {Flush: 1}})
      }
      else if (parseInt(values[10]) == 4) {
        trainingData.push({input: points, output: {Straight: 1}})
      }
      else if (parseInt(values[10]) == 3) {
        trainingData.push({input: points, output: {Three_of_a_kind: 1}})
      }
      else if (parseInt(values[10]) == 2) {
        trainingData.push({input: points, output: {Two_pairs: 1}})
      }
      else if (parseInt(values[10]) == 1) {
        trainingData.push({input: points, output: {One_pair: 1}})
      }
      else if (parseInt(values[10]) == 0) {
        trainingData.push({input: points, output: {Nothing: 1}})
      }
 
    }
  
    // console log the output of each iteration
    net.train(trainingData, {
      log: true
    })
  
    // test data - actually virginica
    const lista_teste = []

    lista_teste[0] = [2,8,2,5,1,11,4,1,1,12,0]
    lista_teste[1] = [1,7,3,11,3,3,4,8,3,7,1]
    lista_teste[2] = [2,10,4,4,3,6,1,6,1,10,2]
    lista_teste[3] = [1,10,1,3,3,10,3,1,2,10,3]
    lista_teste[4] = [3,13,3,10,1,1,1,11,3,12,4]
    lista_teste[5] = [4,10,4,12,4,9,4,1,4,13,5]

    const result_teste = ['One_pair', 'Nothing', 'Two_pairs', 'Three_of_a_kind', 'Straight', 'Flush']
    const results = []

    for (var i = 0; i < lista_teste.length; i++) {
      results[i] = net.run(lista_teste[i])
    }
  
    return res.json(results);
  });
  


module.exports = router;
