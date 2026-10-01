import tkinter as tk
import math


# =========================
# Window
# =========================

window = tk.Tk()
window.title(" Calculator")
window.geometry("360x600")
window.resizable(False, False)
window.configure(bg="black")


# =========================
# Calculator variables
# =========================

current_value = "0"
first_number = None
operator = None
new_number = True


# =========================
# Display
# =========================

display = tk.Label(
    window,
    text="0",
    font=("Arial", 45),
    bg="black",
    fg="white",
    anchor="e",
    padx=20
)

display.pack(
    fill="both",
    expand=True
)


# =========================
# Calculator functions
# =========================

def update_display():
    display.config(text=current_value)


def number_clicked(number):
    global current_value, new_number

    if new_number or current_value == "0":
        current_value = number
        new_number = False
    else:
        current_value += number

    update_display()


def decimal_clicked():
    global current_value, new_number

    if new_number:
        current_value = "0."
        new_number = False

    elif "." not in current_value:
        current_value += "."

    update_display()


def clear_clicked():
    global current_value, first_number, operator, new_number

    current_value = "0"
    first_number = None
    operator = None
    new_number = True

    update_display()


def sign_clicked():
    global current_value

    if current_value != "0":

        if current_value.startswith("-"):
            current_value = current_value[1:]
        else:
            current_value = "-" + current_value

    update_display()


def percent_clicked():
    global current_value

    try:
        number = float(current_value)
        result = number / 100

        if result.is_integer():
            current_value = str(int(result))
        else:
            current_value = str(result)

    except ValueError:
        current_value = "0"

    update_display()


def operator_clicked(selected_operator):
    global first_number, operator, new_number

    try:
        first_number = float(current_value)
        operator = selected_operator
        new_number = True

    except ValueError:
        clear_clicked()


def equal_clicked():
    global current_value, first_number, operator, new_number

    if first_number is None or operator is None:
        return

    try:
        second_number = float(current_value)

        if operator == "+":
            result = first_number + second_number

        elif operator == "-":
            result = first_number - second_number

        elif operator == "×":
            result = first_number * second_number

        elif operator == "÷":

            if second_number == 0:
                current_value = "Error"
                update_display()

                first_number = None
                operator = None
                new_number = True

                return

            result = first_number / second_number

        if result.is_integer():
            current_value = str(int(result))
        else:
            current_value = str(result)

        first_number = None
        operator = None
        new_number = True

        update_display()

    except ValueError:
        current_value = "Error"
        update_display()


# =========================
# Rounded button
# =========================

def create_round_button(
        canvas,
        x,
        y,
        radius,
        text,
        background,
        foreground,
        command
):

    # Circle
    circle = canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill=background,
        outline=background
    )

    # Text
    label = canvas.create_text(
        x,
        y,
        text=text,
        fill=foreground,
        font=("Arial", 22)
    )

    # Click area
    def click(event):
        distance = math.sqrt(
            (event.x - x) ** 2 +
            (event.y - y) ** 2
        )

        if distance <= radius:
            command()

    canvas.tag_bind(circle, "<Button-1>", click)
    canvas.tag_bind(label, "<Button-1>", click)

    # Small visual effect when mouse enters
    def enter(event):
        canvas.itemconfig(circle, fill="#555555")

    def leave(event):
        canvas.itemconfig(circle, fill=background)

    canvas.tag_bind(circle, "<Enter>", enter)
    canvas.tag_bind(label, "<Enter>", enter)

    canvas.tag_bind(circle, "<Leave>", leave)
    canvas.tag_bind(label, "<Leave>", leave)


# =========================
# Buttons Canvas
# =========================

canvas = tk.Canvas(
    window,
    width=360,
    height=350,
    bg="black",
    highlightthickness=0
)

canvas.pack(
    padx=5,
    pady=5
)


# =========================
# Button positions
# =========================

radius = 35

x_positions = [45, 125, 205, 295]

y_positions = [
    35,
    105,
    175,
    245,
    315
]


# =========================
# Top row
# =========================

create_round_button(
    canvas,
    x_positions[0],
    y_positions[0],
    radius,
    "AC",
    "#a5a5a5",
    "black",
    clear_clicked
)

create_round_button(
    canvas,
    x_positions[1],
    y_positions[0],
    radius,
    "+/-",
    "#a5a5a5",
    "black",
    sign_clicked
)

create_round_button(
    canvas,
    x_positions[2],
    y_positions[0],
    radius,
    "%",
    "#a5a5a5",
    "black",
    percent_clicked
)

create_round_button(
    canvas,
    x_positions[3],
    y_positions[0],
    radius,
    "÷",
    "#ff9500",
    "white",
    lambda: operator_clicked("÷")
)


# =========================
# Row 2
# =========================

create_round_button(canvas, x_positions[0], y_positions[1], radius, "7", "#333333", "white", lambda: number_clicked("7"))
create_round_button(canvas, x_positions[1], y_positions[1], radius, "8", "#333333", "white", lambda: number_clicked("8"))
create_round_button(canvas, x_positions[2], y_positions[1], radius, "9", "#333333", "white", lambda: number_clicked("9"))
create_round_button(canvas, x_positions[3], y_positions[1], radius, "×", "#ff9500", "white", lambda: operator_clicked("×"))


# =========================
# Row 3
# =========================

create_round_button(canvas, x_positions[0], y_positions[2], radius, "4", "#333333", "white", lambda: number_clicked("4"))
create_round_button(canvas, x_positions[1], y_positions[2], radius, "5", "#333333", "white", lambda: number_clicked("5"))
create_round_button(canvas, x_positions[2], y_positions[2], radius, "6", "#333333", "white", lambda: number_clicked("6"))
create_round_button(canvas, x_positions[3], y_positions[2], radius, "−", "#ff9500", "white", lambda: operator_clicked("-"))


# =========================
# Row 4
# =========================

create_round_button(canvas, x_positions[0], y_positions[3], radius, "1", "#333333", "white", lambda: number_clicked("1"))
create_round_button(canvas, x_positions[1], y_positions[3], radius, "2", "#333333", "white", lambda: number_clicked("2"))
create_round_button(canvas, x_positions[2], y_positions[3], radius, "3", "#333333", "white", lambda: number_clicked("3"))
create_round_button(canvas, x_positions[3], y_positions[3], radius, "+", "#ff9500", "white", lambda: operator_clicked("+"))


# =========================
# Bottom row
# =========================

create_round_button(
    canvas,
    x_positions[0],
    y_positions[4],
    radius,
    "0",
    "#333333",
    "white",
    lambda: number_clicked("0")
)

create_round_button(
    canvas,
    x_positions[1],
    y_positions[4],
    radius,
    ".",
    "#333333",
    "white",
    decimal_clicked
)

create_round_button(
    canvas,
    x_positions[2],
    y_positions[4],
    radius,
    "=",
    "#ff9500",
    "white",
    equal_clicked
)


# =========================
# Start
# =========================

window.mainloop()