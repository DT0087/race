from slime import Slime

def main():
    slimes = [
        ("=", "〇"), 
        ("~", "✕"),
        ("*", "★"),
    ]

    slimes = [Slime(*data) for data in slimes]

    print("list of runners")
    for i, slime in enumerate(slimes):
        print(f"No.{i+1}: {slime.marker}")

    while True:
        user_input = input("[Bet]\nNo: ").strip()
        user_input = user_input.translate(str.maketrans("０１２３４５６７８９", "0123456789"))

        if user_input.isdigit():
            bet_input = int(user_input)
            if 1 <= bet_input <= len(slimes):
                break
            else:
                print(f"Please enter a number between 1 and {len(slimes)}")
        
        else:
            print("Please enter a valid number")
    
    
    bet_marker = slimes[bet_input - 1].marker

    # カウントダウン　３秒　で始まる
    import time
            
    print("[on your mark]")
    for i in range(3, 0, -1):
        print(f"{i}", end='\r')
        time.sleep(1)
    print("GO!") 
    time.sleep(1)


    print("----５----10")

    #レース
    while True:
        for slime in slimes:
            slime.display()
            slime.run()
        print("----５----10")

        winners = [slime for slime in slimes if slime.position > 10]

        if winners:
            print("Winner!")
            for slime in winners:
                print(f"{slime.marker}")
            break

    print(f"your bet on {bet_marker}")
    if any(slime.marker == bet_marker for slime in winners):
        print("You win!")
    else:
        print("You lose!")
        

if __name__ == "__main__":
    main()
