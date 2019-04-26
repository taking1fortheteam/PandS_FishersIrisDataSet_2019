''' Aidan Colon - Iris Data Set Project April 16 2019
This project is an analysis of the Fisher Iris Data Set that was published in 1916 by Dr. Fisher in his studies. This python code and accompanying documents / files is this students dissemination of that data and reresentation in a  format that ill hopefully be easy on the eye as well as intuitive.

Initially I would like to import the data set in order to work on it. '''

import numpy as np                      # Importing numpy for analyzing the data           
import matplotlib.pyplot as plt         # Importing pyplot from matplotlib for plotting the data
from sklearn.datasets import load_iris  #2 THis line of code retrieves the data set from scikit database hosting site
iris = load_iris()                      #2 Let iris equal to the load iris function
from PIL import Image                   # having to use the Python Imaging Library to import and display images in Python.          
import pylab 

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

# Same goes for Iris Versicolor

                                        # I am just filling up an array with the specific data for each parameter associated with each breed 
Sepal_Length = Iris_Versicolor[:, 0]        # In this case I am setting Sepal_Length equal to each value of the array (all rows (of the 0-50), column 0)
Sepal_Width = Iris_Versicolor[:, 1]         # Here I am setting Sepal Width equal to each value of the array (all rows (of the 0 to 50), column 1)  

                                        # As verification I wanto ensure I have extracted the data correctly so Iam printing it to sreen in these lines:
print('The following figures are the values of the Sepal Length of the Iris Versicolor flower:') # Print the text
print(Sepal_Length,'\n\n')              # Print the values in the Sepal_Length array (50 values in total)...followed by 2 carriage returns                                                    
print('The following figures are the values of the Sepal Width of the Iris Versicolor flower:')  # Print the text
print(Sepal_Width,'\n\n')               # Print the values in the Sepal_Width array (50 values in total)...followed by 2 carriage returns                                                    


# And again for Iris Virginica


                                        # I am just filling up an array with the specific data for each parameter associated with each breed 
Sepal_Length = Iris_Virginica[:, 0]        # In this case I am setting Sepal_Length equal to each value of the array (all rows (of the 0-50), column 0)
Sepal_Width = Iris_Virginica[:, 1]         # Here I am setting Sepal Width equal to each value of the array (all rows (of the 0 to 50), column 1)  

                                        # As verification I wanto ensure I have extracted the data correctly so Iam printing it to sreen in these lines:
print('The following figures are the values of the Sepal Length of the Iris Virginica flower:') # Print the text
print(Sepal_Length,'\n\n')              # Print the values in the Sepal_Length array (50 values in total)...followed by 2 carriage returns                                                    
print('The following figures are the values of the Sepal Width of the Iris Virginica flower:')  # Print the text
print(Sepal_Width,'\n\n')               # Print the values in the Sepal_Width array (50 values in total)...followed by 2 carriage returns                                                    


########Show image as a intro:

# Image saved from : https://i.ytimg.com/vi/ywIWUfjPCyY/maxresdefault.jpg

#####img = Image.open('SepalPetal.jpg') # Open thse image from local machinre
#####img.show()  # Show the image using default image viewer on local machine. 
#####input("Press Enter to continue...")


# Lets try and plot the data of Sepal Length against Width

fig, ax = plt.subplots(figsize=(20, 10))

plt.subplot(1, 3, 1)                                                                                        # plot subplot - 1 row, 3 elements, and we are woring on 1st on left subplot
plt.title('Sepal Length Versus Width of the Iris Setosa Flower', fontsize=10, fontweight='bold')            # Plot the title of the plot
plt.xlabel('Sepal Length')                                                                                  # plot the x axis label
plt.ylabel('Sepal Width')                                                                                   # plot the y axis label
plt.grid(True)                                                                                              # plot the grid


'''from matplot lib resource online:
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)[source]

'''

plt.axvline(np.mean(Iris_Setosa[:,0]), color='m', linestyle='dashdot', linewidth=1, label="mean")           # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Setosa[:,0]), color='r', linestyle='dashed', linewidth=1, label="max")                 # plot a vertical line of maximum length of Setosa flower - dashed colour red
plt.axvline(min(Iris_Setosa[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")               # plot a vertical line of minimum length of Setosa flower - dotted colour blue
plt.scatter(Iris_Setosa[:, 0], Iris_Setosa[:, 1], marker = "v", c="red", cmap=plt.cm.Set1, edgecolor='k')   # plot scatter - all array values in column 0, marker is a Square, Colour is red triangle 
plt.legend(loc = "upper left")                                                                                               # plot the legend in the graph

# plot the average value on the scatter chart@: 

plt.axhline(np.mean(Iris_Setosa[:,1]), color='m', linestyle='dashdot', linewidth=1)                         # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Setosa[:,1]), color='r', linestyle='dashed', linewidth=1)                              # plot a horizontal line of maximum length of Setosa flower - dashed colour red
plt.axhline(min(Iris_Setosa[:,1]), color='b', linestyle='dotted', linewidth=1)                              # plot a horizontal line of minimum length of Setosa flower - dotted colour blue

# Lets try and plot the data of Sepal Length against Width os Iris Versicolor FLower

plt.subplot(1, 3, 2)                                                                                        # plot a subplot with 1 row 3 columns and we are working on 2nd element (middle)
plt.title('Sepal Length Versus Width of the Iris Versicolor Flower', fontsize=10, fontweight='bold')        # plot the title of the plot
plt.xlabel('Sepal Length')                                                                                  # plot x axis label
plt.ylabel('Sepal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

plt.axvline(np.mean(Iris_Versicolor[:,0]), color='m', linestyle='dashdot', linewidth=1, label = "mean")     # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Versicolor[:,0]), color='r', linestyle='dashed', linewidth=1, label = "max")           # plot a vertical line of maximum length of Versicolor flower - dashed colour red
plt.axvline(min(Iris_Versicolor[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")           # plot a vertical line of minimum length of Versicolor flower - dotted colour blue
plt.scatter(Iris_Versicolor[:, 0], Iris_Versicolor[:, 1], marker = "o", c="blue", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend(loc = "upper left")                                                                                               # plot the legend

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Versicolor[:,1]), color='m', linestyle='dashdot', linewidth=1)                     # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Versicolor[:,1]), color='r', linestyle='dashed', linewidth=1)                          # plot a horizontal line of maximum length of Versicolor flower - dashed colour red
plt.axhline(min(Iris_Versicolor[:,1]), color='b', linestyle='dotted', linewidth=1)                          # plot a horizontal line of minimum length of Versicolor flower - dotted colour blue

# Lets try and plot the data of Sepal Length against Width os Iris Virginica FLower

plt.subplot(1, 3, 3)                                                                                        # plot a subplot with 1 row 3 columns and we are working on 3rd element (right)
plt.title('Sepal Length versus Width of the Iris Virginica Flower', fontsize=10, fontweight='bold')         # plot the title of the plot
plt.xlabel('Sepal Length')                                                                                  # plot x axis label
plt.ylabel('Sepal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

plt.axvline(np.mean(Iris_Virginica[:,0]), color='m', linestyle='dashdot', linewidth=1, label = "mean")      # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Virginica[:,0]), color='r', linestyle='dashed', linewidth=1, label = "max")            # plot a vertical line of maximum length of Virginica flower - dashed colour red
plt.axvline(min(Iris_Virginica[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")            # plot a vertical line of minimum length of Virginica flower - dotted colour blue
plt.scatter(Iris_Virginica[:, 0], Iris_Virginica[:, 1], marker = "s", c="green", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend(loc = "upper left")

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Virginica[:,1]), color='m', linestyle='dashdot', linewidth=1)                      # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Virginica[:,1]), color='r', linestyle='dashed', linewidth=1)                           # plot a horizontal line of maximum length of Virginica flower - dashed colour red
plt.axhline(min(Iris_Virginica[:,1]), color='b', linestyle='dotted', linewidth=1)                           # plot a horizontal line of minimum length of Virginica flower - dotted colour blue

plt.show()                                                                                                  # show the plot

#input("Press Enter to continue...")                                                                         # wait for user to enter a character

''' 
So at this stage we have managed to plot some data, specifically the sepal width versus the sepal length of the 3 different species of the Iris flower. 
What I intend to do now is to try plot on the one graph the combined sepal width Vs length in order that we are able to see the data wth respect to all 
samples instead of as individual plots
'''

fig = plt.figure(2, figsize=(20, 10))                                                                       # plot figure 2 with the size of 20 inches by 10.
plt.title('Sepal Length Versus Width of all 3 species', fontsize=10, fontweight='bold')                     # plot the title 
plt.xlabel('Sepal Length')                                                                                  # plot x axes label
plt.ylabel('Sepal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

#plt.axvline(np.mean(Iris_Versicolor[:,0]), color='m', linestyle='dashdot', linewidth=1, label = "mean")
#plt.axvline(max(Iris_Versicolor[:,0]), color='r', linestyle='dashed', linewidth=1, label = "max")
#plt.axvline(min(Iris_Versicolor[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")
plt.scatter(Iris_Setosa[:, 0], Iris_Setosa[:, 1], marker = "v", c="red", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Setosa")                # plot scatter - all array values in column 0, marker is a Square, Colour is red
plt.scatter(Iris_Versicolor[:, 0], Iris_Versicolor[:, 1], marker = "o", c="blue", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Versicolor")   # plot scatter - all array values in column 0, marker is a Square, Colour is blue 
plt.scatter(Iris_Virginica[:, 0], Iris_Virginica[:, 1], marker = "s", c="green", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Virginica")     # plot scatter - all array values in column 0, marker is a Square, Colour is green 
plt.legend(loc = "upper left")                                                                                               # plot the legend

plt.show()                                                                                                  # show the plot
# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
#plt.axhline(np.mean(Iris_Versicolor[:,1]), color='m', linestyle='dashdot', linewidth=1)
#plt.axhline(max(Iris_Versicolor[:,1]), color='r', linestyle='dashed', linewidth=1)
#plt.axhline(min(Iris_Versicolor[:,1]), color='b', linestyle='dotted', linewidth=1)

'''
NExt up I would like to take a look at teh Petal Width versus Petal Length of the 3 varieties. Initially I will plot as individual plots on the same figure.
Then I will again plot them on one plot to see if any traits of any species show any individual traits. 
'''
#the following is just a check that I am checking the correct data in the data set.
Petal_Length = Iris_Setosa[:, 2]        # In this case I am setting Petal_Length equal to each value of the array (all rows (of the 0-50), column 2)
Petal_Width = Iris_Setosa[:, 3]         # Here I am setting Petal Width equal to each value of the array (all rows (of the 0 to 50), column 3)  

print('The following figures are the values of the Petal Length of the Iris Setosa flower:') # Print the text
print(Petal_Length,'\n\n')              # Print the values in the Petal_Length array (50 values in total)...followed by 2 carriage returns                                                    
print('The following figures are the values of the Petal Width of the Iris Setosa flower:')  # Print the text
print(Petal_Width,'\n\n')               # Print the values in the Petal_Width array (50 values in total)...followed by 2 carriage returns                                                    

Petal_Length = Iris_Versicolor[:, 2]        # In this case I am setting Petal_Length equal to each value of the array (all rows (of the 0-50), column 2)
Petal_Width = Iris_Versicolor[:, 3]         # Here I am setting Petal Width equal to each value of the array (all rows (of the 0 to 50), column 3)  


Petal_Length = Iris_Virginica[:, 2]        # In this case I am setting Petal_Length equal to each value of the array (all rows (of the 0-50), column 2)
Petal_Width = Iris_Virginica[:, 3]         # Here I am setting Petal Width equal to each value of the array (all rows (of the 0 to 50), column 3)  





# Lets try and plot the data of Petal Length against Width

fig = plt.figure(3, figsize=(20, 10)) 
#fig, ax = plt.subplots(figsize=(20, 10))

plt.subplot(1, 3, 1)                                                                                        # plot subplot - 1 row, 3 elements, and we are woring on 1st on left subplot
plt.title('Petal Length Versus Width of the Iris Setosa Flower', fontsize=10, fontweight='bold')            # Plot the title of the plot
plt.xlabel('Petal Length')                                                                                  # plot the x axis label
plt.ylabel('Petal Width')                                                                                   # plot the y axis label
plt.grid(True)                                                                                              # plot the grid

plt.axvline(np.mean(Iris_Setosa[:,2]), color='m', linestyle='dashdot', linewidth=1, label="mean")           # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Setosa[:,2]), color='r', linestyle='dashed', linewidth=1, label="max")                 # plot a vertical line of maximum length of Setosa flower - dashed colour red
plt.axvline(min(Iris_Setosa[:,2]), color='b', linestyle='dotted', linewidth=1, label = "min")               # plot a vertical line of minimum length of Setosa flower - dotted colour blue
plt.scatter(Iris_Setosa[:, 2], Iris_Setosa[:, 3], marker = "v", c="red", cmap=plt.cm.Set1, edgecolor='k')   # plot scatter - all array values in column 0, marker is a Square, Colour is red triangle 
plt.legend(loc = "upper left")                                                                                               # plot the legend in the graph

# plot the average value on the scatter chart@: 

plt.axhline(np.mean(Iris_Setosa[:,3]), color='m', linestyle='dashdot', linewidth=1)                         # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Setosa[:,3]), color='r', linestyle='dashed', linewidth=1)                              # plot a horizontal line of maximum length of Setosa flower - dashed colour red
plt.axhline(min(Iris_Setosa[:,3]), color='b', linestyle='dotted', linewidth=1)                              # plot a horizontal line of minimum length of Setosa flower - dotted colour blue

# Lets try and plot the data of Sepal Length against Width os Iris Versicolor FLower

plt.subplot(1, 3, 2)                                                                                        # plot a subplot with 1 row 3 columns and we are working on 2nd element (middle)
plt.title('Petal Length Versus Width of the Iris Versicolor Flower', fontsize=10, fontweight='bold')        # plot the title of the plot
plt.xlabel('Petal Length')                                                                                  # plot x axis label
plt.ylabel('Petal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

plt.axvline(np.mean(Iris_Versicolor[:,2]), color='m', linestyle='dashdot', linewidth=1, label = "mean")     # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Versicolor[:,2]), color='r', linestyle='dashed', linewidth=1, label = "max")           # plot a vertical line of maximum length of Versicolor flower - dashed colour red
plt.axvline(min(Iris_Versicolor[:,2]), color='b', linestyle='dotted', linewidth=1, label = "min")           # plot a vertical line of minimum length of Versicolor flower - dotted colour blue
plt.scatter(Iris_Versicolor[:, 2], Iris_Versicolor[:, 3], marker = "o", c="blue", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend(loc = "upper left")                                                                                              # plot the legend

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Versicolor[:,3]), color='m', linestyle='dashdot', linewidth=1)                     # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Versicolor[:,3]), color='r', linestyle='dashed', linewidth=1)                          # plot a horizontal line of maximum length of Versicolor flower - dashed colour red
plt.axhline(min(Iris_Versicolor[:,3]), color='b', linestyle='dotted', linewidth=1)                          # plot a horizontal line of minimum length of Versicolor flower - dotted colour blue

# Lets try and plot the data of Petal Length against Width of Iris Virginica FLower

plt.subplot(1, 3, 3)                                                                                        # plot a subplot with 1 row 3 columns and we are working on 3rd element (right)
plt.title('Petal Length versus Width of the Iris Virginica Flower', fontsize=10, fontweight='bold')         # plot the title of the plot
plt.xlabel('Petal Length')                                                                                  # plot x axis label
plt.ylabel('Petal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

plt.axvline(np.mean(Iris_Virginica[:,2]), color='m', linestyle='dashdot', linewidth=1, label = "mean")      # plot a vertical dash dot line of the mean with colour magenta
plt.axvline(max(Iris_Virginica[:,2]), color='r', linestyle='dashed', linewidth=1, label = "max")            # plot a vertical line of maximum length of Virginica flower - dashed colour red
plt.axvline(min(Iris_Virginica[:,2]), color='b', linestyle='dotted', linewidth=1, label = "min")            # plot a vertical line of minimum length of Virginica flower - dotted colour blue
plt.scatter(Iris_Virginica[:, 2], Iris_Virginica[:, 3], marker = "s", c="green", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend(loc = "upper left")

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Virginica[:,3]), color='m', linestyle='dashdot', linewidth=1)                      # plot a horizontal dash dot line of the mean with colour magenta
plt.axhline(max(Iris_Virginica[:,3]), color='r', linestyle='dashed', linewidth=1)                           # plot a horizontal line of maximum length of Virginica flower - dashed colour red
plt.axhline(min(Iris_Virginica[:,3]), color='b', linestyle='dotted', linewidth=1)                           # plot a horizontal line of minimum length of Virginica flower - dotted colour blue

plt.show()                                                                                                  # show the plot

#input("Press Enter to continue...")                                                                         # wait for user to enter a character

# And again because it is difficult to gather any insight from 3 X individual plots, it is better to plot all 3 together

fig = plt.figure(4, figsize=(20, 10))                                                                       # plot figure 2 with the size of 20 inches by 10.
plt.title('Petal Length Versus Width of all 3 species', fontsize=10, fontweight='bold')                     # plot the title 
plt.xlabel('Petal Length')                                                                                  # plot x axes label
plt.ylabel('Petal Width')                                                                                   # plot y axis label
plt.grid(True)                                                                                              # plot the grid

plt.scatter(Iris_Setosa[:, 2], Iris_Setosa[:, 3], marker = "v", c="red", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Setosa")                # plot scatter - all array values in column 0, marker is a Square, Colour is red
plt.scatter(Iris_Versicolor[:, 2], Iris_Versicolor[:, 3], marker = "o", c="blue", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Versicolor")   # plot scatter - all array values in column 0, marker is a Square, Colour is blue 
plt.scatter(Iris_Virginica[:, 2], Iris_Virginica[:, 3], marker = "s", c="green", cmap=plt.cm.Set1, edgecolor='k', label = "Iris Virginica")     # plot scatter - all array values in column 0, marker is a Square, Colour is green 
plt.legend(loc = "upper left")                                                                                               # plot the legend

plt.show()                                                                                                  # show the plot






















#plt.show(2)
#plt.subplot(1, 2, 2)
#fig.tight_layout()





# 1 https://apmonitor.com/che263/index.php/Main/PythonDataAnalysis




