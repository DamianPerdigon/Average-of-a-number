#Write a Python program to calculate the average value of a list elements.
#Sample List:

#[20, 30, 25, 35, -16, 60, -100]

#Expected Output:

#Average value of the list elements is : 7.7.


#sum() will return the sum of all the values in the list, 
# which can be divided by the number of elements returned by the len() function

def Average(l): 
    avg = sum(l) / len(l) 
    return avg

myList = [20, 30, 25, 35, -16, 60, -100]
average = Average(myList)

print("Average value of the list elements is :", average)