# from pathlib import Path
# import os
# def readfileandfolder():
#     path=Path('')
#     items=list(path.rglob('*'))
#     for i , items in enumerate(items):
#         print(f"{i+1}:{items}")

# print("press 1 for create a file:-")     
# print("press 2 for reading a file:-")
# print("press 3 for updating a file")
# print("press 4 for deleting a file:-")
# check=int(input("please tell your response:-"))
# def createfile():
    
      
#     readfileandfolder()
#     name=input("please tell your file name:-")
#     p=Path(name)
#     if not p.exists():
#         with open(p,'w')as fs:
#             data=input("what you want to write in this file:-")
#             fs.write(data)
#             print(f"File create succefully")
#     else:
#         print("This file already exist")


# if check==1:
#     createfile()

# def readfile():
#     readfileandfolder()
#     name=input("which file you want to read:-")
#     p=Path(name)
#     if p.exists() and p.is_file():
#         with open(p,'r') as fs:
#             data=fs.read()
#             print(data)
#             print("Readed successfully")
#     else:
#         print("The file does not exists")

# if check==2:
#     readfile()     

# def updatfile():
#     readfileandfolder()
#     name=input("Tell which file you want to update:-")
#     p=Path(name)
#     if p.exists() and p.is_file():
#         print("press 1 for changing the name of file:-")
#         print("press 2 for changing the overwriting data of file:-")
#         print("press 3 for changing the appending some content the data of file:-")

#         res=int(input("tell your response:-"))

#         if res==1:
#             name2=input("tell your new file name:-")
#             p2=Path(name2)
#             p.rename(p2)

#         if res==2:
#             with open(p,'w')as fs:
#                 data=input("tell what want you overwrite in file:-")
#                 fs.write(data)

#         if res==3:
#             with open(p,'a')as fs:
#                 data=input("Tell what you want to append in this file:-")
#                 fs.write(""+ data)

# if check==3:
#     updatfile()                


# def deletefile():
#     readfileandfolder()
#     name=input("Tell which file you want to delete:-")
#     p=Path(name)
#     if p.exists() and p.is_file():
#         os.remove(p)
#         print("File remove succefully")
#     else:
#         print("No such file exists")   
      
# if check==4:
#     deletefile()