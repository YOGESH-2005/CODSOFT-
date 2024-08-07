import tkinter as tk
from tkinter import messagebox, simpledialog
import json

class todolist:
    def __init__(self,root):
        self.root =root
        self.root.title("To Do List  By Naga Vamsi R")
        self.tasks = self.load_tasks()
        

        self.task_listbox=tk.Listbox(self.root,width=50,height=10,selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        self.add_button = tk.Button(self.root,text= "Add Task",command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root,text= "Remove Task",command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        self.update_button = tk.Button(self.root,text= "Update Task",command=self.update_task)
        self.update_button.pack(pady=5)
        
        self.sort_button = tk.Button(self.root,text= "Sort Task",command=self.sort_tasks)
        self.sort_button.pack(pady=5)


        self.refresh_tasks()
        
    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as f:
                tasks = json.load(f)
        except FileNotFoundError:
            tasks = []
        return tasks
    
    def save_tasks(self):
        with open('tasks.json', 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            self.tasks.append(task_name)
            self.save_tasks()
            self.refresh_tasks()
            
    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            del self.tasks[task_index]
            self.save_tasks()
            self.refresh_tasks()
            
    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task_index = selected_index[0]
            new_task_name = simpledialog.askstring("Update Task", "Enter new task name:", initialvalue=self.tasks[task_index])
            if new_task_name:
                self.tasks[task_index] = new_task_name
                self.save_tasks()
                self.refresh_tasks()
                
    def refresh_tasks(self):
             self.task_listbox.delete(0, tk.END)
             for task in self.tasks:
                 self.task_listbox.insert(tk.END, task)
    def sort_tasks(self):
        self.tasks.sort()
        self.save_tasks()
        self.refresh_tasks()   
                
if __name__ == "__main__":
    root = tk.Tk()
    todo_app = todolist(root)
root.mainloop()

