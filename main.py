import customtkinter as ctk
import tkinter as tk
import requests
from PIL import ImageTk, Image


window = ctk.CTk()
window.geometry("400x460")
window.title("Converter")
window.resizable(False, False)

image_convert = Image.open("Images/exchange.png")
but_convert = ctk.CTkImage(image_convert)
image_back = Image.open("Images/left-arrow.png")
but_back = ctk.CTkImage(image_back)

def back_command():
    back_frame.pack_forget()
    top_frame.pack_forget()
    middle_frame.pack_forget()
    bottom_frame.pack_forget()
    first_frame.pack(pady=30)



def menu():
    global first_combobox, second_combobox, entry, label, convert_button, back_frame, top_frame, middle_frame, bottom_frame
    back_frame = ctk.CTkFrame(window, fg_color="transparent")
    back_frame.pack()
    top_frame = ctk.CTkFrame(window, fg_color="transparent")
    top_frame.pack(pady=35)
    middle_frame = ctk.CTkFrame(window, fg_color="transparent")
    middle_frame.pack(pady=20)
    bottom_frame = ctk.CTkFrame(window, fg_color="transparent")
    bottom_frame.pack(pady=35)
    back_button = ctk.CTkButton(back_frame, width= 30,height=30, image=but_back, text="", fg_color="#FF7518", hover_color="#F08000", corner_radius=80, command= back_command)
    back_button.pack(padx = (0,320), pady = (10,0))
    entry = ctk.CTkEntry(top_frame, width=100, height=70, font=('Helvetica', 25), justify="center")
    entry.pack(side=tk.LEFT)
    first_combobox = ctk.CTkComboBox(top_frame, width=140, height=70, font=('Helvetica', 25), values=["1", "2", "3"], justify="center")
    first_combobox.pack(side=tk.LEFT)
    convert_button = ctk.CTkButton(middle_frame, height=70,image=but_convert, text="Convert", fg_color="#FF7518", hover_color="#F08000", corner_radius=40, command= lambda : print("error"))
    convert_button.pack()
    label = ctk.CTkLabel(bottom_frame, width=100,text="0", height=70, font=('Helvetica', 25), justify="center")
    label.pack(side=tk.LEFT)
    second_combobox = ctk.CTkComboBox(bottom_frame, width=140, height=70, font=('Helvetica', 25), values=["1", "2", "3"], justify="center")
    second_combobox.pack(side=tk.LEFT)


def Length_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = lengths_dict[choice1]
    number2 = lengths_dict[choice2]
    diff = number2 - number1
    if diff > 0:
        sonuc = int(veri) * (10**diff)
    elif diff < 0:
        diff = -1 * diff
        count = int(veri) * (1/(10**diff))
        sonuc = round(count, 2)
    else:
        sonuc = veri

    label.configure(text=sonuc)


def Weight_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = weight_dict[choice1]
    number2 = weight_dict[choice2]
    diff = number2 - number1
    if diff > 0:
        sonuc = int(veri) * (10**diff)
    elif diff < 0:
        diff = -1 * diff
        count = int(veri) * (1/(10**diff))
        sonuc = round(count, 2)
    else:
        sonuc = veri

    label.configure(text=sonuc)


def Temperature_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = temperature_dict[choice1]
    number2 = temperature_dict[choice2]
    if number1 == 1 and number2 == 2:
        sonuc = round(((int(veri) * (9/5)) + 32),2)
    elif number1 == 2 and number2 == 1:
        sonuc = round(((int(veri) - 32) * (5/9)),2)
    elif number1 == 1 and number2 == 3:
        sonuc = round((int(veri) + 273.15),2)
    elif number1 == 3 and number2 == 1:
        sonuc = round((int(veri) - 273.15),2)
    elif number1 == 2 and number2 == 3:
        sonuc = round(((int(veri) + 459.67) * (5/9)),2)
    elif number1 == 3 and number2 == 2:
        sonuc = round(((int(veri) * (9/5)) - 459.67),2)
    else:
        print("hi")

    label.configure(text=sonuc)


def Time_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = int(entry.get())
    second_combobox.set(choice2)
    number1 = time_dict[choice1]
    number2 = time_dict[choice2]
    diff = number2 - number1
    if (number1 == 1 or number1 == 2 or number1 == 3 or number1 == 4) and (number2 == 1 or number2 == 2 or number2 == 3 or number2 == 4):
        sonuc = round((veri / (60 ** diff)),2)
    elif number2 == 5:
        if number1 == 1:
            sonuc = round((veri / (3600000*24)),2)
        elif number1 == 2:
            sonuc = round((veri / (3600*24)),2)
        elif number1 == 3:
            sonuc = round((veri /(60*24)),2)
        elif number1 == 4:
            sonuc = round((veri / (24)),2)
        elif number1 == 6:
            sonuc = round((veri * 7),2)
        elif number1 == 7:
            sonuc = round((veri * 30.437),2)
        elif number1 == 8:
            sonuc = round((veri * 365.242),2)
        elif number1 == 5:
            sonuc = veri
    elif number2 == 6:
        if number1 == 1:
            sonuc = round((veri / 604800000),2)
        elif number1 == 2:
            sonuc = round((veri / 604800),2)
        elif number1 == 3:
            sonuc = round((veri / 10080),2)
        elif number1 == 4:
            sonuc = round((veri / 168),2)
        elif number1 == 5:
            sonuc = round((veri / 7),2)
        elif number1 == 7:
            sonuc = round((veri * 4.348),2)
        elif number1 == 8:
            sonuc = round((veri * 52.177),2)
        elif number1 == 6:
            sonuc = veri
    elif number2 == 7:
        if number1 == 1:
            sonuc = round((veri / 2628000000),2)
        elif number1 == 2:
            sonuc = round((veri / 2628000),2)
        elif number1 == 3:
            sonuc = round((veri / 43800),2)
        elif number1 == 4:
            sonuc = round((veri / 730),2)
        elif number1 == 5:
            sonuc = round((veri / 30.416),2)
        elif number1 == 6:
            sonuc = round((veri / 4.345),2)
        elif number1 == 8:
            sonuc = round((veri * 12),2)
        elif number1 == 7:
            sonuc = veri
    elif number2 == 8:
        if number1 == 1:
            sonuc = round((veri / 31536000000),2)
        elif number1 == 2:
            sonuc = round((veri / 31536000),2)
        elif number1 == 3:
            sonuc = round((veri / 525600),2)
        elif number1 == 4:
            sonuc = round((veri / 8760),2)
        elif number1 == 5:
            sonuc = round((veri / 365),2)
        elif number1 == 6:
            sonuc = round((veri / 52.142),2)
        elif number1 == 7:
            sonuc = round((veri / 12),2)
        elif number1 == 8:
            sonuc = veri
    elif number1 == 5:
        if number2 == 1:
            sonuc = round((veri * (3600000*24)),2)
        elif number2 == 2:
            sonuc = round((veri * (3600*24)),2)
        elif number2 == 3:
            sonuc = round((veri *(60*24)),2)
        elif number2 == 4:
            sonuc = round((veri * (24)),2)
        elif number2 == 6:
            sonuc = round((veri / 7),2)
        elif number2 == 7:
            sonuc = round((veri / 30.437),2)
        elif number2 == 8:
            sonuc = round((veri / 365.242),2)
    elif number1 == 6:
        if number2 == 1:
            sonuc = round((veri * 604800000),2)
        elif number2 == 2:
            sonuc = round((veri * 604800),2)
        elif number2 == 3:
            sonuc = round((veri * 10080),2)
        elif number2 == 4:
            sonuc = round((veri * 168),2)
        elif number2 == 5:
            sonuc = round((veri * 7),2)
        elif number2 == 7:
            sonuc = round((veri / 4.348),2)
        elif number2 == 8:
            sonuc = round((veri / 52.177),2)
    elif number1 == 7:
        if number2 == 1:
            sonuc = round((veri * 2628000000),2)
        elif number2 == 2:
            sonuc = round((veri * 2628000),2)
        elif number2 == 3:
            sonuc = round((veri * 43800),2)
        elif number2 == 4:
            sonuc = round((veri * 730),2)
        elif number2 == 5:
            sonuc = round((veri * 30.416),2)
        elif number2 == 6:
            sonuc = round((veri * 4.345),2)
        elif number2 == 8:
            sonuc = round((veri / 12),2)
    elif number1 == 8:
        if number2 == 1:
            sonuc = round((veri * 31536000000),2)
        elif number2 == 2:
            sonuc = round((veri * 31536000),2)
        elif number2 == 3:
            sonuc = round((veri * 525600),2)
        elif number2 == 4:
            sonuc = round((veri * 8760),2)
        elif number2 == 5:
            sonuc = round((veri * 365),2)
        elif number2 == 6:
            sonuc = round((veri * 52.142),2)
        elif number2 == 7:
            sonuc = round((veri * 12),2)

    label.configure(text=sonuc)


def Data_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = data_dict[choice1]
    number2 = data_dict[choice2]
    diff = number1 - number2
    sonuc = int(veri) * (1024**diff)

    label.configure(text=sonuc)


def Speed_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = speed_dict[choice1]
    number2 = speed_dict[choice2]
    if number1 == 1 and number2 == 2:
        sonuc = round((int(veri)* 1 / 60),2)
    elif number1 == 1 and number2 == 3:
        sonuc = round((int(veri)*1 / 3600),2)
    elif number1 == 1 and number2 == 4:
        sonuc = round((int(veri) * 1000 / 1),2)
    elif number1 == 1 and number2 == 5:
        sonuc = round((int(veri) * 1000 / 60),2)
    elif number1 == 1 and number2 == 6:
        sonuc = round((int(veri) * 1000 / 3600),2)
    elif number1 == 2 and number2 == 1:
        sonuc = round((int(veri)*1 / (1/60)),2)
    elif number1 == 2 and number2 == 3:
        sonuc = round((int(veri)*1 / 60),2)
    elif number1 == 2 and number2 == 4:
        sonuc = round((int(veri)*1000 / (1/60)),2)
    elif number1 == 2 and number2 == 5:
        sonuc = round((int(veri)*1000 / 1),2)
    elif number1 == 2 and number2 == 6:
        sonuc = round((int(veri)*1000 / 60),2)
    elif number1 == 3 and number2 == 1:
        sonuc = round((int(veri)*1 / (1/3600)),2)
    elif number1 == 3 and number2 == 2:
        sonuc = round((int(veri)*1 / (1/60)),2)
    elif number1 == 3 and number2 == 4:
        sonuc = round((int(veri)*1000 / (1/3600)),2)
    elif number1 == 3 and number2 == 5:
        sonuc = round((int(veri)*1000 / (1/60)),2)
    elif number1 == 3 and number2 == 6:
        sonuc = round((int(veri)*1000 / 1),2)
    elif number1 == 4 and number2 == 1:
        sonuc = round((int(veri)*(1/1000) / 1),3)
    elif number1 == 4 and number2 == 2:
        sonuc = round((int(veri)*(1/1000) / 60),3)
    elif number1 == 4 and number2 == 3:
        sonuc = round((int(veri)*(1/1000) / 3600),3)
    elif number1 == 4 and number2 == 5:
        sonuc = round((int(veri)*1 / 60),3)
    elif number1 == 4 and number2 == 6:
        sonuc = round((int(veri)*1 / 3600),3)
    elif number1 == 5 and number2 == 1:
        sonuc = round((int(veri)*(1/1000) / (1/60)),3)
    elif number1 == 5 and number2 == 2:
        sonuc = round((int(veri)*(1/1000) / (1)),3)
    elif number1 == 5 and number2 == 3:
        sonuc = round((int(veri)*(1/1000) / 60),3)
    elif number1 == 5 and number2 == 4:
        sonuc = round((int(veri)*1 / (1/60)),3)
    elif number1 == 5 and number2 == 6:
        sonuc = round((int(veri)*1 / 60),3)
    elif number1 == 6 and number2 == 1:
        sonuc = round((int(veri)*(1/1000) / (1/3600)),3)
    elif number1 == 6 and number2 == 2:
        sonuc = round((int(veri)*(1/1000) / (1/60)),3)
    elif number1 == 6 and number2 == 3:
        sonuc = round((int(veri)*(1/1000) / (1)),3)
    elif number1 == 6 and number2 == 4:
        sonuc = round((int(veri)*(1) / (1/3600)),3)
    elif number1 == 6 and number2 == 5:
        sonuc = round((int(veri)*(1) / (1/60)),3)
    elif number1 == number2:
        sonuc = veri
    label.configure(text=sonuc)


def Area_button():
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = area_dict[choice1]
    number2 = area_dict[choice2]
    diff = number1 - number2
    if number1 == number2:
        sonuc = veri
    else:
        sonuc = int(veri) * (100**diff)
        print(diff)

    label.configure(text=sonuc)


def Currency_button():
    link = "https://exchange-rates.abstractapi.com/v1/live"
    choice1 = first_combobox.get()
    choice2 = second_combobox.get()
    veri = entry.get()
    second_combobox.set(choice2)
    number1 = currency_dict[choice1]
    number2 = currency_dict[choice2]
    if number1 == 1 and number2 == 2:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "EUR", "target": "USD"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["USD"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 1 and number2 == 3:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "EUR", "target": "TRY"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["TRY"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 1 and number2 == 4:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "EUR", "target": "GBP"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["GBP"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 2 and number2 == 1:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "USD", "target": "EUR"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["EUR"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 2 and number2 == 3:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "USD", "target": "TRY"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["TRY"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 2 and number2 == 4:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "USD", "target": "GBP"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["GBP"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 3 and number2 == 1:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "TRY", "target": "EUR"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["EUR"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 3 and number2 == 2:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "TRY", "target": "USD"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["USD"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 3 and number2 == 4:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "TRY", "target": "GBP"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["GBP"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 4 and number2 == 1:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "GBP", "target": "EUR"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["EUR"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 4 and number2 == 2:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "GBP", "target": "USD"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["USD"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == 4 and number2 == 3:
        response = requests.get(link, params={"api_key": "9f2df96e1f544cda8f2e732026dec590", "base": "GBP", "target": "TRY"})
        response_json = response.json()
        rate = response_json["exchange_rates"]["TRY"]
        sonuc = round((int(veri) * rate),2)
    elif number1 == number2:
        sonuc =veri

    label.configure(text=sonuc)


def Length():
    global lengths_dict
    lengths_dict = {"km": 1, "hm": 2, "dam": 3, "m": 4, "dm": 5, "cm": 6, "mm": 7}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(lengths_dict.keys()))
    first_combobox.set("km")
    second_combobox.configure(values=list(lengths_dict.keys()))
    second_combobox.set("km")
    convert_button.configure(command = Length_button)


def Weight():
    global weight_dict
    weight_dict = {"kg": 1, "hg": 2, "dag": 3, "g": 4, "dg": 5, "cg": 6, "mg": 7}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(weight_dict.keys()))
    first_combobox.set("kg")
    second_combobox.configure(values=list(weight_dict.keys()))
    second_combobox.set("kg")
    convert_button.configure(command = Weight_button)


def Temperature():
    global temperature_dict
    temperature_dict = {"°C": 1, "°F": 2, "K": 3}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(temperature_dict.keys()))
    first_combobox.set("°C")
    second_combobox.configure(values=list(temperature_dict.keys()))
    second_combobox.set("°C")
    convert_button.configure(command = Temperature_button)


def Time():
    global time_dict
    time_dict = {"ms": 1, "s": 2, "min": 3, "h": 4, "d": 5, "wk": 6, "mo": 7, "yr": 8}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(time_dict.keys()))
    first_combobox.set("s")
    second_combobox.configure(values=list(time_dict.keys()))
    second_combobox.set("s")
    convert_button.configure(command = Time_button)


def Data():
    global data_dict
    data_dict = {"b": 1, "kb": 2, "Mb": 3, "Gb": 4, "Tb": 5}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(data_dict.keys()))
    first_combobox.set("kb")
    second_combobox.configure(values=list(data_dict.keys()))
    second_combobox.set("kb")
    convert_button.configure(command=Data_button)

def Speed():
    global speed_dict
    speed_dict = {"km/h": 1, "km/min": 2, "km/s": 3, "m/h": 4, "m/min": 5, "m/s": 6}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(speed_dict.keys()))
    first_combobox.set("km/h")
    second_combobox.configure(values=list(speed_dict.keys()))
    second_combobox.set("km/h")
    convert_button.configure(command=Speed_button)


def Area():
    global area_dict
    area_dict = {"mm²": 1, "cm²": 2, "m²": 4, "km²": 7}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(area_dict.keys()))
    first_combobox.set("m²")
    second_combobox.configure(values=list(area_dict.keys()))
    second_combobox.set("m²")
    convert_button.configure(command = Area_button)


def Currency():
    global currency_dict
    currency_dict = {"EUR": 1, "USD": 2, "TRY": 3, "GBP": 4}
    first_frame.pack_forget()
    menu()
    first_combobox.configure(values=list(currency_dict.keys()))
    first_combobox.set("EUR")
    second_combobox.configure(values=list(currency_dict.keys()))
    second_combobox.set("EUR")
    convert_button.configure(command = Currency_button)

image_length = Image.open("Images/length.png")
but_length = ctk.CTkImage(image_length)

image_weight = Image.open("Images/weight.png")
but_weight = ctk.CTkImage(image_weight)

image_Temperature = Image.open("Images/thermometer.png")
but_Temperature = ctk.CTkImage(image_Temperature)

image_Time = Image.open("Images/time-left.png")
but_Time = ctk.CTkImage(image_Time)

image_Data = Image.open("Images/data.png")
but_Data = ctk.CTkImage(image_Data)

image_Speed = Image.open("Images/speedometer.png")
but_Speed = ctk.CTkImage(image_Speed)

image_Area = Image.open("Images/area.png")
but_Area = ctk.CTkImage(image_Area)

image_Currency = Image.open("Images/currencies.png")
but_Currency = ctk.CTkImage(image_Currency)

first_frame = ctk.CTkFrame(window, fg_color="transparent")
first_frame.pack(pady=30)

first_row_frame = ctk.CTkFrame(first_frame, fg_color="transparent")
first_row_frame.pack(pady=30)

button_1 = ctk.CTkButton(first_row_frame,width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_length, text="Length", command= Length)
button_1.pack(side=tk.LEFT, padx=10)
button_2 = ctk.CTkButton(first_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_weight, text="Weight", command= Weight)
button_2.pack(side=tk.LEFT, padx=10)

second_row_frame = ctk.CTkFrame(first_frame, fg_color="transparent")
second_row_frame.pack(pady=30)

button_3 = ctk.CTkButton(second_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Temperature, text="Temperature", command= Temperature)
button_3.pack(side=tk.LEFT, padx=10)
button_4 = ctk.CTkButton(second_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Time, text="Time", command= Time)
button_4.pack(side=tk.LEFT, padx=10)

third_row_frame = ctk.CTkFrame(first_frame, fg_color="transparent")
third_row_frame.pack(pady=30)

button_5 = ctk.CTkButton(third_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Data, text="Data", command= Data)
button_5.pack(side=tk.LEFT, padx=10)
button_6 = ctk.CTkButton(third_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Speed, text="Speed", command= Speed)
button_6.pack(side=tk.LEFT, padx=10)

fourth_row_frame = ctk.CTkFrame(first_frame, fg_color="transparent")
fourth_row_frame.pack(pady=30)

button_8 = ctk.CTkButton(fourth_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Area, text="Area", command= Area)
button_8.pack(side=tk.LEFT, padx=10)

button_9 = ctk.CTkButton(fourth_row_frame, width=150, height=40, fg_color="#FF7518", hover_color="#F08000",image=but_Currency, text="Currency", command= Currency)
button_9.pack(side=tk.LEFT, padx=10)


window.mainloop()

