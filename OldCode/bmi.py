import customtkinter as ctk
from typing import Optional, Union, Tuple


class App(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ) -> None:
        super().__init__(fg_color, **kwargs)

        self.title("BMI Calculator")
        self.geometry("300x400")
        self.resizable(False, False)

        self.label = ctk.CTkLabel(
            master=self, text="Calculate BMI", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.label.pack()

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack(fill="both", padx=10, pady=(20, 20))

        self.forms_frame = ctk.CTkFrame(master=self.frame)
        self.forms_frame.pack(fill="both", padx=10, pady=(10, 5))

        self.weight_label = ctk.CTkLabel(
            master=self.forms_frame,
            text="Weight",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.weight_label.grid(row=0, column=0, padx=20, pady=(10, 5))

        self.weight_entry = ctk.CTkEntry(
            master=self.forms_frame, placeholder_text="weight (kg)"
        )
        self.weight_entry.grid(row=0, column=1, columnspan=1, pady=(10, 5))

        self.height_label = ctk.CTkLabel(
            master=self.forms_frame,
            text="Height",
            font=ctk.CTkFont(size=16, weight="bold"),
        )
        self.height_label.grid(row=1, column=0, padx=20, pady=(10, 5))

        self.height_entry = ctk.CTkEntry(
            master=self.forms_frame, placeholder_text="height (cm)"
        )
        self.height_entry.grid(row=1, column=1, columnspan=1, pady=(10, 5))

        self.results_frame = ctk.CTkFrame(master=self.frame)
        self.results_frame.pack(fill="both", padx=10, pady=(5, 10))

        self.calculate_button = ctk.CTkButton(
            master=self.results_frame, text="Calcluate", command=self.print_result
        )
        self.calculate_button.pack()

        self.output = ctk.CTkTextbox(master=self.results_frame)
        self.output.pack(pady=(10, 10))

    def calculate_bmi(self, height: float, weight: float) -> float:
        return round(weight / (height * height) * (10000), 1)

    def print_result(self) -> None:
        try:
            height = float(self.height_entry.get())
        except TypeError:
            print("Input must be of type float")
        try:
            weight = float(self.weight_entry.get())
        except TypeError:
            ("Input must be of type float")

        self.bmi = self.calculate_bmi(height=height, weight=weight)

        self.output.delete(0.0, "end")
        self.output.insert(0.0, self.bmi)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
