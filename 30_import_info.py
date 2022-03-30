'''import sklearn as sk
print(sk.__version__)'''
#never make any file with the same name of module

# to know how we get and from where we get all modules. it has another module
'''import sys
print(sys.path)'''


# RandomForestClassifier is a class and it is basically use in machine learning. it is a ensemble classifier
'''from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())'''


#we can import one file data to another file for use of that data
#lets make from_data_import.py and import data from that file to current file
import from_data_import
print(from_data_import.testing) # 'testing' is a variable in from_data_import.py file
print(from_data_import.testClass("This is me")) # 'testClass()' is a user define class in from_data_import.py file