'''
    AUTHOR: VEYSEL BOYBAY
    STUDENT ID: 301115376
    FILE NAME: COPYFILE.PY
    DESCRIPTION: THIS PYTHON FILE HELPS USER TO COPY A FILE TO ANOTHER DESTINATION FILE.
'''
from shutil import copyfile


print("You will enter two different file names with their extensions to be copied one to another.")
source=input("Enter the source file:")
destination=input("Enter the destination file:")
check=input(f"You want to copy the whole content of {source} to the {destination},Is that correct?(y/n)")
#THIS FUNCTION IS TO ASK USER IF SHE/HE IS SURE TO COPY A FILE TO ANOTHER FILE.
if(check=='y'):
    copyfile(source,destination)
    print(f"Everything is copied to {destination}, You can check it as soon as this message prompted.")
elif(check=='n'):
    print("Thank you,see you next time.")
    exit()
else:
    print("You did not make any selection, see you!")
    exit()