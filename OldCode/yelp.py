import customtkinter as ctk
from typing import Optional, Tuple, Union


class App(ctk.CTk):
    def __init__(
        self, fg_color: Optional[Union[str, Tuple[str, str]]] = None, **kwargs
    ) -> None:
        super().__init__(fg_color, **kwargs)

        self.title("Yelp Business Search")
        self.geometry("750x550")
        self.resizable(True, True)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
