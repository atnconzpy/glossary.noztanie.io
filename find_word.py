import pandas as pd
import numpy as np


dt = pd.read_csv("dict_new.csv")

#Main
key = input("ENTER THE WORD YOU WANT TO LOOK UP: ").lower()

while key != "quit":
    
    for i in dt["Key"]:
        a = key.lower()
        i_str = str(i).strip().lower()
        
        if a == i_str or a in i_str:
            df = dt[dt.Key == i]
            x = str(df["Mean"]).split()
            del x[0]
            del x[x.index("Name:"):]
            y = " ".join(x)
            print("-->",i_str.title(),":",y)
            print("\n")
   

    key = input("ENTER THE WORD YOU WANT TO LOOK UP: ").lower()

else:
    print("See you late <3")
















# Function

# def translate(word):
#     for i in dt["Key"]:
#         a = word.lower()
#         i_str = str(i).strip().lower()


#         if a in i_str or a == i_str:
#             df = dt[dt.Key == i]
#             x = str(df["Mean"]).split()
#             del x[0]
#             del x[x.index("Name:"):]
#             y = " ".join(x)
#             return i,":",y
    






# for i in dt["Key"]:
#     a = "fan token".lower()
#     i_str = str(i).strip().lower()
    
    
#     if a in i_str or a == i_str:
#         df = dt[dt.Key == i]
#         print(df["Mean"])

