import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Patient Records App")
        master.attributes('-fullscreen', True)

        # --- Video Player Setup ---
        self.video_label = tk.Label(master)
        self.video_label.pack(fill="both", expand=True)
        self.video_path = "./software_data/intro.mp4"
        self.play_video()

        # --- Background Image (Load here, but don't place yet) ---
        try:
            self.bg_image = ImageTk.PhotoImage(Image.open('./software_data/images.jpeg')) 
        except FileNotFoundError:
            print("Background image not found. Using default background.")
            self.bg_image = None  # Set to None if image not found

        # --- Login Widgets (Frame to hold them) ---
        self.login_frame = tk.Frame(master)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Helvetica", 12))
        self.password_label.pack()

        self.password_entry = ttk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=10)

        self.login_button = ttk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.pack()

        self.login_type = None
        self.entered_password = None

    def play_video(self):
        """Plays the video and schedules the login screen to appear."""
        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            print("Error opening video file.")
            self.show_login()  # Show login if video fails
            return

        self.update_video_frame()

    def update_video_frame(self):
        """Updates the video frame and checks for completion."""
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.video_label.config(image=img)
            self.video_label.image = img
            self.master.after(30, self.update_video_frame)  # Update every 30ms
        else:
            self.cap.release()
            self.show_login()

    def show_login(self):
        """Hides the video player and shows the login widgets and background."""
        self.video_label.pack_forget()

        # --- Place background image ---
        if self.bg_image:
            self.bg_label = tk.Label(self.master, image=self.bg_image)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # --- Show login frame ---
        self.login_frame.pack()

    def fade_out_widgets(self):
        """Fades out the login widgets."""
        alpha = self.login_frame.winfo_ismapped() / 10  # Get initial alpha (1.0 if visible)
        if alpha > 0:
            alpha -= 0.1
            self.login_frame.wm_attributes('-alpha', alpha)
            self.master.after(50, self.fade_out_widgets)  # Recursive call every 50ms
        else:
            self.login_frame.pack_forget()  # Hide completely after fading
            self.play_success_video()

    def play_success_video(self):
        """Plays the success video and then calls show_patient_list."""
        self.success_video_label = tk.Label(self.master)
        self.success_video_label.pack(fill="both", expand=True)
        self.success_video_path = "./software_data/success.mp4"  # Replace with your video
        self.success_cap = cv2.VideoCapture(self.success_video_path)

        if not self.success_cap.isOpened():
            print("Error opening success video file.")
            self.show_patient_list()  # Go to patient list if video fails
            return

        self.update_success_video_frame()

    def update_success_video_frame(self):
        """Updates the success video frame."""
        ret, frame = self.success_cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.success_video_label.config(image=img)
            self.success_video_label.image = img
            self.master.after(30, self.update_success_video_frame)
        else:
            self.success_cap.release()
            self.success_video_label.pack_forget()
            self.show_patient_list()

    def show_patient_list(self):
        """Transition to the patient list (replace with your actual logic)."""
        print("Transitioning to patient list...")
        self.master.destroy()  # Close the login window
        # Add your code here to open the patient list window

    def login(self):
        self.entered_password = self.password_entry.get()
        if  # (Password is correct)
            self.fade_out_widgets()
        else:

    def show_login_window(self):
        self.master.mainloop()
        return self.login_type, self.entered_password

