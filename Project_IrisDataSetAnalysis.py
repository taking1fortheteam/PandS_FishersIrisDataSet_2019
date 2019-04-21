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
fig = plt.figure(1, figsize=(5, 5))
plt.title('Sepal Length Versus Width of the Iris Setosa Flower', fontsize=10, fontweight='bold')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)


'''from matplot lib resource online:

matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)[source]

'''
plt.axvline(np.mean(Iris_Setosa[:,0]), color='m', linestyle='dashdot', linewidth=1, label="mean")
plt.axvline(max(Iris_Setosa[:,0]), color='r', linestyle='dashed', linewidth=1, label="max")
plt.axvline(min(Iris_Setosa[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")
plt.scatter(Iris_Setosa[:, 0], Iris_Setosa[:, 1], marker = "v", c="red", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend()

# plot the average value on the scatter chart@: 

plt.axhline(np.mean(Iris_Setosa[:,1]), color='m', linestyle='dashdot', linewidth=1)
plt.axhline(max(Iris_Setosa[:,1]), color='r', linestyle='dashed', linewidth=1)
plt.axhline(min(Iris_Setosa[:,1]), color='b', linestyle='dotted', linewidth=1)

#plt.show()
fig.tight_layout()

# Lets try and plot the data of Sepal Length against Width os Iris Versicolor FLower

fig = plt.figure(2, figsize=(5, 5))
plt.title('Sepal Length Versus Width of the Iris Versicolor Flower', fontsize=10, fontweight='bold')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)

plt.axvline(np.mean(Iris_Versicolor[:,0]), color='m', linestyle='dashdot', linewidth=1, label = "mean")
plt.axvline(max(Iris_Versicolor[:,0]), color='r', linestyle='dashed', linewidth=1, label = "max")
plt.axvline(min(Iris_Versicolor[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")
plt.scatter(Iris_Versicolor[:, 0], Iris_Versicolor[:, 1], marker = "o", c="blue", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend()

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Versicolor[:,1]), color='m', linestyle='dashdot', linewidth=1)
plt.axhline(max(Iris_Versicolor[:,1]), color='r', linestyle='dashed', linewidth=1)
plt.axhline(min(Iris_Versicolor[:,1]), color='b', linestyle='dotted', linewidth=1)


#plt.show(2)
#plt.subplot(1, 2, 2)
fig.tight_layout()



# Lets try and plot the data of Sepal Length against Width os Iris Virginica FLower

fig = plt.figure(3, figsize=(5, 5))
plt.title('Sepal Length versus Width of the Iris Virginica Flower', fontsize=10, fontweight='bold')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.grid(True)

plt.axvline(np.mean(Iris_Virginica[:,0]), color='m', linestyle='dashdot', linewidth=1, label = "mean")
plt.axvline(max(Iris_Virginica[:,0]), color='r', linestyle='dashed', linewidth=1, label = "max")
plt.axvline(min(Iris_Virginica[:,0]), color='b', linestyle='dotted', linewidth=1, label = "min")
plt.scatter(Iris_Virginica[:, 0], Iris_Virginica[:, 1], marker = "s", c="green", cmap=plt.cm.Set1, edgecolor='k') # plot scatter - all array values in column 0, marker is a Square, CColour is blue, 
plt.legend()

# I would like now to have on the one graph the max min values on both axes so that it is easily spoken about.
plt.axhline(np.mean(Iris_Virginica[:,1]), color='m', linestyle='dashdot', linewidth=1)
plt.axhline(max(Iris_Virginica[:,1]), color='r', linestyle='dashed', linewidth=1)
plt.axhline(min(Iris_Virginica[:,1]), color='b', linestyle='dotted', linewidth=1)

#plt.show(3)
fig.tight_layout()

#fig, ax = plt.subplots()
#mngr = plt.get_current_fig_manager()
# to put it into the upper left corner for example:
#mngr.window.setGeometry(50,100,640, 545)


#geom = mngr.window.geometry()
#x,y,dx,dy = geom.getRect()

#mngr.window.setGeometry(newX, newY, dx, dy)

#plt.grid(True)
#plt.show()
#plt.grid(True)
#plt.show(2)
#plt.grid(True)
#plt.show(3)
plt.show()
#plt.show()

# 1 https://apmonitor.com/che263/index.php/Main/PythonDataAnalysis




