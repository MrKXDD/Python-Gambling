import random


def spin_reel():
    symbols = ['🍒', '🍉', '🍎', '🧋', '🍗']

    results = []
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results
    #could also use "return [random.choice(symbols) for symbol in range(3)]"

def print_reel(reel):
    print("*************")
    print(" | ".join(reel))
    print("*************")

def payout(reel, bet):
    if reel[0] == reel[1] == reel[2]:
        if reel[0] == '🍒':
            return bet * 1
        elif reel[0] == '🍉':
            return bet * 3
        elif reel[0] == '🍎':
            return bet * 5
        elif reel[0] == '🧋':
            return bet * 10
        elif reel[0] == '🍗':
            return bet * 50
    return 0

def main():
    money = 100

    print("****************************")
    print("welcome to K's Slot Machine")
    print("Symbols: 🍒 🍉 🍎 🧋 🍗")
    print("****************************")

    while money > 0:
        print(f"Current Balance: ${money}")
        bet = input("Place your bet:")
        if not bet.isdigit():
            print("Please place a valid bet")
            continue

        bet = int(bet)
        if bet > money:
            print("Insufficient Funds")
            continue
        if bet <= 0:
            print("Bet must be greater than zero")
            continue
        money -= bet

        reel = spin_reel()
        print("Spinning...\n")
        print_reel(reel)

        paid = payout(reel, bet)
        if paid > 0:
            print(f"You Won ${paid}")
        elif paid > (bet * 50):
            print(f"JACKPOT ${paid}$")
        else:
            print("No matches? No pay.")
        money += paid

        play_again = input("Spin Again? (Y/N): ").upper()

        if play_again != 'Y':
            break
    print("***************************************************")
    print(f"Congratulations, You're now worth: ${money}")
    print("***************************************************")
if __name__ == '__main__':
    main()