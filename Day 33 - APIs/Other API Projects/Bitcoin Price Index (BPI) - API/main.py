import requests
from tkinter import *
from PIL import Image, ImageTk  # Import the PIL library

TITLE_FONT = ("Arial", 30, "bold")
CONVERT_RATE = ("Arial", 23, "normal")

REFRESH_INTERVAL = 15000  # 15 seconds in milliseconds


def get_rate():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    data = response.json()

    usd_data = data["bpi"]['USD']
    usd_rate = usd_data["rate"]

    gbp_data = data["bpi"]['GBP']
    gbp_rate = gbp_data["rate"]

    eur_data = data["bpi"]['EUR']
    eur_rate = eur_data["rate"]

    usd_label.config(text=f"${usd_rate}")
    gbp_label.config(text=f"£{gbp_rate}")
    eur_label.config(text=f"€{eur_rate}")

    disclaimer_label.config(text=data["disclaimer"])

    # Schedule the next data update after the refresh interval
    window.after(REFRESH_INTERVAL, get_rate)


window = Tk()
window.title("Bitcoin Price Index - BPI")
window.config(padx=50)

# Load and display the Bitcoin logo image
bitcoin_image = Image.open("bitcoin.png")  # Make sure to place the image file in the same directory as your script
bitcoin_image = bitcoin_image.resize((100, 100))  # Resize the image
bitcoin_image = ImageTk.PhotoImage(bitcoin_image)
bitcoin_label = Label(image=bitcoin_image, highlightthickness=0)
bitcoin_label.grid(row=0, column=0, columnspan=2)

usd_label = Label(text="usd", font=CONVERT_RATE)
usd_label.grid(row=1, column=0, columnspan=2)

gbp_label = Label(text="gbp", font=CONVERT_RATE)
gbp_label.grid(row=2, column=0, columnspan=2)

eur_label = Label(text="eur", font=CONVERT_RATE)
eur_label.grid(row=3, column=0, columnspan=2)

refresh_button = Button(text="Refresh", width=30, command=get_rate)
refresh_button.grid(row=4, column=0, columnspan=2)

# Add a label for the automatic refresh interval
interval_label = Label(text="Refreshing every 15 seconds...")
interval_label.grid(row=5, column=0, columnspan=2)

extra_label = Label(text="")
extra_label.grid(row=6, column=0)

disclaimer_label = Label(text="", wraplength=400)  # Adding wraplength to limit line length
disclaimer_label.grid(row=7, column=0, columnspan=2)

extra_label = Label(text="")
extra_label.grid(row=8, column=0)

copyright_label = Label(text="©️2023 - Ankit Luthra")
copyright_label.grid(row=9, column=0, columnspan=2)

get_rate()

window.mainloop()
