import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from pairing_logic import SantaTime
import customtkinter as ctk

ctk.set_appearance_mode("light")

# themes and main labels and such
root = ThemedTk(theme="yaru")
root.geometry("1000x700")
root.title("Secret Santa App")
w = ttk.Label(
    root,
    text="Hey Buddy! Please select the participating committees.",
    font=("Arial", 25),
)
w.pack(pady=10)

# frames
main_frame = ttk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

left_frame = ttk.Frame(main_frame)
left_frame.pack(side="left", fill="y", padx=10, pady=10)

checks_frame = ttk.Frame(left_frame)
checks_frame.pack(anchor="nw", fill="y")

right_frame = ttk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)


# checkbuttons
def _make_checkbutton(committee):
    key = committee.lower().replace(" ", "_")  # python style rules
    vars_dict[key] = tk.IntVar()

    buttons_dict[key] = ttk.Checkbutton(
        checks_frame,
        text=committee,
        variable=vars_dict[key],
        onvalue=1,
        offvalue=0,
        width=15,
    )
    buttons_dict[key].invoke()

    buttons_dict[key].pack(anchor="w", padx=20)


committee_list = [
    "Academicie",
    "Almanac",
    "Alumni",
    "BAf",
    "CaCo",
    "De Wabber",
    "Ecolution",
    "EI",
    "FA",
    "FCP",
    "FYC",
    "Idiomotor",
    "InNatura",
    "LifeLine",
    "Paparazcie",
    "SLAK",
    "StudyTour",
]
vars_dict = {}
buttons_dict = {}

for committee in committee_list:
    _make_checkbutton(committee)


# Add Other section
other_label = ttk.Label(left_frame, text="Add Other: ")
other_label.pack(anchor="w", padx=20, pady=(15, 0))

other_entry = ctk.CTkEntry(
    left_frame,
    corner_radius=9,
    width=156,
    exportselection=False,
    font=("Arial", 12),
    border_color="#A55B82",
)
other_entry.pack(anchor="w", padx=20)


def add_other_committee():
    """
    Adds the committee typed in the entry box to the list,
    and creates its checkbutton.
    Removes the entry after checkbutton creation.
    """
    # checks
    name = other_entry.get().strip()
    if not name:
        return
    if name in committee_list:
        return

    committee_list.append(name)
    _make_checkbutton(name)
    other_entry.delete(0, tk.END)


add_button = ttk.Button(left_frame, text="Add", command=add_other_committee, width=8)
add_button.pack(anchor="w", padx=20, pady=(5, 10))


# toggle button for single cycle option
def update_toggle_text():
    if toggle_var.get() == 1:
        scl_toggle.config(
            text="Continuous Chain Mode (Recommended) -  ON",
            foreground="#772953",
            selectcolor="#772953",
        )
    else:
        scl_toggle.config(
            text="Continuous Chain Mode (Recommended) - OFF",
            foreground="#219090",
            selectcolor="#219090",
        )


toggle_var = tk.IntVar()
scl_toggle = tk.Checkbutton(
    left_frame,
    variable=toggle_var,
    command=update_toggle_text,
    wraplength=200,
    indicatoron=False,
    borderwidth=4,
    foreground="#772953",
    selectcolor="#772953",
)

scl_toggle.invoke()
scl_toggle.pack(anchor="w", padx=20)


# result box
results_box = tk.Text(
    right_frame,
    height=25,
    width=50,
    font=("PT Mono", 20),
    relief="groove",
    selectbackground="#6E3954",
    inactiveselectbackground="#4E9195",
    highlightthickness=0.5,
)
results_box.config(highlightbackground="#772953", highlightcolor="#772953")
results_box.tag_configure("center", justify="center")


# main button
def shuffle():
    """Calls main.py logic. Applied when main button is pressed."""
    selected = []
    for committee in committee_list:
        key = committee.lower().replace(" ", "_")
        if vars_dict[key].get() == 1:
            selected.append(committee)
    santa = SantaTime(selected)
    if toggle_var.get() == 1:
        santa.single_cycle_shuffle()
    else:
        santa.shuffle_until_valid()
    result_string = santa.return_string_results()
    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, result_string, "center")


s = ttk.Style()
s.configure("Main.TButton", foreground="#772953", font=("Arial", 18, "bold"))
s.map(
    "Main.TButton",
    foreground=[("pressed", "#135E5E"), ("active", "#219090")],
)

main_button = ttk.Button(
    right_frame,
    text="Reveal Setup!",
    command=shuffle,
    width=20,
    cursor="gobbler",
    style="Main.TButton",
)
main_button.pack(side="top", pady=8, anchor="center")
results_box.pack(side="top", pady=25, fill="both", expand=True)

root.mainloop()
