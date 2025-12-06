import random

def santa_function(committees: list[str]) -> dict[str, str]:
    if len(committees) < 3:
        raise ValueError("Input at least at least three committees.")

    shuffled = committees[:]  # make committee list copy
    max_tries = 10000
    for _ in range(max_tries):  # think like a machine
        random.shuffle(shuffled) # shuffle the copy
        pair_attempt = list(zip(committees, shuffled))  # attempt at pre-dictionary

        # ensure no comittee is assigned to itself
        self_assigned_found = False
        if any(giver == receiver for giver, receiver in pair_attempt):
            self_assigned_found = True

        # avoid committee A being assigned to B WHILE B is assigned to A
        # ex: I don't want Ecolution to get De Wabber 
        # if De Wabber already gets Ecolution
        mutual_found = False
        set_object = set(pair_attempt)  # iterator wouldn't work
        for giver, receiver in pair_attempt:
            if (receiver, giver) in set_object:
                mutual_found = True
                break

        if not mutual_found and not self_assigned_found:
            break
    
    return dict(pair_attempt)

def santa_printer(dicty: dict[str, str]) -> None:
    print("=== Secret Santa Pairings ===")
    # for dynamic field width alignment in f-string
    max_len = max(len(k) for k in dicty)
    for giver, receiver in dicty.items():
        #  add spaces to the right of giver until character num = max_len
        print(f"{giver:<{max_len}}  →  {receiver}") 
    print("=============================")


def main() -> None:
    items = input("Enter the names of the participating committees, " \
    "separated by commas: ").split(",")
    items = [i.strip() for i in items]
    mapping = santa_function(items)
    santa_printer(mapping)

if __name__ == "__main__":
    main()
