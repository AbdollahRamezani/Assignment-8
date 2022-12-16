import gtts  #pip install gtts
my_text=input("Enter Yor Text : ")
file_name_voice=input("Enter Your File Name Voice To save : ")
x=gtts.gTTS(my_text, lang="en", slow=False)
x.save("Assignment 8/"+file_name_voice+".mp3")












