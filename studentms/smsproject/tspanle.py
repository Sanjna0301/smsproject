import tkinter as tk
from tkinter import ttk, messagebox

class TeacherPanelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teacher Panel")
        self.root.geometry("1000x600")

        # Left Menu Frame
        self.menu_frame = tk.Frame(self.root, width=200, bg="#2C3E50")
        self.menu_frame.pack(side="left", fill="y")

        # Right Content Frame
        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Navigation Buttons
        self.buttons = {
            "Dashboard": self.load_dashboard,
            "Student Management": self.load_student_management,
            "Attendance Management": self.load_attendance_management,
            "Task Management": self.load_task_management,
            "Marks Entry": self.load_marks_entry
        }

        for text, command in self.buttons.items():
            tk.Button(
                self.menu_frame, text=text, bg="#34495E", fg="white", 
                font=("Arial", 12), relief="flat", height=2, width=20, 
                command=command
            ).pack(pady=5)

        self.load_dashboard()  # Default screen

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def load_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Dashboard", font=("Arial", 18), bg="white").pack(pady=10)

        # # Example Overview
        # tk.Label(self.content_frame, text="Total Students: 120", font=("Arial", 14), bg="white").pack(pady=5)
        # tk.Label(self.content_frame, text="Recent Activities", font=("Arial", 14), bg="white").pack(pady=10)

        # activities = ["Task 1 assigned", "Attendance updated", "Marks uploaded"]
        # for act in activities:
        tk.Label(self.content_frame, text=f"- {"Task 1 assigned"}", bg="white", anchor="w").pack(fill="x", padx=30)

    def load_student_management(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Student Management", font=("Arial", 18), bg="white").pack(pady=10)

        # Sample Table
        cols = ("s.no", "Name", "Roll.no", "Class")
        tree = ttk.Treeview(self.content_frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        # Dummy Data
        students = [("1", "Aman", "01","BCA"), ("2", "Sita", "02","BCA"), ("3", "Rahul", "03","BCA")]
        for s in students:
            tree.insert("", "end", values=(*s, "Edit/Delete"))

    def load_attendance_management(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Attendance Management", font=("Arial", 18), bg="white").pack(pady=10)

        options = ["Mark Attendance", "Update Attendance", "View Monthly Report"]
        for opt in options:
            tk.Button(self.content_frame, text=opt, font=("Arial", 12), bg="#5DADE2", width=30).pack(pady=5)

    def load_task_management(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Task Management", font=("Arial", 18), bg="white").pack(pady=10)

        tk.Label(self.content_frame, text="Title").pack()
        title_entry = tk.Entry(self.content_frame, width=40)
        title_entry.pack()

        tk.Label(self.content_frame, text="Description").pack()
        desc_entry = tk.Text(self.content_frame, height=5, width=40)
        desc_entry.pack()

        tk.Label(self.content_frame, text="Due Date").pack()
        date_entry = tk.Entry(self.content_frame, width=40)
        date_entry.pack()

        tk.Button(self.content_frame, text="Create Task", bg="#58D68D", width=20).pack(pady=10)

    def load_marks_entry(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Marks Entry", font=("Arial", 18), bg="white").pack(pady=10)

        cols = ("sr.no", "Name", "Task", "Marks", "Actions")
        tree = ttk.Treeview(self.content_frame, columns=cols, show="headings")
        for col in cols:
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        # Dummy Data
        marks = [("1", "Aman", "Math HW", "85"), ("2", "Sita", "python project", "90")]
        for m in marks:
            tree.insert("", "end", values=(*m, "Edit/Delete"))

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = TeacherPanelApp(root)
    root.mainloop()
