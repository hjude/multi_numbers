import math, sys # import modules for this program. def is_multi (n):       function that checks if a number n is multiple of another integer k. return int(math.floor((float)pow(10,(len(str(
> create detailed step by step  script in python to  find multivariative numbers
import math, sys # import modules for this programm
def multivariate_numbers():         # function that finds the number of variables and returns a list with all possible combinations.
        n = int(input("Enter Number Of Variables : "))     # input from user to get no:of variable

       if (n <=0):                             # check for negative numbers or zeroes
           print ("Number of variables must be greater than Zero")
        else:                ##if condition is true then execute the code below.
            list = []              ###creating a empty array to store all possible combinations

                               #for loop for generating all combination with n number of variable
             i=0; j=1 ; k=-99999999999999999999999999999999  ###initializing the variables to generate all possible combinations.
            while (i < n):                   #loop for generating combination with variable number of elements          
                list.append(str(j))          ##appending each element in a string format and storing it into an array   
               j=int((k*10)**n)+9  ###incrementing the value by ten to generate all possible combinations
                 k=-99999999999999999999999999999999   #decrementing it for next iteration
                i=i+1  ###increment the counter to generate all possible combinations
            return list                       ##return a string with all combination of n number variable.
