import tkinter as tk 
from tkinter import messagebox
import os 

class App:
    readInformationFile = open("UserInformation.txt", "r")
    readInformationFile2 = open("UserInformation.txt", "r")
    depositInformationFile = open("DepositInformation.txt", "a")

    
    firstName = ""
    lastName = ""
    location = ""
    items = ""
    
    # Destroys all widgets on the screen
    def destroy_widgets(self):
        for widgets in self.frame.winfo_children():
            widgets.destroy()
    
    # Function that will put the things that you will be depositing in the file
    def depositInformation(self):
        split_line = self.items_depositing_entry.get().split(",")

        for line in split_line:
            self.depositInformationFile.write(self.firstName + " " + self.lastName + " - " + line)

    def depositSupplies(self):
        if self.firstName == "" or self.lastName == "" or self.location == "":
            tk.messagebox.showerror("Error", "Please fill out the necessary information")
            return
        else:
            mainFont = ("Times New Roman", 20)
            # Destroying any widgets that were on the main menu
            self.destroy_widgets()

            self.first_name_label = tk.Label(self.frame, text="First Name:", font=mainFont)
            self.first_name_entry = tk.Entry(self.frame, width="28", font=mainFont)
            self.first_name_entry.insert(0, self.firstName)

            self.last_name_label = tk.Label(self.frame, text="Last Name:", font=mainFont)
            self.last_name_entry = tk.Entry(self.frame, width="28", font=mainFont)
            self.last_name_entry.insert(0, self.lastName)

            self.location_label = tk.Label(self.frame, text="Location:", font=mainFont)
            self.location_depositing_entry = tk.Entry(self.frame, width="28", font=mainFont)
            self.location_entry.insert(0, self.location)

            self.items_label = tk.Label(self.frame, text="Items Depositing:", font=mainFont)
            self.items_depositing_entry = tk.Entry(self.frame, width="28", font=mainFont)

            self.submit_button = tk.Button(self.frame, text="Submit", command=self.depositInformation)

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

    def uploadInformation(self):
        # This method uploads the information retreived from the getSupplies() method and uploads them to the UserInformation.txt file
        self.firstName = self.first_name_entry.get()
        self.lastName = self.last_name_entry.get()
        self.location = self.location_entry.get()
        # The error is here, find a way to get all the items in the thing

        lines = []

        self.full_name = self.first_name_entry.get() + " " + self.last_name_entry.get()
        self.first_name = self.first_name_entry.get()
        self.last_name = self.last_name_entry.get()
        self.location = self.location_entry.get()
        self.items = self.items_entry.get()

        # Because this is an individualized app, the user can only enter their own name
        # Check if the lines equal 0
        if os.path.getsize("UserInformation.txt") > 0:
            for line in self.readInformationFile:
                if self.firstName in line and self.lastName in line:
                    lines.append(line + " / " + self.items)
                    
        else:
            lines.append("Full Name: " + self.full_name + " Location: " + self.location + " Items: " + self.items)
            self.items += " / " + self.items_entry.get()

        uploadInformationFile = open("UserInformation.txt", "w")
        for l in lines:
            uploadInformationFile.write(l)
        
        uploadInformationFile.close()


    # Function that finds the users that have the items you are looking for
    def findLocations(self):
        self.destroy_widgets()

        self.personFoundValue = tk.StringVar()
        self.testLabel = tk.Label(self.frame, textvariable=self.personFoundValue)

        # needs to loop through the file and then find users that have the items the user is looking for and then display their info
        split_line = []
        items = []
        self.personFound = ""
        

        for line in self.readInformationFile2:
            split_line = line.split(" ")
            break
        

        starting_index = split_line.index("Items:")

        for i in range(starting_index + 1, len(split_line) - 1):
            items.append(split_line[i])

        with open("LocalInformation.txt") as f:
            for line in f:
                for item in items:
                    if item in line:
                        split_line = line.split(" ")
                        print (split_line)

                        self.personFound = split_line[2] + " " + split_line[3]
                        self.personFoundValue.set(self.personFound)
                        break
        
        self.menuButton = tk.Button(self.frame, text="Menu", command=self.main_menu)

        self.testLabel.pack()
        self.menuButton.pack()

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
        self.find_button = tk.Button(self.frame, text="Find", command=self.findLocations)

    
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

        self.find_button.pack()
        self.submit_button.pack()

        self.backButton.pack()

    def main_menu(self):
        # Destroying any widgets that may be on the screen from the previous screen
        self.destroy_widgets()
        # Placing the buttons that will be on the main menu screen
        self.getSuppliesButton = tk.Button(self.frame, text="Get Supplies", command=self.getSupplies)
        self.depositSuppliesButton = tk.Button(self.frame, text="Deposit Supplies", command=self.depositSupplies)

        # Packing all the buttons 
        self.getSuppliesButton.pack()
        self.depositSuppliesButton.pack()

    # The init method
    def __init__(self):
        self.frame = tk.Tk()
        self.frame.geometry("600x400")
        self.main_menu()
        self.frame.mainloop()

# Creating a new app object
app = App()

# Closing all the files used in this program
app.readInformationFile.close()
app.readInformationFile2.close()
app.depositInformationFile.close()