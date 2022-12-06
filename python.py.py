#Your task to create a functionality in which when user will input a range of two dates. Then your module will find and print all years in the range of given dates those are leap years separately and rest of the years those are non-leap separately.
#For example:
#Input date range in the format dd/mm/yy
#(12/01/200) to (13/12/2025)
#Leaps years are:
#2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048.
#Non leap years are:
#2001,2002,2005,2006,2007,...........



Starting_date = input("Enter starting date in dd/mm/yyyy format: ")
Ending_date = input("Enter ending date in dd/mm/yyyy format: ")

#---------------------------------------------------------------------------------------->

day1,month1,year1 = Starting_date.split("/")
day2,month2,year2 = Ending_date.split("/")

#                                             <----------converting string to integer------------->

day1 = int(day1)
month1 = int(month1)
year1 = int(year1)


day2 = int(day2)
month2 = int(month2)
year2 = int(year2)

#                                             <-----------check for inputted month is valid or not------------->

if month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12:
    max_days = 31
elif month1 == 4 or month1 == 6 or month1 == 9 or month1 == 11:
    max_days = 30
elif year1%4 == 0 and year1%100 != 0 or year1%400 == 0:
    max_days = 29
else:
    max_days = 28

#                                              <-----------check for inputted days is valid or not-------------->

if day1 < 1 or day1 > max_days:
    print("Invalid date1")
    print("Check the day")
elif month1<1 or month1>12:
    print("Invaid date1")
    print("Check the month")
else:
    print("Inputted date_1 is valid")

#----------------------------------------------------------------------------------------->

if month2==1 or month2==3 or month2==5 or month2==7 or month2==8 or month2==10 or month2==12:
    max_days=31
elif month2==4 or month2==6 or month2==9 or month2==11:
    max_days=30
elif year2%4==0 and year2%100!=0 or year2%400==0:
    max_days=29
else:
    max_days=28
if day2<1 or day2>max_days:
    print("Invalid date2")
    print("Check the day")
elif month2<1 or month2>12:
    print("Invaid date2")
    print("Check the month")
else:
    print("Inputted date_2 is valid")

#                                   <-----------program for finding leap year and non leap year------------>
if year1 < year2:
    print("Leap year are: ")
    for i in range(year1 , year2 + 1):
        if (i % 4 == 0 and i%100 !=0 or i % 400 ==0):
            print(i , end="\t" )
        
        #break

    
    print(" \nNon leap years are: ")
    for j in range(year1 , year2 + 1):
        if (j % 4 == 0 and j%100 !=0 or j % 400 == 0):
            pass
        else:
            print(j , end = "\t")
else:
    print("Check your year input")
            
