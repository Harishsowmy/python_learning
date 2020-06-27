log_file=open("test.log", 'w')
name=input("enter your name: ")
age=input("enter your age: ")
phone=input("enter your phone number: ")
food=input("what is you faviort food: ")

log_file.write(f"{name} \n")
log_file.write(f"{age}\n")
log_file.write(f"{phone}\n")
log_file.write(f"{food}\n")

log_file.close()