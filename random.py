#My take on John von Neumann's random number generator using middle-square method.
#outputs a number between 1 and 9
import calendar
import time
print "Date: ", calendar.timegm(time.gmtime())
def get_input():
    check = False
    while(check ==False):
        inp = raw_input("Enter a posotive seed number for your random number generation (atleast 2 digits): \n")
        if(len(inp)==0):
            inp = calendar.timegm(time.gmtime())
            return inp

        elif(len(str(inp))>=2):
            check = True
            break
        else:
            print ("Number must be greater than 1 digit.\n")
    return inp
#Multiply number and take off first and last characters.
def manipulate():
    inp = get_input()
    inp = long(inp) * long(inp)
    #print inp
    inp = str(inp)
    inp = inp[:-1]
    inp = inp[1:]
    #print ("this is inp without first and last digits: " + str(inp))
    inp_counter = 0
    zeros = False
    numLoops = 0
    #print ("This is inps length " + str(len(inp)))
    for length in inp:
        numLoops +=1
        if(length == '0'):
            #print ("we encountered a zero at position: " + str(inp_counter) + " here it is: " + length)
            zeros = True
            inp_counter +=1

    #print("number of loops " + str(numLoops))
    #print ("zeros is " + str(zeros))
    #print ("This was number of zeros found " + str(inp_counter))
    if(zeros == True):
        #took out longs on inps
        new_num = long(inp) + long(inp_counter**2)
    else:
        new_num = long(inp)
    #print new_num
    return new_num
#This is where the seed number is changed to make the algorithm harder to guess.
def mathing():
    new_num = manipulate()
    new_num = new_num+(new_num**(.5)) +1
    int_str =  (str(int(new_num)) + "\n")
    #print ("int str " + int_str)
    counter = -1
    for numbers in int_str:
        counter+=1
    #print ("here is the counter " + str(counter))

    divide_str = "1"
    for x in xrange (0,counter-1):
        divide_str = divide_str + "0"
    #print divide_str
    final_num = long(new_num)/long(divide_str)
    print ("final num out of ten " + str(final_num))

if __name__=='__main__':
    mathing()
