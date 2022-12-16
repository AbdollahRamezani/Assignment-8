import re
import gtts
import os
global result
result=os.listdir("../Assignment/Assignment 8")
def reade_from_file():
        global words_bank
        f=open("Assignment 8\words_bank.txt", "r")
        temp = f.read().split("\n")       #تمام کلمات داخل فایل را تبدیل به یک استرینگ بزرگ میکند  : read()
        words_bank=[]
        for i in range(0, len(temp), 2) :
                my_dict={'en':temp[i], 'fa':temp[i+1]}
                words_bank.append(my_dict)
        f.close()

def translate_english_to_persian():
    user_Sentence=input("Enter Your Sentence : ")
    user_words=re.split(r'[" ".]',user_Sentence) #اسپلیت دوتایی 
    #user_words=user_Sentence.split(" ")
    output=""
    
    for user_word in user_words:
        for word in words_bank :
         if user_word==word["en"]:
           output+=word["fa"]+" "
           break      
        else:
         output+=user_word+" "    
    print(output)   
    x=gtts.gTTS(output, lang="en", slow=False)
    x.save("Assignment 8/file_translate_Voice_english.mp3") 

def translate_persian_to_english():
    user_Sentence=input("Jomleh Khod Ra vared Namayid : ")
    user_words=re.split(r'[" ".]',user_Sentence) #اسپلیت دوتایی 
    #user_words=user_Sentence.split(" ")
    output=""
    
    for user_word in user_words:
        for word in words_bank :
         if user_word==word["fa"]:
           output+=word["en"]+" "
           break      
        else:
         output+=user_word+" "    
    print(output) 
    x=gtts.gTTS(output, lang="en", slow=False)
    x.save("Assignment 8/file_translate_Voice_persian.mp3")    
  
def add_new_word_to_database():  
 for item in result:
    if item=="words_bank.txt":
      f=open("Assignment 8\words_bank.txt", "a")
      english_word=input("enter english word : " )
      persian_word=input("enter persian word : " )
      f.write("\n"+english_word+"\n"+persian_word)
      f.close()
    
      break
 else:
      print("The file words_bank.txt does not exist in the desired path")   

    
       
 

def show_menu():
  print("WelCome To my Translate") 
  print("1_ Translate English To Persian")
  print("2_ Translate Persian To English")
  print("3_ Add a New Word To Database")
  print("4_ Exit")


reade_from_file()  

show_menu()

while True:
    
    choice=int(input("Enter Your Choice : "))
    if choice==1:
     translate_english_to_persian()
    elif choice==2:
     translate_persian_to_english()
    elif choice==3:
     add_new_word_to_database()
    elif choice==4:
     exit(0)


