
#NAME                   WALAGA PRISCILLA  N. EDITH
#REGISTRATION NUMBER    16/U/12253/PS






import calendar  #importing inbuilt calendar module
a=input("What is your year of birth?\n")
b=input("Enter your month of birth  (enter number e.g for december enter 12\n")        
c=input("Enter the date on which you were born(1-30)\n")
x=calendar.weekday(year=int(a), month=int(b), day=int(c)) #module gives the index of the day from the list ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#Applying a conditional function to assign each date a corresponding prefix
if int(c) == 1:
    d = c +"st"
elif int(c)==2:
    d = c +"nd"
elif int(c)==3:
    d = c +"rd"
elif int(c) >= 4 and int(c) <= 20:
    d = c +"th"
elif int(c)==21:
    d = c +"st"
elif int(c) == 22:
    d = c +"nd"
elif int(c) == 23:
    d = c +"rd"
elif int(c) == 31:
    d = c +"st"
else:
    d = c+"th"



#Applying a conditional func

    #Applying a conditional function to assign the result from the module used to the respective day
if x == 0:
    y = "Monday"
elif x == 1:
    y = "Tuesday"
elif x == 2:
    y = "Wednesday"
elif x == 3:
    y = "Thursday"
elif x == 4:
    y = "Friday"
elif x == 5:
    y = "Saturday"
else:
    y = "Sunday"

print("We you were born on "+y+" "+d)
input("Press enter")
