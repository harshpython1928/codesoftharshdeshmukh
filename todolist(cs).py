
#To do list python program
#Importing all functions from the tkinter   
from tkinter import *
from tkinter import messagebox

#Factions that we need
tasks_list = []
counter = 1
def inputError() :
     
    if enterTaskField.get() == "" :
         
        messagebox.showerror("Input Error")
         
        return 0
     
    return 1    
def clear_taskNumberField() :
     
    taskNumberField.delete(0.0, END) 
def clear_taskField() :
 
    enterTaskField.delete(0, END)
def insertTask():
 
    global counter
    value = inputError()
    if value == 0 :
        return
 
    content = enterTaskField.get() + "\n"
    tasks_list.append(content)
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
 
    counter += 1
    clear_taskField()

def delete() :
     
    global counter
 
    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
 
    #Get the task number, which is required to delete
    number = taskNumberField.get(1.0, END)
 
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 
    clear_taskNumberField()
    
    tasks_list.pop(task_no - 1)
    counter -= 1
    TextArea.delete(1.0, END)
 
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
 
#Driver code 
if __name__ == "__main__" :
 
    #Create a GUI window
    gui = Tk()
    gui.configure(background = "light gray")
    gui.title("TO DO LIST")
    gui.geometry("300x400")
    enterTask = Label(gui, text = "Create New Task", bg = "sky blue")
    enterTaskField = Entry(gui, bg = "light green")
    Submit = Button(gui, text = "Add", fg = "black", bg = "green", command = insertTask)
    TextArea = Text(gui, height = 7, width = 27, font = "Arial", bg = "light green")
    taskNumber = Label(gui, text = "Delete Task Number", bg = "sky blue")                  
    taskNumberField = Text(gui, height = 1, width = 2, font = "Arial", bg ="light green")
 
    delete = Button(gui, text = "Delete", fg = "Black", bg = "Red", command = delete)
    Exit = Button(gui, text = "Exit", fg = "white", bg = "gray", command = exit)
 
    #Grid method
    enterTask.grid(row = 0, column = 2)
    #ipadx attributed set the entry box horizontal size               
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
    Submit.grid(row = 2, column = 2)
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)                    
    taskNumber.grid(row = 4, column = 2, pady = 5)
    taskNumberField.grid(row = 5, column = 2)                
    delete.grid(row = 7, column = 2, pady = 7)                 
    Exit.grid(row = 8, column = 2)
 
    #Start the GUI 
    gui.mainloop()