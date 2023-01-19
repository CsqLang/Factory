'''
This is the runner of Csq code which calls Csq compiler.
'''
#Getting dependencies
import os
import sys
#Get current directory.
def currentDirectory():
    return os.getcwd()
#Find Csq compiler
def CsqCompilerPath(current):
    return current + "/Csq4/"
#Build alias
def BuildAlias(current):
    os.system(f"alias factory ./{current}/factory/factory")
#Run code
def Run(module):
    os.system("/"+CsqCompilerPath(currentDirectory()) + "/csq main " + currentDirectory()+"/"+module + f" {CsqCompilerPath(currentDirectory())}")

'''
Driver code
'''
if __name__ == "__main__":
    Run("test")
