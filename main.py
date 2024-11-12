import hashlib  # For password hashing (you can use bcrypt or Argon2 instead)
from gui import login_window, patient_list
import tkinter as tk

# (Import other GUI modules as you create them)

def main():
    """Main application entry point."""

    # --- Configuration (You can move this to a separate config file) ---
    ADMIN_PASSWORD_HASH = "your_hashed_admin_password"  # Hash the password securely!
    DOCTOR_PASSWORD_HASH = "your_hashed_doctor_password"  # Hash the password securely!

    # --- Login Handling ---
    login_successful = False
    while not login_successful:
        root = tk.Tk()  # Create the root Tkinter window
        login_window_instance = login_window.LoginWindow(root)  # Pass root as master
        login_type, entered_password = login_window_instance.show_login_window()
        root.destroy()

        if login_type == "admin":
            if hashlib.sha256(entered_password.encode()).hexdigest() == ADMIN_PASSWORD_HASH:
                login_successful = True
                user_type = "admin"
            else:
                login_window.show_error_message("Incorrect password!")
        elif login_type == "doctor":
            if hashlib.sha256(entered_password.encode()).hexdigest() == DOCTOR_PASSWORD_HASH:
                login_successful = True
                user_type = "doctor"
            else:
                login_window.show_error_message("Incorrect password!")
        else:
            # Handle case where login window is closed
            return

    # --- Main Application Loop ---
    if login_successful:
        # Open the patient list window after successful login
        patient_list.show_patient_list_window(user_type)

if __name__ == "__main__":
    main()