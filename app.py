import customtkinter as ctk
import requests # to call the genius API

access_token = "p_o14Y47yGd0SBvmPdGIAS16IFclamd1UZ9IyzRZhb7yrQPoCcrLEYkY3IQRz-Ap"  
# The API needs to know who we are (our identity) before giving us data.
# To do this, we send an "Authorization" header with our secret token.
# "Bearer" is a fixed keyword used in APIs to say: "I have a token to prove who I am."
# {access_token} is our unique key given by the API service.
headers = { "Authorization": f"Bearer {access_token}"} 

app = ctk.CTk() #creating the window
app.title("VibeVerse")
app.geometry("500x300")

# a function to display the text we typed 
def searchtextdisplay():  
    text_typed = entry.get()  #get the text typed in the entry 
    #print(text_typed) # testing
    parts = text_typed.split('-')
    if len(parts) == 2:
        artist = parts[0].strip()  #strip remove extra whitespaces from before the string so only the first word typed will count no spaces
        song = parts[1].strip()
        label_display_what_typed.configure(text=f"You searched for: {artist}\nSong: {song}")
    else:
        label_display_what_typed.configure(text=f"Please enter in 'Artist - Song' format: ")


# added labels displayed in the gui like type the song name label the entry (where to type) 
# the button (we linked it to the function thru command) 
label = ctk.CTkLabel(app, text="please type the song you want to analyse:")
label.pack()

entry=ctk.CTkEntry(app, width=300)
entry.pack()

button=ctk.CTkButton(app, text="click here", width=20, command=searchtextdisplay)
button.pack()

label_display_what_typed = ctk.CTkLabel(app, text="")
label_display_what_typed.pack()

app.mainloop()
