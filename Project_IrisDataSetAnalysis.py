''' Aidan Colon - Iris Data Set Project April 16 2019
This project is an analysis of the Fisher Iris Data Set that was published in 1916 by Dr. Fisher in his studies. This python code and accompanying documents / files is this students dissemination of that data and reresentation in a  format that ill hopefully be easy on the eye as well as intuitive.

Initially I would like to import the data set in order to work on it. '''

import numpy as np                      # Importing numpy for analyzing the data           
import matplotlib.pyplot as plt         # Importing pyplot from matplotlib for plotting the data
from sklearn.datasets import load_iris  #2 THis line of code retrieves the data set from scikit database hosting site
iris = load_iris()                      #2 Let iris equal to the load iris function
from PIL import Image                   # having to use the Python Imaging Library to import and display images in Python.                                                                             
from statistics import mean             # import mean function from statistics


def average(a, n):                       # Function that return average of an array to 2 decimal places 
    sum = 0                                 # sum is 0 to begin with
    for i in range(n):                      # for i is in the range of the elements (n) of the array
        sum += a[i]                             # add each of the elements together as it progresses through the array
    return round(sum/n, 2);                 # return a value (sum divided by the number of elements in the array) that is rounded to 2 decimal places, 





                                        # By using iris.data -> this only looks at the data arrays within the iris file taken from source.
Iris_Setosa = (iris.data[0:50])         # Iris Setosa data is contained in the first 50 elements of the array 
Iris_Versicolor = (iris.data[51:100])   # Iris Versicolor data is contained in the elements 50 - 100 of the array 
Iris_Virginica = (iris.data[101:150])   # Iris Virginica data is contained in elements 100 - 150 of the array 

                                        # I am just filling up an array with the specific data for each parameter associated with each breed 
Sepal_Length = Iris_Setosa[:, 0]        # In this case I am setting Sepal_Length equal to each value of the array (all rows (of the 0-50), column 0)
Sepal_Width = Iris_Setosa[:, 1]         # Here I am setting Sepal Width equal to each value of the array (all rows (of the 0 to 50), column 1)  

                                        # As verification I wanto ensure I have extracted the data correctly so Iam printing it to sreen in these lines:
print('The following figures are the values of the Sepal Length of the Iris Setosa flower:') # Print the text
print(Sepal_Length,'\n\n')              # Print the values in the Sepal_Length array (50 values in total)...followed by 2 carriage returns                                                    
print('The following figures are the values of the Sepal Width of the Iris Setosa flower:')  # Print the text
print(Sepal_Width,'\n\n')               # Print the values in the Sepal_Width array (50 values in total)...followed by 2 carriage returns                                                    


########Show image as a intro:

# Image saved from : https://i.ytimg.com/vi/ywIWUfjPCyY/maxresdefault.jpg
img = Image.open('SepalPetal.jpg') # Open thse image from local machinre
img.show()  # Show the image using default image viewer on local machine. 



input("Press Enter to continue...")


# Lets try and plot the data of Sepal Length against Width

plt.title('This is a plot of the Sepal Length Versus Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
fig = plt.figure(1, figsize=(12, 12))


plt.scatter(Iris_Setosa[:, 0], Iris_Setosa[:, 1], c="red", cmap=plt.cm.Set1, edgecolor='k')
#plt.scatter(Iris_Versicolor[:, 0], Iris_Versicolor[:, 1], c="blue", cmap=plt.cm.Set1, edgecolor='k')
#plt.scatter(Iris_Virginica[:, 0], Iris_Virginica[:, 1], c="green", cmap=plt.cm.Set1, edgecolor='k')


# Need to determine the max value of each of the elements in the array

print('\n')
print('Max ELement of Sepal Length of Iris Setosa is:', max(Iris_Setosa[:,0])) # Print Max Value of Sepal Length of Iris Setosa 
print('Min ELement of Sepal Length of Iris Setosa is:', min(Iris_Setosa[:,0])) # Print Min Value of Sepal Length of Iris Setosa 


arr = (Iris_Setosa[:,0])
n = len(arr) 
print('The average of the Sepal Length of Iris Setosa is:', average(arr, n))

# plot the average value on the scatter chart@: 
plt.axvline(average(arr, n), color='m', linestyle='dashdot', linewidth=1)
plt.axvline(max(Iris_Setosa[:,0]), color='r', linestyle='dashed', linewidth=1)
plt.axvline(min(Iris_Setosa[:,0]), color='b', linestyle='dashed', linewidth=1)





#print('Average of the list is :', Average)
#print('Sum of the array is', sum)
#print('Len of thr array is', len)
#print('Average of the length is:', round(mean(Iris_Setosa[:,0])))


print('Max ELement of Sepal Width of Iris Setosa is:', max(Iris_Setosa[:,1])) # Print Max value of Sepal Width of Iris Setosa
print('Min ELement of Sepal Width of Iris Setosa is:', min(Iris_Setosa[:,1])) # Print Min value of Sepal Width of Iris Setosa
arr = (Iris_Setosa[:,1])
n = len(arr) 
print('The average of the Sepal Width is:', average(arr, n))                  # Print the average value of Sepal Width for Iris Setosa 
#Print the average or mean of the Y axis:
plt.axhline(average(arr, n), color='m', linestyle='dashdot', linewidth=1)      # Plot the average value for the Sepal Width as a horizontal line, colour - m for magenta, dashed linestyle 

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(max(Iris_Setosa[:,1]), color='r', linestyle='dashed', linewidth=1)
plt.axhline(min(Iris_Setosa[:,1]), color='b', linestyle='dashed', linewidth=1)


plt.show()

# 1 https://apmonitor.com/che263/index.php/Main/PythonDataAnalysis




