import customtkinter as ctk


def main() -> None:
    root = ctk.CTk()
    root.title("Custom TkInter")
    root.geometry("250x250")
    root.resizable(False, False)

    label = ctk.CTkLabel(
        master=root, text="Hello, CTkInter", font=ctk.CTkFont(size=20, weight="bold")
    )
    label.pack()

    button = ctk.CTkButton(master=root, text="Click Me")
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
