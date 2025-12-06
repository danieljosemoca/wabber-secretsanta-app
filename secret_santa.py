import random

class SantaTime: 
    """Class to handle Secret Santa committee pairings."""
    def __init__(self, committees: list[str]) -> None: 
        self._validate_list(committees)
        self.committees = committees
        self.shuffled_committees: dict[str, str] | None  = None


    def _validate_list(self, committees: list[str]) -> None: 
        if len(committees) < 3:
            raise ValueError("Input at least at least three committees.")
        if len(set(committees)) != len(committees):
            raise ValueError("Committee names must be unique.")
        if len(committees) == 3:
            # special case for 3 committees
            self.three_items = True
        else: 
            self.three_items = False


    def shuffle_until_valid(self, max_tries = 10000) -> None:
        """
        Pair the provided committees.
        Avoids self-pairing (committee assigned to itself),
        and mutual pairing (committee A assigned to gift to committee B
        while committee B is already assigned to gift to committee A).
        
        Args:
            committees: List of committee names.
            max_tries: Maximum number of shuffle attempts to find a valid pairing.
                        'Incorrect' pairing used if max_tries exceeded.

        Returns:
            A dictionary mapping each committee to the committee they will gift to.
        """

        if self.three_items == None:
            raise ValueError("Committee list not validated.")

        shuffled = self.committees[:]  # make committee list copy
        for try_number in range(max_tries):  # think like a machine
            valid_found = False

            if self.three_items == True: 
                
                self.shuffled_committees = {
                    self.committees[0]: self.committees[1],
                    self.committees[1]: self.committees[2],
                    self.committees[2]: self.committees[0],
                }
                valid_found = True
                return
            
            random.shuffle(shuffled) # shuffle the copy
            pair_attempt = list(zip(self.committees, shuffled))  # attempt at pre-dictionary

            # ensure no comittee is assigned to itself
            self_assigned_found = False
            if any(giver == receiver for giver, receiver in pair_attempt):
                self_assigned_found = True

            # avoid committee A being assigned to B WHILE B is assigned to A
            # ex: I don't want Ecolution to get De Wabber 
            # if De Wabber already gets Ecolution
            mutual_found = False
            for giver, receiver in pair_attempt:
                if (receiver, giver) in pair_attempt:
                    mutual_found = True

            if not mutual_found and not self_assigned_found:
                valid_found = True
                self.shuffled_committees = dict(pair_attempt)
                break

        if valid_found == False:
            print("Warning: Maximum shuffle attempts reached without finding a valid " \
            "pairing. An incorrect pairing has been assigned.")
            self.shuffled_committees = dict(pair_attempt)


    def print_results(self) -> None:
        "Print Secret Santa pairings in aligned format."
        print("=== Secret Santa Pairings ===")
        # for dynamic field width alignment in f-string
        max_len = max(len(k) for k in self.committees)
        for giver, receiver in self.shuffled_committees.items():
            #  add spaces to the right of giver until character num = max_len
            print(f"{giver:<{max_len}}  →  {receiver}") 
        print("=============================")


def main() -> None:
    items = input("Enter the names of the participating committees, " \
    "separated by commas: ").split(",")
    items = [i.strip() for i in items]
    santa = SantaTime(items)
    santa.shuffle_until_valid()
    santa.print_results()

if __name__ == "__main__":
    main()