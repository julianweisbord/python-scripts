#This script gives users some of the functionality of a shell script but with the added benefit of being written in Python. Instead of having to program the direct path to the directory you want to change in to, the user can use the cd ~ shortcut by calling goHome. The user cann also use cd .. shortcut by calling goBack.
#requires mac, linux, or windows powershell
import os, sys, string, time, subprocess

def goBackX(x, numElements,my_list):
    numDir= int(x)
    print numElements
    if(numDir> numElements ):
        print ("Error exiting...")
        sys.exit(0)
    if(numDir>=1):
        for y in range (0, numDir):
            my_list.pop(-1)




def goHome(numElements, my_list):
    #we can cd here
    for x in range (0,numElements-2):
        my_list.pop(-1)
    #for Element in my_list:
        #print Element
def main():
    path = str(os.getcwd())
    print ("starting directory: " + path)
    print ("Contents of current folder: \n" + subprocess.check_output(["ls"]))
    my_list = path.split("/")
    my_list.pop(0)
    numElements =0
    for Element in my_list:
        #print Element
        numElements+=1

    print("number of directories: " + str(numElements))
    #print(numElements)
    choice = raw_input("would you like to go to home or go back? (Home or Back?): \n")

    if (choice) =="Home":

        goHome(numElements, my_list)

    elif (choice)=="Back":
        a = raw_input("Back how many directories?(integer): \n")
        goBackX(a, numElements, my_list)

    replaced_string = my_list
    str_concatenate = "/"
    final_string="/"+ str_concatenate.join(replaced_string)
    print ("final string " + final_string)
    os.chdir(final_string)
    final_path = os.getcwd()
    print ("final path "+ final_path)

if __name__=='__main__':
    main()
