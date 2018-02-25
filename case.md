![Image of Part1](https://github.com/JiminQ/Perovskite/blob/edit_usecases/Part1.png =100x)


![Image of Part2](https://github.com/JiminQ/Perovskite/blob/edit_usecases/Part2.png)



## Use cases:
### Use case 1 : find the features of Perovskites with water-split ability
Input: Perovskites(with or without water-split ability), and their properties include crystal structure parameters, atoms parameters, electrical field parameters.

Output: The features of input perovskites.

Components: 
  * read perovskites' parameters
  * screening perovskites with water-split ability
  * do clustering
  * output the features

![Image of workflow1](https://github.com/JiminQ/Perovskite/blob/edit_usecases/use%20case%20flow1.png)


### Use case 2: predict band gap and formation energy
Input: Perovskites(with or without water-split ability) properties include crystal structure parameters, atoms parameters, electrical field parameters, and their band gap and formation energy.

Output: Band gap and formation energy of input perovskites.

Components:
  * read perovskites' parameters and their band gap and formation energy
  * create training dataset and testing dataset
  * do kernel ridge regression on training dataset
  * predict the band gap and formation energy on testing dataset
  * analyze the accuracy of prediction
  
![Image of workflow2](https://github.com/JiminQ/Perovskite/blob/edit_usecases/use%20case%20flow2.png)


### Use case 3: predict water-split ability
Input: Perovskites(with or without water-split ability), and their properties include crystal structure parameters, atoms parameters, electrical field parameters.

Output: The estimated water-split ability of input perovskites.

Components:
  * read perovskites' parameters and their water-split ability.
  * create training dataset and testing dataset
  * do kernel ridge regression on training dataset
  * predict water-split ability on testing dataset
  * analyze the accuracy of prediction
  
  ![Image of workflow3](https://github.com/JiminQ/Perovskite/blob/edit_usecases/use%20case%20flow3.png)

