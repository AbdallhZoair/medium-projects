
import string

student_name = []
student_number =[]
count_add_studnet = 0
To = 0
while To == 0:
 To = int(input("""Enter :
                1 : To Display All Student
                2 : To Enter Student
                3 : To Delete Student
                4 : To search for a student
                5 : To Exit
                
                  : """))
 while To == 1 :
     if len(student_name) != 0 :
        print(f"Ther is : {len(student_name)} Student and ther info is :")
        
        for A in range(len(student_name)):
         print(f"The Student name is : ({student_name[A]})\nand hes number is :({student_number[A]})\n")
         print("---------")
        break

     else :
       print ("Ther Is No Student Yet... \n")
       break

 
 while To == 2 :

   while True :
    test_student_info = input(f"Enter the Number belong to Student Number {count_add_studnet+1} : " )

    if test_student_info.isdigit():
      test_student_info = int(test_student_info)
      if (test_student_info not in student_name) and (test_student_info not in student_number):
        student_number.append(test_student_info)
        test_student_info = (input(f"Enter the Name Of Student {count_add_studnet+1} : " ))
        student_name.append(test_student_info)
        count_add_studnet += 1
        break

      else :
        print("your  elready get this")
        break
    else :
      print("you must Enet just digits first")
      break
      
      
  
   To = input("\nEnter num 1 to Enter  student \nelse to close : \n")
   if To == "1":
       To = 2
   else :
       To = 0
   
 while To == 3 :
    delete_code = input("Enter the number or name for student you want to delete : ")
  
    if delete_code.isdigit():
      delete_code = int(delete_code)

    if delete_code in student_name :
        delete_index = student_name.index(delete_code)
        print(f"The student ({student_name[delete_index]}) is seccful removed")
        student_name.pop(delete_index)
        student_number.pop(delete_index)

    
    elif delete_code in student_number :
        delete_index = student_number.index(delete_code)
        print(f"The student numbere ({student_number[delete_index]}) is seccful removed")
        student_name.pop(delete_index)
        student_number.pop(delete_index)
     
    else :
         print("Invalid input ...")

    To = input("Enter num 1 to Try again \nelse to close : \n")
    if To == "1":
      To = 3
    else :
      To = 0
      
 while To == 4 :
    search_code = input("Enter the number or name for student you want to see : ")
    
    if search_code.isdigit():
        search_code = int(search_code)
    
    if search_code in student_name :
       search_index = student_name.index(search_code)
       print("The studint is :" , student_name[search_index] , " and hes number is :" , student_number[search_index])
 
    elif search_code in student_number :
        search_index = student_number.index(search_code)
        print("The studint is :" , student_name[search_index] , " and hes number is :" , student_number[search_index])
    else :
        print("no found")
    To = input("Search agian(Enter 1)\nExsit (Enter any Think)") 
    if To == "1":
        To = 4
    else :
        To = 5


if To != 5 :
 To = input("\nEnter 1 To see the main page \nelse to Exit : \n")
 if To == "1":
    To = 0
 else :
     To = 5

while To == 5 :
 print("its good to see you man")
 exit()
