import tkinter as tk
import pandas as pd

# Create a tkinter app
app = tk.Tk()
app.title("Ottomate App")
app.geometry("300x200")

# Create a function that opens the second page
def open_second_page():
    # Close the first page
    page1.destroy()

    # Create the second page
    page2 = tk.Frame(app)
    page2.pack()

    # Read the data from an Excel file
    df = pd.read_excel("my_data.xlsx")

    # Create the three text fields
    rainy_text = tk.StringVar()
    summer_text = tk.StringVar()
    winter_text = tk.StringVar()

    rainy_label = tk.Label(page2, text="Rainy")
    rainy_label.pack()

    rainy_entry = tk.Entry(page2, textvariable=rainy_text)
    rainy_entry.pack()

    summer_label = tk.Label(page2, text="Summer")
    summer_label.pack()

    summer_entry = tk.Entry(page2, textvariable=summer_text)
    summer_entry.pack()

    winter_label = tk.Label(page2, text="Winter")
    winter_label.pack()

    winter_entry = tk.Entry(page2, textvariable=winter_text)
    winter_entry.pack()

    # Create the read and write buttons
    def read_data():
        rainy_text.set(df.loc[0, "Rainy"])
        summer_text.set(df.loc[0, "Summer"])
        winter_text.set(df.loc[0, "Winter"])

    def write_data():
        df.loc[0, "Rainy"] = rainy_text.get()
        df.loc[0, "Summer"] = summer_text.get()
        df.loc[0, "Winter"] = winter_text.get()
        df.to_excel("my_data.xlsx", index=False)

    read_button = tk.Button(page2, text="Read Data", command=read_data)
    read_button.pack()

    write_button = tk.Button(page2, text="Write Data", command=write_data)
    write_button.pack()

    # Create the back button
    def go_back():
        # Close the second page
        page2.destroy()
        # Reopen the first page
        page1.pack()

    back_button = tk.Button(page2, text="Back", command=go_back)
    back_button.pack()

# Create the first page with the "ottomate" button
page1 = tk.Frame(app)
page1.pack()

ottomate_button = tk.Button(page1, text="Ottomate", command=open_second_page)
ottomate_button.pack()

# Start the tkinter event loop
app.mainloop()
