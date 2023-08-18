from tamagotchi import Tamagotchi

tamagotchis = {}


def show_tamagotchis():
    # sort tamagotchis
    sorted_tamagotchis = sorted(tamagotchis.items(), key=lambda t: t[0])
    for name, tamagotchi in sorted_tamagotchis:
        print(tamagotchi)


playing = True

while playing:
    command = input("Command: ")

    if not command:
        playing = False
        break

    args = command.split(" ")

    if args[0] == "create":
        name = args[1]

        if name in tamagotchis:
            if not tamagotchis[name].is_dead():
                print("You already have a Tamagotchi called that.")
                continue

        tamagotchi = Tamagotchi(name)
        tamagotchis[name] = tamagotchi
    elif args[0] == "feed":
        name = args[1]
        if name not in tamagotchis:
            print("No Tamagotchi with that name.")
            continue
        tamagotchis[name].feed()
    elif args[0] == "play":
        name = args[1]
        if name not in tamagotchis:
            print("No Tamagotchi with that name.")
            continue
        tamagotchis[name].play()
    elif args[0] != "wait":
        print("Invalid command.")
        continue

    show_tamagotchis()
    for tamagotchi in tamagotchis.values():
        tamagotchi.increment_time()
