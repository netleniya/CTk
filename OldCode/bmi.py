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

    app.mainloop()


if __name__ == "__main__":
    main()
