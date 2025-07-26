from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

# Connect to MySQL using XAMPP
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="userdb"
    )

# Register user
def register_user():
    name = entry_name.get()
    email = entry_email.get()
    password = entry_pass.get()

    if name == "" or email == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    try:
        con = connect_db()
        cursor = con.cursor()
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                       (name, email, password))
        con.commit()
        con.close()
        messagebox.showinfo("Success", "Registered Successfully")
        switch_to_login()
    except mysql.connector.IntegrityError:
        messagebox.showerror("Error", "Email already exists")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

# Login user
def login_user():
    email = login_email.get()
    password = login_pass.get()

    if email == "" or password == "":
        messagebox.showerror("Error", "All fields are required")
        return

    con = connect_db()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", 
                   (email, password))
    row = cursor.fetchone()
    con.close()

    if row:
        messagebox.showinfo("Success", f"Welcome {row[1]}!")
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Switch to register frame
def switch_to_register():
    login_frame.place_forget()
    register_frame.place(x=100, y=100)

# Switch to login frame
def switch_to_login():
    register_frame.place_forget()
    login_frame.place(x=100, y=100)

# Tkinter root window
root = Tk()
root.title("Login & Register")
root.geometry("900x600")


# # Background image
# bg_img = Image.open("pic.jpg")
# bg_img = bg_img.resize((1500, 1100))
# bg_photo = ImageTk.PhotoImage(bg_img)

# bg_label = Label(root, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Login Frame
login_frame = Frame(root, bg="#9775ab", bd=2)
login_frame.place(x=100, y=100, width=350, height=400)



Label(login_frame, text="Login", font=("Arial", 20), bg="#9775ab").pack(pady=20)
Label(login_frame, text="Email", font=("Arial", 12), bg="#9775ab").pack(pady=5)
login_email = Entry(login_frame, font=("Arial", 12))
login_email.pack(pady=5)

Label(login_frame, text="Password", font=("Arial", 12), bg="#9775ab").pack(pady=5)
login_pass = Entry(login_frame, show="*", font=("Arial", 12))
login_pass.pack(pady=5)

Button(login_frame, text="Login", command=login_user, bg="#F9F9F9", fg="black", font=("Arial", 12)).pack(pady=20)
Button(login_frame, text="Go to Register", command=switch_to_register, bg="#F9F9F9", fg="black", font=("Arial", 10)).pack()

# Register Frame
register_frame = Frame(root, bg="#9775ab", bd=3)
# register_frame.place(x=100, y=100, width=1000, height=500)
register_frame.place_forget()

Label(register_frame, text="Register", font=("Arial", 20), bg="#9775ab").pack(pady=20)
Label(register_frame, text="Name", font=("Arial", 12), bg="#9775ab").pack(pady=5)
entry_name = Entry(register_frame, font=("Arial", 12))
entry_name.pack(pady=5)

Label(register_frame, text="Email", font=("Arial", 12), bg="#9775ab").pack(pady=5)
entry_email = Entry(register_frame, font=("Arial", 12))
entry_email.pack(pady=5)

Label(register_frame, text="Password", font=("Arial", 12), bg="#9775ab").pack(pady=5)
entry_pass = Entry(register_frame, show="*", font=("Arial", 12))
entry_pass.pack(pady=5)

Button(register_frame, text="Submit", command=register_user, bg="#F5F9F5", fg="black", font=("Arial", 12)).pack(pady=20)
Button(register_frame, text="Login", command=switch_to_login, bg="#F5F9F5", fg="black", font=("Arial", 10)).pack()

root.mainloop()


