import random
import os
import time
def autogenerate():
        while True:
            passwords=["aA16b!*cn","9%Uvz@012","de#lmG3fg","h@I8Sw4xyj","k5r#Fs78","@opiYqt#$"]
            pickset=random.choice(passwords)
            print("Generating password...")
            pickset=list(pickset)#sconverted picked password to list so if can be shuffled
            random.shuffle(pickset)
            print("ensuring password is strong...")
            password="".join(pickset) #convert bact to string for easy display
            print(f"Here you go: '{password}'\n")
            change=input("Do you like the password? Y/N: ").lower()
            if change == "y":
                  return password
            continue
        

def create_password(): # used when user wants to self create a password
      while True:
        Password=input("Enter password: ").strip()
        if not Password:
              continue
        elif len(Password) < 8 or len(Password) > 15:
              print("Password must be 8-15 characters") 
              continue
        return Password
            
# the code below just takes Id-name(key) from the user
# make sure it does not already exist
def id_name():# used as key to the password
      while True:
           id=input("\nEnter name for identification: ").strip().lower()
           if not id:# cant be empty
                 continue
           if id in passwords:
                 print("Name already exist")
                 continue
           return id
      
def add_to_list(key,value):# add password and key to dict
      passwords[key]=value
      


# this could be easily written directly where it is being called
# but it is being called more than once i guess
#is it still uneccesery?
def Check_list(dictionary):
    if not dictionary: 
      return True 
            
              
def display_passwords():
      for key,value in passwords.items():
            print(f"{key}: {value}")

# it checks if the id the user input in in the dict, it True it will
# print out the key and its value. if False it prompts the user to view all password instead
# if the user still insist's on searching, the loop restarts    
def search_password(): 
      while True:
            id=input("\nEnter identifier: ").strip().lower()
            if not id:
                  print("Cannot be empty")
                  continue
            if id in passwords:
                  print(f"{id}: {passwords[id]}")
                  return
            else:
                  print(f"Id '{id}' does not exist")
                  view=input("\nView all password instead? Y/N: ").lower()
                  if view == "y":
                        display_passwords()
                        return
                  continue

def Delete_password():
      while True:
            Delete=input("Enter password key to delete: ")
            if Delete in passwords:
                  del passwords[Delete]
                  print("Deleted succesfully")
                  return
            else:
                  print((f'The id "{Delete}" does not exist'))
                  continue

def Edit_password():
      while True:
            option=input("1: Update key\n2: update password\n?: ").strip()
            if not option:
                  continue
            elif option == "1":
                  pass # will write this later
            elif option == "2":
                  while True:
                        password=input("Enter password-key to edit: ")
                        if password in passwords:
                              print(f"{password}: {passwords[password]}\n")
                              while True:
                                    user_choice=input(f"1: Autogenerate\n2: Create yourself").strip()
                                    if not user_choice:
                                          continue
                                    elif user_choice == "1":
                                          edited=autogenerate()
                                          break
                                    elif user_choice == "2":
                                          edited=create_password()
                                          break
                              print(f"{password}: {passwords[password]}")
                              save=input("Save changes? Y/N: ").lower()
                              if save == "y":
                                    add_to_list(password,edited)
                                    return
                              continue
#used when user delects or edit anything in the data


def Add_to_file():
      with open("temppwd.db","w") as file:
            for key,value in passwords.items():
                  file.write(f"{key}: {value}\n")
            time.sleep(10)
      return True
      


def file_to_list():
      try:
            with open("password.db", "r") as file:
                  for password in file:
                        if not password.strip():
                              continue
                        key,value=password.split(":",1)
                        passwords[key]=value.strip()
      except FileNotFoundError:
            open("password.db", "x")
            return



           
           
passwords={ 
      
}         
                 

def Menu():
      print("\n-----------Menu----------")
      choice=input("1: Add password\n2: View all passwords\n3: Search password\n4: Delete password\n5: Edit password\n6: Exit\nn?: ")
      print()
      return choice

def main():

      user_choice=Menu()

      if user_choice == "1":
            iden_name=id_name()
            while True:
                option=input("1: Auto-generate\n2: Create yourself\n?: ").strip()
                if not option:
                      continue
                elif option == "1":        
                      password=autogenerate()
                      break
                elif option == "2":
                      password=create_password()
                      break
            # for you  to be able to save data to file it must first exist inside the dict
            # every iteration replaces the old data with the current 
            add_to_list(iden_name,password)
            check=Add_to_file()
            return check
      elif user_choice == "2":
            if Check_list(passwords) == True:
                  print("Nothing to show!")
            else:
                  display_passwords()
      elif user_choice == "3":
            if Check_list(passwords) == True:
                  print("No saved password!")
            else:
                  search_password()
      elif user_choice == "4":
            if Check_list(passwords) == True:
                  print("Nothing to delete")
            else:
                  Delete_password()
                  check=Add_to_file()
                  return check
      elif user_choice == "5":
            if Check_list(passwords) == True:
                  print("Empty!")
            else:
                  Edit_password()
                  check=Add_to_file()
                  return check
      elif  user_choice == "6":
            print("Good bye!")
            exit()



            
            
          
while True:
      file_to_list()
      check=main()
      if check == True:
            os.replace("temppwd.db", "password.db")
      
            