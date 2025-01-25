import random

def updated_cards():
    coins = 500
    high_score = 0
    your_card_list = []
    dealer_card_list = []

    while coins != 0:
        if your_card_list == []:
            Ace = 11
            King = 10
            Queen = 10
            Jack = 10
            cards_list = [Ace,2,3,4,5,6,7,8,9,10,King,Queen,Jack]

            your_random_card1 = random.choice(cards_list)
            your_random_card2 = random.choice(cards_list)
            your_card_list =  [your_random_card1,your_random_card2]

            dealer_random_card1 = random.choice(cards_list)
            dealer_random_card2 = random.choice(cards_list)
            dealer_card_list = [dealer_random_card1,dealer_random_card2]

        print(f"Your cards : {your_card_list}")
        if sum(your_card_list) == 21:
            print("BLACK JACK | Congratulations !")
            print("You win !")
            coins += 100
            print(f"Your coin balance : {coins}")
            your_card_list.clear()
            dealer_card_list.clear()
            continue

        choose = input("Choose (Hit/Stand): ").lower()
        if high_score > coins:
            high_score = coins


        if choose[0] == "h":
            your_card_list.append(random.choice(cards_list))
            for i in range(len(your_card_list)):
                #it converts ace to 1 when the sum goes above 21 with ace
                if your_card_list[i] == 11 and sum(your_card_list) > 21:
                    your_card_list[i] = 1
            if sum(your_card_list) > 21:
                print(f"BUST! \n You lose : current cards{your_card_list}\n")
                coins -=100
                print(f"Your Coin balance : {coins}")
                your_card_list.clear()
                dealer_card_list.clear()
            else:
                continue 

        elif choose[0] == "s":
            print(f"Dealer cards:{dealer_card_list}")

            if sum(dealer_card_list) > sum(your_card_list):
                print(f"BUST \nYou lose !")
                print(f"Dealer cards : {dealer_card_list}\n")
                your_card_list.clear()
                dealer_card_list.clear()
                coins -=100
                print(f"Your coin balance : {coins}")
                continue
            elif sum(dealer_card_list) == sum(your_card_list):
                print("PUSH \nValue is same - Draw\n")
                your_card_list.clear()
                dealer_card_list.clear()
                continue

        while (sum(dealer_card_list) < 21) and (sum(your_card_list) > sum(dealer_card_list)):
                for i in range(len(dealer_card_list)):
                    if dealer_card_list[i] == 11 and sum(dealer_card_list) > 21:
                        dealer_card_list[i] = 1
                dealer_card_list.append(random.choice(cards_list))
                print(f"Dealer picks : {dealer_card_list}")
                if sum(dealer_card_list) >= 21:
                    break

        if sum(dealer_card_list) > 21:
            print("BUST \nYou win!\n")
            coins +=100
            print(f"Your coin balance : {coins}")
            your_card_list.clear()
            dealer_card_list.clear()
            
        elif sum(dealer_card_list) > sum(your_card_list) and sum(dealer_card_list) <= 21:
            print("BUST \nYou lose !\n")
            coins -=100
            print(f"Your coin balance : {coins}")
            your_card_list.clear()
            dealer_card_list.clear()

        elif sum(dealer_card_list) == 21:
            print(f"BUST \nYou lose!\n{dealer_card_list}")
            coins -=100
            print(f"Your coin balance : {coins}")
            your_card_list.clear()
            dealer_card_list.clear()
        if coins == 0:
            break
    print(f"Your highest coins : {high_score}")
    print(f"Game Over !")
    

updated_cards()