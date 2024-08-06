name=input("What is your name ? ")
age=int(input("What is your age ? "))
new_Patient=input("Are you new patient ? y or n " )
if new_Patient =="y":
    is_patient=True
else:
    is_patient=False

print("Hello "+name+"\nYour  "+ str(age)+" "+str(is_patient))