import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil

# Simulated in-memory data
student = {
    "name": "sana",
    "course": "Btech CSE",
    "batch": "2024",
    "profile_img": "pic.jpg",
}

attendance_records = [
    {"date": "2025-07-01", "subject": "DSA", "status": "Present"},
    {"date": "2025-07-02", "subject": "OS", "status": "Absent"},
]

assigned_tasks = [
    {"title": "DSA Assignment", "description": "Solve Chapter 5", "deadline": "2025-07-25", "submitted": "Yes"},
    {"title": "OS Project", "description": "Prepare model", "deadline": "2025-07-28", "submitted": "No"},
]

marks_data = [
    {"task": "DSA Assignment", "marks": 9},
    {"task": "OS Project", "marks": 7},
]

class StudentPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Panel (No Database)")
        self.root.geometry("1000x600")

        self.menu_frame = tk.Frame(self.root, width=200, bg="#2C3E50")
        self.menu_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.root, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.sections = {
            "Dashboard": self.load_dashboard,
            "Attendance": self.load_attendance,
            "Assigned Tasks": self.load_tasks,
            "Marks/Performance": self.load_marks,
            "Profile": self.load_profile
        }

        for name, cmd in self.sections.items():
            tk.Button(self.menu_frame, text=name, width=20, height=2, command=cmd, bg="#34495E", fg="white", font=("Arial", 12)).pack(pady=5)

        self.load_dashboard()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def load_dashboard(self):
        self.clear_content()
        tk.Label(self.content_frame, text=f"Welcome, {student['name']}!", font=("Arial", 22), bg="white").pack(pady=10)

        img_file = student["profile_img"] if os.path.exists(student["profile_img"]) else "pic.jpg"
        image = Image.open(img_file).resize((150, 150))
        photo = ImageTk.PhotoImage(image)

        img_label = tk.Label(self.content_frame, image=photo, bg="white")
        img_label.image = photo
        img_label.pack(pady=10)

        tk.Label(self.content_frame, text=f"course: {student['course']}", bg="white", font=("Arial", 14)).pack()
        tk.Label(self.content_frame, text=f"Batch: {student['batch']}", bg="white", font=("Arial", 14)).pack()

    def load_attendance(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Attendance Records", font=("Arial", 18), bg="white").pack(pady=10)

        tree = ttk.Treeview(self.content_frame, columns=("Date", "Subject", "Status"), show="headings")
        for col in ("Date", "Subject", "Status"):
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        for record in attendance_records:
            tree.insert("", "end", values=(record["date"], record["subject"], record["status"]))

    def load_tasks(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Assigned Tasks", font=("Arial", 18), bg="white").pack(pady=10)

        tree = ttk.Treeview(self.content_frame, columns=("Title", "Description", "Deadline", "Submitted"), show="headings")
        for col in ("Title", "Description", "Deadline", "Submitted"):
            tree.heading(col, text=col)
        tree.pack(fill="both", expand=True)

        for task in assigned_tasks:
            tree.insert("", "end", values=(task["title"], task["description"], task["deadline"], task["submitted"]))

    def load_marks(self):
        self.clear_content()
        tk.Label(self.content_frame, text="Marks & Performance", font=("Arial", 18), bg="white").pack(pady=10)

        tree = ttk.Treeview(self.content_frame, columns=("Task", "Marks"), show="headings")
        tree.heading("Task", text="Task Title")
        tree.heading("Marks", text="Marks Obtained")
        tree.pack(fill="both", expand=True)

        for mark in marks_data:
            tree.insert("", "end", values=(mark["task"], mark["marks"]))

    def load_profile(self):
        self.clear_content()
        tk.Label(self.content_frame, text="My Profile", font=("Arial", 18), bg="white").pack(pady=10)

        # Form
        tk.Label(self.content_frame, text="Name").pack()
        name_entry = tk.Entry(self.content_frame)
        name_entry.insert(0, student["name"])
        name_entry.pack()

        tk.Label(self.content_frame, text="course").pack()
        section_entry = tk.Entry(self.content_frame)
        section_entry.insert(0, student["course"])
        section_entry.pack()

        tk.Label(self.content_frame, text="Batch").pack()
        batch_entry = tk.Entry(self.content_frame)
        batch_entry.insert(0, student["batch"])
        batch_entry.pack()

        def upload_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg")])
            if file_path:
                os.makedirs("profile_images", exist_ok=True)
                save_path = f"profile_images/profile_{student['id']}.png"
                shutil.copy(file_path, save_path)
                student["profile_img"] = save_path
                messagebox.showinfo("Success", "Profile image updated!")

        def save_profile():
            student["name"] = name_entry.get()
            student["course"] = section_entry.get()
            student["batch"] = batch_entry.get()
            messagebox.showinfo("Saved", "Profile updated successfully.")
            self.load_dashboard()

        tk.Button(self.content_frame, text="Upload Profile Image", command=upload_image).pack(pady=5)
        tk.Button(self.content_frame, text="Save Changes", command=save_profile, bg="#58D68D").pack(pady=10)

# === MAIN ===
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentPanel(root)
    root.mainloop()
