import tkinter as tk
root = tk.Tk()
root.geometry("1000x700")
root.title("Secret Santa App")
w=tk.Label(root, text="Hey Buddy! Please select the participating committees.")
w.pack()

committee_list = ["Academicie", "Almanac", "Alumni", "BAf",
                  "CaCo", "De Wabber", "Ecolution", "EI",
                  "Foreign Affairs", "FCP", "FYC",
                  "Idiomotor", "InNatura", "LifeLine",
                  "Lustrum",  "Paparazcie", "SLAK",
                  "StudyTour"]
vars_dict = {}
buttons_dict = {}


for committee in committee_list:
    key = committee.lower().replace(" ", "_")
    vars_dict[key] = tk.IntVar()

    buttons_dict[key] = tk.Checkbutton(
        root,
        text=committee,
        variable=vars_dict[key],
        onvalue=1,
        offvalue=0,
        height=2,
        width=15
    )

    buttons_dict[key].pack(anchor='w', padx=20)
    buttons_dict[key].select()


def get_selected_committees():
    selected = []
    for committee in committee_list:
        key = committee.lower().replace(" ", "_")
        if vars_dict[key].get() == 1:
            selected.append(committee)
    return selected

main_button = tk.Button(root,text = 'Reveal Setup!', command = get_selected_committees)
main_button.pack(pady=20)

root.mainloop()

