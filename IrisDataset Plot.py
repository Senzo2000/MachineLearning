from sklearn import datasets




iris = datasets.load_iris()
print(type(iris))
print(iris['target_names'])#This prints out the type of irirs plant it is 
print(iris['data'])
print(iris['target'])
print(iris['DESCR'])#This is a whole description of the iris plant
print(iris['feature_names'])# the features of the sepal (sepal length and width, and petal length and width)
print(iris) #iris is the dataset object

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

fig = plt.figure()
#The first number represents the number of rows(Horizontal ----)
#The second number represents the number of columns(Vertical |)
#The third number represents the position of the graph itself

#There are 4 rows, 3 columns and 12 graphs.

ax1 = plt.subplot(4,3,1)
ax2 = plt.subplot(4,3,2)
ax3 = plt.subplot(4,3,3)
ax4 = plt.subplot(4,3,4)
ax5 = plt.subplot(4,3,5)
ax6 = plt.subplot(4,3,6)
ax7 = plt.subplot(4,3,7)
ax8 = plt.subplot(4,3,8)
ax9 = plt.subplot(4,3,9)
ax10 = plt.subplot(4,3,10)
ax11 = plt.subplot(4,3,11)
ax12 = plt.subplot(4,3,12)

iris = load_iris()
data = np.array(iris['data'])
targets = np.array(iris['target'])

cd = {0:'r',1:'b',2:"g"}
cols = np.array([cd[target] for target in targets])

ax1.scatter(data[:,0], data[:,1], c=cols)
ax2.scatter(data[:,0], data[:,2], c=cols)
ax3.scatter(data[:,0], data[:,2], c=cols)
ax4.scatter(data[:,0], data[:,1], c=cols)
ax5.scatter(data[:,0], data[:,2], c=cols)
ax6.scatter(data[:,0], data[:,2], c=cols)
ax7.scatter(data[:,0], data[:,1], c=cols)
ax8.scatter(data[:,0], data[:,2], c=cols)
ax9.scatter(data[:,0], data[:,2], c=cols)
ax10.scatter(data[:,0], data[:,1], c=cols)
ax11.scatter(data[:,0], data[:,2], c=cols)
ax12.scatter(data[:,0], data[:,2], c=cols)

plt.show()