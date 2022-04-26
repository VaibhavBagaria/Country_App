from tkinter import*
import json
import requests
from tkinter import messagebox as msgbox

root=Tk()
root.title("Country App")
root.geometry('400x550')
root.configure(bg="aqua")

capital_name_label=Label(root, text="Capital Name",font=("Helvetica", 18,'bold'),bg="aqua",fg="blue")
capital_name_label.place(relx=0.5,rely=0.05,anchor=CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.5,rely=0.1,anchor=CENTER)

country_info = Label(root,text="Country:",bg="aqua",fg="blue",font=("bold", 14))
country_info.place(relx=0.3,rely=0.35,anchor=CENTER)

region_info = Label(root,text="Region:",bg="aqua",fg="blue",font=("bold",14))
region_info.place(relx=0.3,rely=0.45,anchor=CENTER)

language_info = Label(root,text="Language:",bg="aqua",fg="blue",font=("bold", 14))
language_info.place(relx=0.3,rely=0.55,anchor=CENTER)

population_info = Label(root,text="Population:",bg="aqua",fg="blue",font=("bold",14))
population_info.place(relx=0.3,rely=0.65,anchor=CENTER)

area_info = Label(root,text="Area:",bg="aqua",fg="blue",font=("bold", 14))
area_info.place(relx=0.3,rely=0.75,anchor=CENTER)

def city_details():
    api_request=requests.get("https://restcountries.com/v2/capital/"+city_entry.get())
    api_output_json=json.loads(api_request.content)
    try:
        country=api_output_json[0]["name"]
        print(country)
        region=api_output_json[0]["region"]
        print(region)
        language=api_output_json[0]["demonym"]
        print(language)
        population=api_output_json[0]["population"]
        print(population)
        area=api_output_json[0]["area"]
        print(area)
        
    except(KeyError):
        msgbox.showinfo("Error","Give Valid Captal Name")
    
    country_info['text']="Country: "+country
    region_info['text']="Region: "+region
    language_info['text']="Language: "+language
    population_info['text']="Population: "+str(population)
    area_info['text']="Area: "+str(area)

search_btn=Button(root, text="Search Capital", command=city_details, relief=FLAT)
search_btn.place(relx=0.5,rely=0.2,anchor=CENTER)
root.mainloop()
