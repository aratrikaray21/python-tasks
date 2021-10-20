import csv
import sys
import pandas
def write_csv(l):
    with open('Student_information.csv','a',newline='') as csv_file:
        w=csv.writer(csv_file)
        if csv_file.tell()==0:
            w.writerow(['Roll number','Name','Contact number','Email id'])
        w.writerow(l)
def read_csv():
    with open('Student_information.csv','r') as csv_file:
        reader = csv.reader(csv_file, delimiter = '\t')
        for row in reader:
            print(row)
def dict_read_csv():
    reader=csv.DictReader(open('Student_information.csv'))
    for row in reader:
        print(row)
def pandas_read_csv():
    read=pandas.read_csv('Student_information.csv')
    print(read)
if __name__=='__main__':
    st=1
    condition=True
    while condition:
        print("\nEnter the student {} information-->".format(st))
        rno=int(input("Enter student roll number:"))
        if 1<=rno<60:
            name=input("Enter student name:")
            pno=int(input("Enter student contact number:"))
            if len(str(pno))==10:
                email=input("Enter student email id(more than or equal to 8 characters):")
                if '@' in email and '.com' in email and len(email)>=8:
                    print("All information entered!")
                else:
                    print("Invalid email id")
                    sys.exit()
            else:
                print("Invalid phone number")
                sys.exit()
        else:
            print("Invalid roll number/Total number of students are 60")
            sys.exit()
        print("\nDisplaying entered information->")
        print("Roll number: {}\nStudent name: {}\nContact number: {}\nEmail id: {}".format(rno,name,pno,email))
        check=input("Do you want to make any changes to the above information?(y/n):").casefold()
        l=[rno,name,pno,email]
        if check=='n':
            write_csv(l)
            st+=1
            check1=input("Do you want to enter information for more students?(y/n):").casefold()
            if check1=='y':
                condition=True
            elif check1=='n':
                print("Displaying information entered-->")
                read_csv()
                print("Displaying in a dictionary format-->")
                dict_read_csv()
                print("Displaying in dataframe format-->")
                pandas_read_csv()
                condition=False
            else:
                print("Please enter y for yes and n for no.")
        elif check=='y':
            print("Please re-enter the information")
        else:
            print("Please enter y for yes and n for no.")
