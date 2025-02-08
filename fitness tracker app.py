import tkinter as tk
from tkinter import messagebox
import datetime

# Fitness Tracker Application
class FitnessTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness Tracker")
        self.root.geometry("400x500")
        
        # Workout Entry
        tk.Label(root, text="Workout Type:").pack()
        self.workout_entry = tk.Entry(root)
        self.workout_entry.pack()
        
        # Duration Entry
        tk.Label(root, text="Duration (minutes):").pack()
        self.duration_entry = tk.Entry(root)
        self.duration_entry.pack()
        
        # Calories Burned Entry
        tk.Label(root, text="Calories Burned:").pack()
        self.calories_entry = tk.Entry(root)
        self.calories_entry.pack()
        
        # Add Workout Button
        self.add_button = tk.Button(root, text="Add Workout", command=self.add_workout)
        self.add_button.pack()
        
        # Display History Button
        self.history_button = tk.Button(root, text="View History", command=self.view_history)
        self.history_button.pack()
        
        # Workout History Display
        self.history_text = tk.Text(root, height=15, width=50)
        self.history_text.pack()
    
    def add_workout(self):
        workout = self.workout_entry.get()
        duration = self.duration_entry.get()
        calories = self.calories_entry.get()
        
        if not workout or not duration or not calories:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return
        
        try:
            duration = int(duration)
            calories = int(calories)
        except ValueError:
            messagebox.showwarning("Input Error", "Duration and Calories must be numbers.")
            return
        
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{date} - {workout}, {duration} min, {calories} kcal\n"
        
        with open("fitness_history.txt", "a") as file:
            file.write(entry)
        
        messagebox.showinfo("Success", "Workout added successfully!")
        self.workout_entry.delete(0, tk.END)
        self.duration_entry.delete(0, tk.END)
        self.calories_entry.delete(0, tk.END)
    
    def view_history(self):
        self.history_text.delete(1.0, tk.END)
        try:
            with open("fitness_history.txt", "r") as file:
                history = file.read()
                self.history_text.insert(tk.END, history)
        except FileNotFoundError:
            self.history_text.insert(tk.END, "No workout history found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessTracker(root)
    root.mainloop()
