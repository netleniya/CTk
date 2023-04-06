import customtkinter as ctk


def calculate_bmi(height: float, weight: float) -> float:
    return round(weight / (height * height) * (10000), 1)


def main() -> None:
    app = ctk.CTk()
    app.title("BMI Calculator")
    app.geometry("300x400")
    app.resizable(False, False)

    label = ctk.CTkLabel(
        master=app, text="Calculate your BMI", font=ctk.CTkFont(size=20, weight="bold")
    )
    label.pack()

    frame = ctk.CTkFrame(master=app)
    frame.pack(fill="x", padx=10, pady=10)

    forms_frame = ctk.CTkFrame(master=frame)
    forms_frame.pack(fill="both")

    weight_label = ctk.CTkLabel(
        master=forms_frame, text="Weight", font=ctk.CTkFont(size=16, weight="bold")
    )
    weight_label.pack(pady=(10, 5))
    weight_entry = ctk.CTkEntry(master=forms_frame, placeholder_text="weight (kg)")
    weight_entry.pack(pady=(5, 10))

    height_label = ctk.CTkLabel(
        master=forms_frame, text="Height", font=ctk.CTkFont(size=16, weight="bold")
    )
    height_label.pack(pady=(10, 5))
    height_entry = ctk.CTkEntry(master=forms_frame, placeholder_text="height (cm)")
    height_entry.pack(pady=(5, 10))

    button_frame = ctk.CTkFrame(master=frame)
    button_frame.pack(fill="x", pady=(10, 5))

    calculate_button = ctk.CTkButton(
        master=button_frame, text="Calculate BMI", command=calculate_bmi
    )
    calculate_button.pack()

    results = ctk.CTkTextbox(master=button_frame)
    results.pack(pady=(20, 20))

    app.mainloop()


if __name__ == "__main__":
    main()
