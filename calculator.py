#!/usr/bin/env python3

import os
import tkinter as tk
from tkinter import messagebox

PRIMARY_BG = "#2c0f3d"
SECONDARY_BG = "#4f2a74"
BUTTON_BG = "#7d4fa0"
BUTTON_ACTIVE = "#a571cf"
OP_BG = "#5d2d89"
DISPLAY_BG = "#ecd4ff"

TEXT_COLOR = "#ffffff"
DISPLAY_TEXT = "#2b003d"


def safe_eval_expression(expression):
    expression = expression.strip()
    if not expression:
        raise ValueError("Expresión vacía.")
    allowed = set("0123456789.+-*/")
    if not all(char in allowed for char in expression):
        raise ValueError("Expresión inválida. Usa solo números y operadores + - * /")
    try:
        return eval(expression, {"__builtins__": None}, {})
    except ZeroDivisionError:
        raise
    except Exception:
        raise ValueError("Expresión inválida. Usa solo números y operadores + - * /")


def console_mode():
    print("No se encontró una pantalla disponible. Modo consola activado.")
    print("Escribe 'salir' o 'q' para terminar.")
    while True:
        expr = input("Expresión: ").strip()
        if expr.lower() in ("salir", "q"):
            break
        try:
            result = safe_eval_expression(expr)
            print(f"Resultado: {result}")
        except ZeroDivisionError:
            print("Error: no se puede dividir entre cero.")
        except ValueError as err:
            print(err)


class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Morada")
        self.configure(bg=PRIMARY_BG)
        self.resizable(False, False)
        self.expression = ""
        self._build_ui()

    def _build_ui(self):
        self.display_var = tk.StringVar(value="0")

        display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=("Segoe UI", 24, "bold"),
            bd=0,
            bg=DISPLAY_BG,
            fg=DISPLAY_TEXT,
            justify="right",
            state="readonly",
            readonlybackground=DISPLAY_BG,
        )
        display.grid(row=0, column=0, columnspan=4, padx=12, pady=(12, 8), sticky="we")

        button_style = {
            "font": ("Segoe UI", 16, "bold"),
            "bd": 0,
            "fg": TEXT_COLOR,
            "bg": BUTTON_BG,
            "activebackground": BUTTON_ACTIVE,
            "activeforeground": TEXT_COLOR,
            "width": 4,
            "height": 2,
        }

        digits = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
            ("0", 4, 0), (".", 4, 1),
        ]

        operations = [
            ("/", 1, 3),
            ("*", 2, 3),
            ("-", 3, 3),
            ("+", 4, 3),
        ]

        for text, row, col in digits:
            button = tk.Button(
                self,
                text=text,
                command=lambda value=text: self._add_to_expression(value),
                **button_style,
            )
            button.grid(row=row, column=col, padx=6, pady=6)

        for text, row, col in operations:
            button = tk.Button(
                self,
                text=text,
                command=lambda value=text: self._add_to_expression(value),
                font=("Segoe UI", 16, "bold"),
                bd=0,
                fg=TEXT_COLOR,
                bg=OP_BG,
                activebackground=BUTTON_ACTIVE,
                activeforeground=TEXT_COLOR,
                width=4,
                height=2,
            )
            button.grid(row=row, column=col, padx=6, pady=6)

        clear_button = tk.Button(
            self,
            text="C",
            command=self._clear_expression,
            font=("Segoe UI", 16, "bold"),
            bd=0,
            fg=TEXT_COLOR,
            bg="#da4fff",
            activebackground="#f6b1ff",
            activeforeground=TEXT_COLOR,
            width=4,
            height=2,
        )
        clear_button.grid(row=4, column=2, padx=6, pady=6)

        equal_button = tk.Button(
            self,
            text="=",
            command=self._evaluate_expression,
            font=("Segoe UI", 16, "bold"),
            bd=0,
            fg=TEXT_COLOR,
            bg="#5f0b8d",
            activebackground="#9157bf",
            activeforeground=TEXT_COLOR,
            width=4,
            height=2,
        )
        equal_button.grid(row=5, column=0, columnspan=4, padx=6, pady=(0, 12), sticky="we")

    def _add_to_expression(self, value):
        if self.expression == "0" and value != ".":
            self.expression = value
        else:
            self.expression += value
        self.display_var.set(self.expression)

    def _clear_expression(self):
        self.expression = ""
        self.display_var.set("0")

    def _evaluate_expression(self):
        if not self.expression:
            return
        try:
            result = safe_eval_expression(self.expression)
            self.expression = str(result)
            self.display_var.set(self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir entre cero.")
            self._clear_expression()
        except ValueError as err:
            messagebox.showerror("Error", str(err))
            self._clear_expression()

    @staticmethod
    def _valid_expression(expr):
        allowed = set("0123456789.+-*/")
        return all(char in allowed for char in expr)


def main():
    if not os.environ.get("DISPLAY"):
        console_mode()
        return

    try:
        app = CalculatorApp()
        app.mainloop()
    except tk.TclError as err:
        print("No se puede iniciar la interfaz gráfica. Ejecutando modo consola en su lugar.")
        print(f"Detalles: {err}")
        console_mode()


if __name__ == "__main__":
    main()
