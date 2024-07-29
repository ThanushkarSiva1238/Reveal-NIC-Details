import datetime

# Leap Year Dictionary
leap_year = {1: ['jan', 31], 2: ['feb', 29], 3: ['mar', 31], 4: ['apr', 30], 5: ['may', 31], 6: ['jun', 30], 7: ['jul', 31], 8: ['aug', 31], 9: ['sep', 30], 10: ['oct', 31], 11: ['nov', 30], 12: ['dec', 31]}

# Find Year
def Year(year, x):
    for i in leap_year:
        y = leap_year[i][0]
        if x > leap_year[i][1]:
            x = x - leap_year[i][1]
        else:
            break

    if year % 4 != 0:
        if y == 'feb' and x == 29:
            x = 28

    age = datetime.datetime(year, i, x)

    print("+----------------+-----------------")
    print("| Date of Birth  | %s %d, %d" % (y.title(), x, year))
    print("+----------------+-----------------")
    print("| Birth Week     | %s" % (age.strftime("%A")))




# Main Progress
print("Sri Lanka National Identity Card (NIC) Format \n---------------------------------------------")

try:
    choose = int(input("1. Find Information via NIC No \n2. Predict NIC No \nChoose (1/2) : "))

    if choose == 1:
        NIC = input("\nEnter Your NIC No : ").upper()

        if len(NIC) == 12:
            year = int(NIC[0:4])
            day = int(NIC[4:7])
            if day > 500:
                Gender = "Female"
                day = day - 500
                Year(year, day)

            else:
                Gender = "Male"
                Year(year, day)

        elif len(NIC) == 10 and (NIC[-1] == 'X' or NIC[-1] == 'V'):
            NIC = '19' + NIC[0:5] + '0' + NIC[5:9]
            print("+----------------+-----------------")
            print("| New NIC No     | %s" %(NIC))

            year = int(NIC[0:4])
            day = int(NIC[4:7])
            if day > 500:
                Gender = "Female"
                day = day - 500
                Year(year, day)

            else:
                Gender = "Male"
                Year(year, day)

        Age = datetime.datetime.now().year - year
        print("+----------------+-----------------")
        print("| Age            | %d" %(Age))
        print("+----------------+-----------------")
        print("| Gender         | %s" %(Gender))
        print("+----------------+-----------------")

    elif choose == 2:
        # Create NIC
        DOB = list(int(i) for i in input("\nDate of Birth (DD/MM/YYYY) : ").split('/'))

        if DOB[0] <= 31 and DOB[1] <= 12:
            Gender = input("Gender (M/F) : ").upper()

            Date = 0
            for month in range(1, DOB[1]):
                Date += leap_year[month][1]

            Final_Date = Date + DOB[0]

            if Gender == 'M':
                if Final_Date < 100:
                    print("NIC No : %d0%dxxxxx" % (DOB[2], Final_Date))
                else:
                    print("NIC No : %d%dxxxxx" % (DOB[2], Final_Date))

            elif Gender == 'F':
                Final = Final_Date + 500
                print("NIC No : %d%dxxxxx" % (DOB[2], Final))

        else:
            print("Check the DOB...")

except NameError and KeyError:
    print("Don't make an error")


