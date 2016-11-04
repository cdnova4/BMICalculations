from pylab import *
import matplotlib.pyplot as plot
from math import sqrt
#Developer: Christian DeGenova
#Section: CSC325 Databases
#Due Date: October 14, 2016
#Assignment: Part 2 BMI Calculations

#Defines the class person
class person:
    # the constructor of class person
    def __init__(self,w,h,a, chest_diam, chest_dep, bitro_diam,wrist_g, ankle_g):
        self.w = w
        self.h = h
        self.a = a
        self.chestDiam = chest_diam
        self.chestDep = chest_dep
        self.bitroDiam = bitro_diam
        self.ankleG = ankle_g
        self.wristG = wrist_g

        # calls the two methods below for the BMI equation and the Formula
        self.BMI = self.getBMIEquation()
        self.formula = self.getForm()

    # defines the function with the formula given in the problem statement
    def getForm(self):
        return -110 + 1.34 * (self.chestDiam) + 1.54 * (self.chestDep) + 1.20 * (self.bitroDiam) + \
               1.11 * (self.wristG) + 1.15 * (self.ankleG) + 0.177 * (self.h)

    #defines the function with the BMI formula
    def getBMIEquation(self):
        return (self.w)/(self.h/100)**2


#This holds the BMI data which is called in using the for loop below line by line from the bod.dat.txt file
people = []
with open('body.dat.txt') as i:
    for line in i:
        a = float(line[110] + line[111] + line[112] + line[113])
        w = float(line[115] + line[116] + line[117] + line[118] + line[119])
        h = float(line[121] + line[122] + line[123] + line[124] + line[125])
        chest_diam = float(line[20] + line[21] + line[22] + line[23])
        chest_depth = float(line[15] + line[16] + line[17] + line[18])
        bitro_diam = float(line[10] + line[11] + line[12] + line[13])
        wrist_g = float(line[105] + line[106] + line[107] + line[108])
        ankle_g = float(line[100] + line[101] + line[102] + line[103])
        people.append(person(w, h, a, chest_diam, chest_depth, bitro_diam, wrist_g, ankle_g))

# List for the weight(x value) and formula(y value)
x_weight = []
y_formula = []
for person in people:
    x_weight.append(person.w)
    y_formula.append(person.formula)

#List for the age(x value) and BMI(y value)
x_age = []
y_BMI = []
for person in people:
    x_age.append(person.a)
    y_BMI.append(person.BMI)


#Function to find sum of list items squared
def squaredListSum(x):
    listSum = [i ** 2 for i in x]
    return np.sum(listSum)

#Function to find product of list items
def productListSum(x,y):
    listSum = 0
    for i in range(len(x)):
        listSum += x[i] * y[i]
    return listSum

#Function to create regression line
def regressionLine(slope, inter, x):
    tempList = [inter]
    for i in range(120):
        yVal = (slope*i) + inter
        tempList.append(yVal)
    return tempList

#Defines the slope function which returns the the formula for the slope equation
def slope(n, xy_sum, x_sum, y_sum, x_sum_squared):
    return (n * xy_sum - (x_sum * y_sum)) / (n * x_sum_squared - (x_sum) ** 2)
#Defines the intercept function which returns the formula of intercept equation
def intercept(n, y_sum, x_sum, slope):
    return (y_sum - (slope * x_sum)) / n
#Defines the correlation function which returns the the formula for the correlation equation
def correlation(n, xy_sum, x_sum, y_sum, x_sum_squared, y_sum_squared):
    return (n * xy_sum - (x_sum * y_sum)) / sqrt((n * x_sum_squared - x_sum ** 2) * (n * y_sum_squared - y_sum ** 2))



# AGE vs BMI data
slope_bmi = slope(len(x_age), productListSum(x_age, y_BMI), np.sum(x_age), np.sum(y_BMI), squaredListSum(x_age))
intercept_bmi = intercept(len(x_age), np.sum(y_BMI), np.sum(x_age), slope_bmi)
correlation_bmi = correlation(len(x_age), productListSum(x_age, y_BMI),np.sum(x_age), np.sum(y_BMI), squaredListSum(x_age),squaredListSum(y_BMI))
print "AGE vs BMI Data"
print "**********************************"
print "Slope of Age vs BMI: " + str(slope_bmi)
print "Correlation Age vs BMI: " + str(correlation_bmi)
print "Intercept of Age vs BMI: " + str(intercept_bmi)
print "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\"

#Plots the scatter plot for BMI vs Age and sets the labels, color settings
plot.figure(1)
ax = plt.gca()
ax.set_axis_bgcolor('black')
plot.scatter(x_age, y_BMI, color="blue")
plot.plot(regressionLine(slope_bmi, intercept_bmi, x_age), color="yellow")
plot.title("Age vs BMI")
plot.xlabel("Age")
plot.ylabel("BMI")




# Weight vs Formula data
slopeForm = slope(len(x_weight), productListSum(x_weight, y_formula), np.sum(x_weight), np.sum(y_formula), squaredListSum(x_weight))
interceptForm = intercept(len(x_weight), np.sum(y_formula), np.sum(x_weight), slopeForm)
correlationForm = correlation(len(x_weight), productListSum(x_weight, y_formula),np.sum(x_weight), np.sum(y_formula), squaredListSum(x_weight),squaredListSum(y_formula))
print "Weight vs Formula Data"
print "**********************************"
print "Slope of Weight vs Formula: " + str(slopeForm)
print "Correlation of Weight vs Formula: " + str(correlationForm)
print "Intercept of Weight vs Formula: " + str(interceptForm)
print "--------------------------------------------------"

#Plots the scatter plot for Weight vs Formula and sets the labels, color settings
plot.figure(2)
ax = plt.gca()
ax.set_axis_bgcolor('black')
plot.plot(regressionLine(slopeForm, interceptForm, x_weight), color="yellow")
plot.scatter(x_weight, y_formula, color="blue")
plot.title("Weight vs Formula")
plot.xlabel("Weight")
plot.ylabel("Formula")
plot.show()
