''' Aidan Colon - Iris Data Set Project April 16 2019
This project is an analysis of the Fisher Iris Data Set that was published in 1916 by Dr. Fisher in his studies. This python code and accompanying documents / files is this students dissemination of that data and reresentation in a  format that ill hopefully be easy on the eye as well as intuitive.

Initially I would like to import the data set in order to work on it. '''

import numpy as np       # Importing and anslyzing the data           
import matplotlib.pyplot as plt # matplotlib for plotting the data
import matplotlib.image as mpimg
#from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import load_iris          #2 THis line of code retrieves the data set from scikit database hosting site
iris = load_iris()                                #2 LEt iris equal to the load iris function
#from sklearn.decomposition import PCA




from PIL import Image   # having to use the Python Imaging Library to import and display images in Python.                                                                             
from statistics import mean # import mean function from statistics





#print(iris)                                     # Print Iris as a trstto ensure we are reading correctly.

Iris_Setosa = (iris.data[0:50]) # By using iris.data -> this only looks at the data arrays within the iris file taken from source.
Iris_Versicolor = (iris.data[51:100])
Iris_Virginica = (iris.data[101:150])

Sepal_Length = Iris_Setosa[:, 0]
Sepal_Width = Iris_Setosa[:, 1]

print(Sepal_Length)
#print(Sepal_Width)


########Show image as a intro:
'''
# Image saved from : https://i.ytimg.com/vi/ywIWUfjPCyY/maxresdefault.jpg
img = Image.open('SepalPetal.jpg') # Open thse image from local machinre
img.show()  # Show the image using default image viewer on local machine. 
'''


input("Press Enter to continue...")


#pause()
#imshow("SepalPetal.jpg")

# Lets try and plot the data of Sepal Length against Width

plt.title('This is a plot of the Sepal Length Versus Width')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
fig = plt.figure(1, figsize=(12, 12))


plt.scatter(Iris_Setosa[:, 0], Iris_Setosa[:, 1], c="red", cmap=plt.cm.Set1, edgecolor='k')
#plt.scatter(Iris_Versicolor[:, 0], Iris_Versicolor[:, 1], c="blue", cmap=plt.cm.Set1, edgecolor='k')
#plt.scatter(Iris_Virginica[:, 0], Iris_Virginica[:, 1], c="green", cmap=plt.cm.Set1, edgecolor='k')

# Need to determine the max value of each of the elements in the array


print('Max ELement of Sepal Length is:', max(Iris_Setosa[:,0]))
print('Min ELement of Sepal Length is:', min(Iris_Setosa[:,0]))

def Average():
    return mean() #sum(array) / len(array)



# Function that return average of an array to 2 decimal points. 
def average(a, n): 
    # Find sum of array element 
    sum = 0
    for i in range(n): 
        sum += a[i] 
    return round(sum/n, 2); 

# Driver code 
arr = (Iris_Setosa[:,0])
n = len(arr) 
print('The average of the Sepal Width is:', average(arr, n))








#print('Average of the list is :', Average)
#print('Sum of the array is', sum)
#print('Len of thr array is', len)
#print('Average of the length is:', round(mean(Iris_Setosa[:,0])))


print('Max ELement of Sepal Width is:', max(Iris_Setosa[:,1]))
print('Min ELement of Sepal Width is:', min(Iris_Setosa[:,1]))

#plt.clf()

'''
x = Iris_Setosa[:, :2]
#X = Iris_Setosa[:, 0].min() -.5, X[:, 0].max() + 0.5
y = iris.target


plt.title('Some Sort of Graph for Display', fontsize=32)
# Plot the training points
#plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length', fontsize=18)
plt.ylabel('Sepal width', fontsize=18)

'''



#plt.clf()

'''
print(Iris_Setosa)  # test just to ensure I have extracted correct data points
print(Iris_Versicolor) # test just to ensure I have extracted correct data points
print(Iris_Versicolor) # test just to ensure I have extracted correct data points
#
'''
# Iris_Setosa = 

#data_file = np.loadtxt('data_file.txt', delimiter=',')       #1   

#sample_number = data_file[:,0]                              #1


'''
#iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(1, figsize=(12, 12)) # FIgsize is the size of the plot in inches
plt.clf()

plt.title('Some Sort of Graph for Display', fontsize=32)
# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1, edgecolor='k')
plt.xlabel('Sepal length', fontsize=18)
plt.ylabel('Sepal width', fontsize=18)

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.grid(True)
#plt.grid(color='r', linestyle='-', linewidth=2)

'''
'''
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])
'''
plt.show()

# 1 https://apmonitor.com/che263/index.php/Main/PythonDataAnalysis




'''

THis all works to show the plot in a  3 dmentional plot. 


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :2]  # we only take the first two features.
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])

plt.show()
'''