def mad_libs_camping_trip():
    adjective = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")

    story = f"Once upon a time, a group of {adjective} friends decided to go on a camping adventure. " \
            f"Little did they know, they would encounter some {adjective} surprises along the way. " \
            f"When they tried to set up their {noun1}, they realized they forgot to pack the {noun2}. " \
            f"It was a {adjective} disaster! Despite the setbacks, they made the best of the situation " \
            f"by telling {adjective} jokes, singing silly songs, and eating {adjective} marshmallows. " \
            f"In the end, it turned out to be the most unforgettable and {adjective} camping trip ever!"

    return story


def mad_libs_superhero():
    noun = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    adjective2 = input("Enter another adjective: ")
    noun2 = input("Enter another noun: ")

    story = f"In a world where {noun} roam the streets, one {adjective1} person discovered their extraordinary powers. " \
            f"With their ability to {verb1} and {verb2}, they became the {adjective2} superhero the world had ever seen. " \
            f"They fought against the forces of {noun2}, using their {adjective2} gadgets and their trusty sidekick, " \
            f"a talking {noun}. Together, they brought laughter, {adjective2} justice, and saved the world from boredom. " \
            f"Their superhero name? The Mighty {noun}!"

    return story


def mad_libs_space_adventure():
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter yet another adjective: ")
    noun2 = input("Enter another noun: ")
    adjective4 = input("Enter one more adjective: ")

    story = f"Once in a galaxy far, far away, a {adjective1} astronaut embarked on an intergalactic mission. " \
            f"Their spaceship, named the {noun1}, traveled at {adjective2} speed through the cosmos. " \
            f"They encountered friendly aliens with {adjective3} tentacles and explored planets with {adjective4} " \
            f"landscapes. On their journey, they discovered a hidden treasure of {noun2}, bringing joy and " \
            f"{adjective4} wonder to the universe. It was an epic space adventure full of laughter, exploration, " \
            f"and {adjective2} stardust."

    return story


def mad_libs_science_experiment():
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    adjective2 = input("Enter another adjective: ")
    adjective3 = input("Enter yet another adjective: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter one more noun: ")

    story = f"In a {adjective1} laboratory, a group of scientists conducted a wild and {adjective2} experiment. " \
            f"They mixed {adjective3} potions, causing {noun1} to float, and created {adjective2} explosions of colors. " \
            f"As they wore their {noun2} goggles, they discovered a formula that made objects {adjective3} " \
            f"and others {adjective2}. The lab turned into a place of {adjective1} chaos and laughter " \
            f"as they embraced the unpredictable nature of science. It was a day of {adjective3} discoveries " \
            f"and {adjective2} breakthroughs!"

    return story


while True:
    print("The Hilarious Camping Trip:")
    print(mad_libs_camping_trip())
    print()

    if input('Continue? (yes or no): ').lower() != 'yes':
        break

    print("The Whacky Superhero:")
    print(mad_libs_superhero())
    print()

    if input('Continue? (yes or no): ').lower() != 'yes':
        break

    print("The Epic Space Adventure:")
    print(mad_libs_space_adventure())
    print()

    if input('Continue? (yes or no): ').lower() != 'yes':
        break

    print("The Wacky Science Experiment:")
    print(mad_libs_science_experiment())
    print()

    if input('Continue? (yes or no): ').lower() != 'yes':
        break
