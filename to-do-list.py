from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))    
        list_update()    
        task_field.delete(0, 'end')  
    
def list_update():    
    clear_list()    
    for task in tasks:    
        task_listbox.insert('end', task)  
  
def delete_task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            list_update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def delete_all_tasks():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('delete from tasks')   
        list_update()  
   
def clear_list():   
    task_listbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
   
if __name__ == "__main__":    
    guiWindow = Tk()   
    guiWindow.title(" To-Do List ")  
    guiWindow.geometry("665x400")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  


    
    tasks = []  
        
    functions_frame = Frame(guiWindow, bg = "#b5a294") 
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    task_label = Label( functions_frame,text = "TO-DO LIST \n  \n Enter the Task Title : ",  
        font = ("arial", "14", "bold"),  
        background = "#b5a294", 
        foreground="#262626"
    )    
    #to do list (in writing)
    task_label.place(x = 1, y = 30)  
        
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 30,  
        foreground="black",
        background = "#fcf4ec",  
    )    
    #to do list bar
    task_field.place(x = 270, y = 75)  
    
    add_button =Button(  
        functions_frame,  
        text = "Add",  
        width = 15,
        bg='#d7a377',font=("arial", "14", "bold"),
        command = add_task,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Remove Task",  
        width = 15,
        bg='#d7a377', font=("arial", "14", "bold"),
        command = delete_task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text = "Erase all Task",  
        width = 15,
        font=("arial", "14", "bold"),
        bg='#d7a377',
        command = delete_all_tasks  
    )
    
    exit_button = Button(  
        functions_frame,  
        text = "Close",  
        width = 15,
        bg='#d7a377',  font=("arial", "14", "bold"),
        command = close  
    )    
    add_button.place(x = 18, y = 130,)  
    del_button.place(x = 18, y = 190)  
    del_all_button.place(x = 18, y = 250)  
    exit_button.place(x = 18, y = 342)  

    img=PhotoImage(file="notee.png")
    guiWindow.iconphoto(False,img)

    
    task_listbox = Listbox(  
        functions_frame,  
        width = 37,  
        height = 12,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "#fcf4ec",
        foreground="BLACK",    
        selectbackground = "#d7a377",  
        selectforeground="white"
    )    
    task_listbox.place(x = 270, y = 132)  
    
    retrieve_database()  
    list_update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()