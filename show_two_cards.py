# spade 0 club 1 dia 2 ht 3

def show_two_cards(card1, card2):
    cards = [["│          ♠          │", "│        ♠ ♠         │", "│       ♠ ♠ ♠       │", "│      ♠ ♠ ♠ ♠     │","│    ♠ ♠ ♠ ♠ ♠    │"],
             ["│          ♥          │", "│        ♥ ♥         │", "│       ♥ ♥ ♥       │", "│      ♥ ♥ ♥ ♥     │","│    ♥ ♥ ♥ ♥ ♥    │"],
             ["│          ◆          │", "│        ◆ ◆         │", "│       ◆ ◆ ◆       │", "│      ◆ ◆ ◆ ◆      │","│    ◆ ◆ ◆ ◆ ◆     │"],
             ["│          ♣          │", "│        ♣ ♣         │", "│       ♣ ♣ ♣       │", "│      ♣ ♣ ♣ ♣     │","│    ♣ ♣ ♣ ♣ ♣    │"],
             ["│      J O K E R       │"],
             ["│      J O K E R       │"]]

    map = {"Spade": 0, "Heart": 1, "Diamond": 2, "Club": 3,"joker1":4,"joker2":5}

    suit1 = card1['rank']
    rank1 = card1['suit']
    suit2 = card2['rank']
    rank2 = card2['suit']


    print("┌───────────-┐             ┌───────────-┐")
    print(cards[map[rank1]][suit1-1] + "    (( ))    " + cards[map[rank2]][suit2-1])
    print("└───────────-┘             └───────────-┘")

