import tkinter as tk

from dashboard.dashboard import SecureShieldDashboard


def main():
    root = tk.Tk()

    app = SecureShieldDashboard(root)

    root.mainloop()


if __name__ == "__main__":
    main()