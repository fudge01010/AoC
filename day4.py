class Card():
    def __init__(self) -> None:
        self.num = 0
        self.winning_nums = []
        self.card_nums = []
    
    def __repr__(self) -> str:
        return f"Card class, number {self.num}"

    def __str__(self) -> str:
        return f"Card number {self.num}, winners: {self.winning_nums}, plays: {self.card_nums}"

    def set_card_num(self, card_no: int):
        self.num = int(card_no)
    
    def card_num(self) -> int:
        return self.num

    def winning(self) -> [int]:
        return self.winning_nums
    
    def set_winning(self, winners: [int]) -> None:
        self.winning_nums = winners
    
    def play_nums(self) -> [int]:
        return self.card_nums
    
    def set_play_nums(self, playnums: [int]) -> None:
        self.card_nums = playnums
    
    def matches(self) -> int:
        return len(set(self.winning_nums).intersection(self.card_nums))

# load input data in
with open("input.txt", "r") as file:
    input_data = file.read().splitlines()

scratchcards: [Card] = []
# parse data
for scratchie in input_data:
    curr_card = Card()
    # test__ = scratchie.split(":")[0].split(" ")[-1]
    curr_card.set_card_num(scratchie.split(":")[0].split(" ")[-1])
    curr_card.set_winning(scratchie.split(": ")[1].split(" | ")[0].split())
    curr_card.set_play_nums(scratchie.split(": ")[1].split(" | ")[1].split())
    scratchcards.append(curr_card)
    # print(curr_card)

totalpoints = 0

for scratchie in scratchcards:
    matches = set(scratchie.winning()).intersection(scratchie.play_nums())
    # print(matches)
    if len(matches) != 0:
        # there are some matches
        totalpoints += pow(2, len(matches)-1)

print(f"Total sum of scratchie points is {totalpoints}")


## part 2
original_deck = scratchcards[:]
total_cards = [1 for _ in scratchcards]

for ccard in scratchcards:
    for i in range(ccard.matches()):
        total_cards[ccard.card_num() + i] += total_cards[ccard.card_num()-1]
print(f"we had {sum(total_cards)} in the pile")