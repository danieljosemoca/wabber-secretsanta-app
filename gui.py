import tkinter as tk
from main import SantaTime
import random

root = tk.Tk()
root.geometry("1000x700")
root.title("Secret Santa App")
w=tk.Label(root, text="Hey Buddy! Please select the participating committees.", font=("Papyrus", 25))
w.pack(pady=10)

committee_list = ["Academicie", "Almanac", "Alumni", "BAf",
                  "CaCo", "De Wabber", "Ecolution", "EI",
                  "Foreign Affairs", "FCP", "FYC",
                  "Idiomotor", "InNatura", "LifeLine",
                  "Lustrum",  "Paparazcie", "SLAK",
                  "StudyTour"]
vars_dict = {}
buttons_dict = {}

main_frame = tk.Frame(root)
main_frame.pack(fill='both', expand=True, padx=10, pady=10)

left_frame = tk.Frame(main_frame)
left_frame.pack(side='left', fill='y', padx=10, pady=10)

right_frame = tk.Frame(main_frame)
right_frame.pack(side='right', fill='both', expand=True, padx=10, pady=10)


for committee in committee_list:
    key = committee.lower().replace(" ", "_")
    vars_dict[key] = tk.IntVar()

    buttons_dict[key] = tk.Checkbutton(
        left_frame,
        text=committee,
        variable=vars_dict[key],
        onvalue=1,
        offvalue=0,
        height=2,
        width=15,
        pady=2
    )

    buttons_dict[key].pack(anchor='w', padx=20)
    buttons_dict[key].select()

results_box = tk.Text(right_frame, height=25, width=50, font=("Courier", 20))

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
    results_box.insert(tk.END, result_string)


main_button = tk.Button(right_frame, text = 'Reveal Setup!', command = shuffle, height=2, width=20)
main_button.pack(side='top', pady=20)
results_box.pack(side='top', pady=20, fill='both', expand=True)



root.mainloop()