# Facial Keypoint Detection

Used the [Facial Keypoint](https://www.kaggle.com/c/facial-keypoints-detection/notebooks) dataset from Kaggle which is data on several images and corresponding data points on those images. 

The variables in the dataset are the locations of each keypoint

I have performed the following tasks on this dataset: 

Task 1:
- Data Analysis and Visualisation on the dataset
- Converting the images into dimensions readable by the model and showing the images

Task 2:
- Building a CNN using Keras 
- This model takes the image in the test data as an input and predicts keypoints
- Task 2a
  - Used transfer learning to replace the custom CNN with ResNet architecture.

Task 3:
- Deployed this model using Flask and built an interface that takes an image and outputs the predicted values overlayed on the same image
- Deployed the model on Heroku

# Future Work
Task 4:
- Using the model (with a new dataset) to predict facial expressions
