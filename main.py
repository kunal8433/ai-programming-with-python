# Gun Snake Water with fixed outcomes

# 1 = gun, 2 = snake, 3 = water

rounds = [
    2,  # 1st round → computer chooses snake
    3,  # 2nd round → computer chooses water
    2   # 3rd round → computer chooses snake
]

yourdict = {"s": 2, "w": 3, "g": 1}
maindict = {1: "gun", 2: "snake", 3: "water"}

for i in range(3):
    print(f"\n--- Round {i+1} ---")
    youstr = input("Enter your choice (s/w/g): ").lower()

    if youstr not in yourdict:
        print("Invalid input")
        continue

    you = yourdict[youstr]
    computer = rounds[i]

    print(f"You chose {maindict[you]}")
    print(f"Computer chose {maindict[computer]}")

    if computer == you:
        print("Match Draw 🤝")
    elif (
        (you == 1 and computer == 2) or
        (you == 2 and computer == 3) or
        (you == 3 and computer == 1)
    ):
        print("You Win 🎉")
    else:
        print("Computer Wins 💻")
