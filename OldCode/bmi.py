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


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
