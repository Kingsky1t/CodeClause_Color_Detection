# CodeClause_Color_Detection

  This is my first task for the CodeClause Data Science Internship programme.
  In this project, 
  The KNN algorithm works by measuring the Euclidean distance between the input color and each color in the dataset. It then selects the color with the minimum distance as the closest color. By setting k=1, we consider only the nearest neighbor, which is the color with the smallest distance.

  To perform color detection, we start by preprocessing the dataset, ensuring that the colors are represented in a suitable format for comparison, such as RGB or HSL. The input color is also converted to the same format.
  The image is read with the help of OpenCV and then was written on it using the same tool.

  Next, we iterate through the dataset and compute the Euclidean distance between the input color and each color in the dataset. The distance calculation considers the differences between the color components, such as red, green, and blue values.
  
  Once we have computed the distances, we select the color with the minimum distance as the closest color. This color is then associated with a corresponding label, representing the detected color.

  By using KNN with k=1, we effectively determine the closest color from the dataset based on the input color. This approach can be used in various applications, such as image processing, computer vision, or color recognition systems.

  It's important to note that the effectiveness of color detection using KNN with k=1 heavily relies on the quality and representativeness of the dataset. A diverse dataset with a wide range of colors will enhance the accuracy of the color detection process, ensuring reliable results for different input colors.
  
  PS:-
  The dataset and the main file is provided in the repo above just download it and run the main file. 
  You can change the image keeping in mind the name of the file is "colorpic.jpg".
