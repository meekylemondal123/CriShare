import tkinter as tk 
from tkinter import messagebox
import os 

class App:
    
    readInformationFile = open("UserInformation.txt", "r")

    firstName = ""
    lastName = ""
    location = ""

    def destroy_widgets(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
    
    def depositSupplies(self):
        self.destroy_widgets()


        self.backButton = tk.Button(self.frame, text="Back", command=self.main_menu)

        self.backButton.pack()

    def uploadInformation(self):
        # This method uploads the information retreived from the getSupplies() method and uploads them to the UserInformation.txt file
        self.firstName = self.first_name_entry.get()
        self.lastName = self.last_name_entry.get()
        self.location = self.location_entry.get()
        lines = []

        full_name = self.first_name_entry.get() + " " + self.last_name_entry.get()
        location = self.location_entry.get()
        items = self.items_entry.get()

        # Because this is an individualized app, the user can only enter their own name
        # Check if the lines equal 0
        if os.path.getsize("UserInformation.txt") > 0:
            for line in self.readInformationFile:
                if self.firstName in line and self.lastName in line:
                    lines.append(line + " " + items)
                else:
                    tk.messagebox.showerror("Error", "Please only enter your own name or else all of your information so far will be deleted")
        else:
            lines.append("Full Name: " + full_name + " Location: " + location + " Items: " + items)

        uploadInformationFile = open("UserInformation.txt", "w")
        for l in lines:
            uploadInformationFile.write(l)
        
        uploadInformationFile.close()


    def getSupplies(self):
        mainFont = ("Times New Roman", 20)
        # Destroying any widgets that were on the main menu
        self.destroy_widgets()

        self.first_name_label = tk.Label(self.frame, text="First Name:", font=mainFont)
        self.first_name_entry = tk.Entry(self.frame, width="28", font=mainFont)

        self.last_name_label = tk.Label(self.frame, text="Last Name:", font=mainFont)
        self.last_name_entry = tk.Entry(self.frame, width="28", font=mainFont)

        self.location_label = tk.Label(self.frame, text="Location:", font=mainFont)
        self.location_entry = tk.Entry(self.frame, width="28", font=mainFont)

        self.items_label = tk.Label(self.frame, text="Items:", font=mainFont)
        self.items_entry = tk.Entry(self.frame, width="28", font=mainFont)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.uploadInformation)
        # Place this on the bottom left of the screen
        self.backButton = tk.Button(self.frame, text="Back", command=self.main_menu)

        # Packing all of the elements
        self.first_name_label.pack()
        self.first_name_entry.pack()
        self.last_name_label.pack()
        self.last_name_entry.pack()
        self.location_label.pack()
        self.location_entry.pack()
        self.items_label.pack()
        self.items_entry.pack()
        self.submit_button.pack()

        self.backButton.pack()

    def main_menu(self):
        # Destroying any widgets that may be on the screen from the previous screen
        self.destroy_widgets()
        print (self.firstName + " " + self.lastName + " " + self.location)
        # Placing the buttons that will be on the main menu screen
        self.getSuppliesButton = tk.Button(self.frame, text="Get Supplies", command=self.getSupplies)
        self.depositSuppliesButton = tk.Button(self.frame, text="Deposit Supplies", command=self.depositSupplies)

        # Packing all the buttons 
        self.getSuppliesButton.pack()
        self.depositSuppliesButton.pack()

    def __init__(self):
        self.frame = tk.Tk()
        self.frame.geometry("600x400")
        self.main_menu()
        self.frame.mainloop()

app = App()
app.readInformationFile.close()
