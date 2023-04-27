from tkinter import *
from tkinter.filedialog import *
from main import *

root = Tk()

root.geometry("700x700")

project_name = StringVar()
project_category = StringVar()
project_image = StringVar()
project_description = StringVar()
pledge_goal = IntVar()
pledge_duration = IntVar()

category_list = ['art', 'comics', 'crafts', 'dance']
pledge_goal.set(1)
pledge_duration.set(1)

def upload_image_click():
    """image_file = askopenfile()
    print(image_file.name)
    imagea = PhotoImage(file=image_file.name)
    Label(root, image=imagea).grid(row=9, column=0)"""
    pass

def save_button_click():
    """project_name, category, project_image, project_duration, project_detail, project_creator"""
    """
    {
    "project_name": "project101",
    "category": "art",
    "project_image": "image",
    "project_duration": "09-09-2029",
    "project_detail": "do not touch my hair!",
    "creator_id": 3
    }
    """
    payload_project = {
        "project_name": project_name.get(),
        "category": project_category.get(),
        "project_image": "image",
        "project_duration": pledge_duration.get(),
        "project_detail": "do not touch my hair!",
        "creator_id": 3 
    }
    response = requests.post()
    """print(description_text.__getattribute__)
    description_text.insert(END, "hoy")"""

Label(root, text='Project title').grid(row=0, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=project_name, width=12, justify='left').grid(row=0, column=1, padx=10)
Label(root, text='Project category').grid(row=1, column=0, padx=10, ipady=5, sticky='E')
category_menu = OptionMenu(root, project_category, *category_list)
category_menu.grid(row=1, column=1)
category_menu.config(width=15)
Label(root, text='Project Image').grid(row=2, column=0, padx=10, ipady=5, sticky='E')
Button(root, text='Upload file', command=upload_image_click).grid(row=2, column=1, padx=10)
Label(root, text='Project description').grid(row=3, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=project_description, width=60, justify='left').grid(row=3, column=1, padx=10)
Label(root, text='fundding goal').grid(row=4, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=pledge_goal, width=12, justify='left').grid(row=4, column=1, padx=10)
Label(root, text='Campaign duration').grid(row=5, column=0, padx=10, ipady=5, sticky='E')
Entry(root, textvariable=pledge_duration, width=12, justify='left').grid(row=5, column=1, padx=10)

Button(root, text='Save', command=save_button_click).grid(row=6, column=1)

root.mainloop()