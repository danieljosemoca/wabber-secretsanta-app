import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from main import SantaTime
import random

# themes and main labels and such
root = ThemedTk(theme='yaru')
root.geometry("1000x700")
root.title("Secret Santa App")
w=ttk.Label(root, text="Hey Buddy! Please select the " \
"participating committees.", font=("Arial", 25))
w.pack(pady=10)

# frames
main_frame = ttk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

left_frame = ttk.Frame(main_frame)
left_frame.pack(side='left', fill='y', padx=10, pady=10)

right_frame = ttk.Frame(main_frame)
right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)


# checkbuttons
committee_list = ["Academicie", "Almanac", "Alumni", "BAf",
                  "CaCo", "De Wabber", "Ecolution", "EI",
                  "FA", "FCP", "FYC",
                  "Idiomotor", "InNatura", "LifeLine",
                  "Lustrum",  "Paparazcie", "SLAK",
                  "StudyTour"]
vars_dict = {}
buttons_dict = {}

for committee in committee_list:
    key = committee.lower().replace(" ", "_") # python style rules
    vars_dict[key] = tk.IntVar()

    buttons_dict[key] = ttk.Checkbutton(
        left_frame,
        text=committee,
        variable=vars_dict[key],
        onvalue=1,
        offvalue=0,
        width=15,
    )
    buttons_dict[key].invoke()

    buttons_dict[key].pack(anchor='w', padx=20)

# "Add Other" option for future new committees 
other_label = ttk.Label(left_frame, text='Add Other: ')
other_label.pack(anchor='w', padx=20, pady=(10, 0))
entry = ttk.Entry(left_frame, exportselection=False, font=("Arial"), foreground="Purple")
entry.pack(anchor='w', padx=20)


# result box
results_box = tk.Text(right_frame, height=25, width=50, font=("PT Mono", 20))
results_box.tag_configure("center", justify='center')

# calls main.py logic
def shuffle():
    selected = []
    for committee in committee_list:
        key = committee.lower().replace(" ", "_")
        if vars_dict[key].get() == 1:
            selected.append(committee)
    santa = SantaTime(selected)
    santa.shuffle_until_valid()
    result_string = santa.return_string_results() 
    results_box.delete("1.0", tk.END)
    results_box.insert(tk.END, result_string, "center")

# big button calls shuffle()
main_button = ttk.Button(right_frame,
                        text ='Reveal Setup!',
                        command=shuffle, 
                        width=20,

                    )
main_button.pack(side='top', pady=20, anchor="center")
results_box.pack(side='top', pady=20, fill='both', expand=True)

root.mainloop()