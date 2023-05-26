import os

# create a flag to know if the scheduler is running or not
f = open('/home/vikram/Documents/Scripts/var.py')
lines = f.readlines()
flag = lines[-1]
print(type(flag))
flag = int(flag)
print(type(flag))

# if not running then make it run 
# else kill the process
# update the flag in both cases
if flag == 0:
    os.system("python3 /home/vikram/Documents/Scripts/main.py")
    flag = 1

elif flag == 1:
    print("entered termination")
    flag = 0
    with open('/home/vikram/Documents/Scripts/var.py', 'w') as f:
        print("flag value after changing term: ", flag)
        f.write(str(flag))
    os.system("killall python3")
    
else:
    print("Some problem")

# changing flag value
with open('/home/vikram/Documents/Scripts/var.py', 'w') as f:
    print("flag value after if else: ", flag)
    f.write(str(flag))



