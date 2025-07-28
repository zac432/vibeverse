import customtkinter as ctk
import requests # to call the genius API

access_token = "p_o14Y47yGd0SBvmPdGIAS16IFclamd1UZ9IyzRZhb7yrQPoCcrLEYkY3IQRz-Ap"  

# Bearer is a fixed keyword used in APIs to say: I have a token to prove who I am.
headers = { "Authorization": f"Bearer {access_token}"} 

app = ctk.CTk() #creating the window
app.title("VibeVerse")
app.geometry("500x300")

# a function to display the text we typed 
def searchtextdisplay():  
    text_typed = entry.get()  #get the text typed in the entry 
    parts = text_typed.split('-')

    if len(parts) == 2:
        artist = parts[0].strip()  #strip remove extra whitespaces from before the string so only the first word typed will count no spaces
        song = parts[1].strip()
        query= f"{artist} {song}" #search query f string that takes 2 vaiables artist and song
        url = f"https://api.genius.com/search?q={query}" #the url to search throught  the genius app for what we r looking for 
        response=requests.get(url, headers=headers) #requesting the url through get request 
        data=response.json() #getting the response and saving it as a dictionary data variable 

         # Check if we got results  write and if statement to check and add handle errors 
        if data["response"]["hits"]:
            first_hit = data["response"]["hits"][0]["result"]  # Take the first result
            title = first_hit["full_title"]  # e.g., "Hello by Adele"
            release_date = first_hit.get("release_date_for_display", "N/A")
            lyrics_url = f"https://genius.com{first_hit['path']}"
            
            # Show details in the label
            label_display_what_typed.configure(
                text=f"Title: {title}\nRelease Date: {release_date}\nLyrics: {lyrics_url}"
            )
        else:
            label_display_what_typed.configure(
                text="No song found. Try again."
            )
    else:
            label_display_what_typed.configure(
                text="Please enter in 'Artist - Song' format.")


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
