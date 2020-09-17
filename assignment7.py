#def inc(str):
 #   result = str[0::2]
  #  return result

#input_str = input("Enter a string: ")
#string = str(input_str)
#every_other = inc(string)
#print("Every other character: ",every_other)

# 2

#def count_digits(str):
 #   counter = 0
  #  for i in str:
   #     if i.isdigit ():
    #        counter += 1
     #   else:
      #      counter = counter
    #result = counter
    #return result

#input_str = input("Enter a string: ")
#string = str(input_str)
#digit_count = count_digits(string)

# Call the function here

#print("No. of digits:", digit_count)

# 3 
#def max_of_three(num1,num2,num3):
 #   result = max(num1,num2,num3)
  #  return result

#first = int(input("Enter first number: "))
#second = int(input("Enter second number: "))
#third = int(input("Enter third number: "))

#maximum = max_of_three(first,second,third)
#print("Maximum:", maximum)

# 4
#def is_prime(int):
 #   counter = 0
  #  if int == 2:
   #     return True
    #else:
     #   for i in range(2,int):
      #      if int % i == 0:
       #         return False
        #return True
    
        
#max_num = int(input("Input an integer greater than 1: "))
#for i in range(2,max_num+1):
 #   a = is_prime(i)
  #  if a == True:
   #     print("{} is a prime".format(i))
    #else:
     #   print("{} is not a prime".format(i))

# 6
def valid_date(str):
    for i in str:
        if str[2] != '.' or str[5] != '.':
            return False
        else:
            if len(str) != 8:
                return False
            elif 1 > int(str[:2])  or 31 < int(str[:2]):
                return False
            elif 1 > int(str[3:5])  or 12 < int(str[3:5]):
                return False
            elif 0 > int(str[6:])  or 99 < int(str[6:]):
                return False
            else:
                return True
    
date_str = input("Enter a date: ")
if valid_date(date_str) == True:
    print("Date is valid")
else:
    print("Date is invalid")  

        

