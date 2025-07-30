print('Welcome to Dreamworld, lets see what rides you are eligible to ride')

age = int(input('How old are you?: '))
height = int(input('How tall are you? (cm): '))

if height < 80 and 3 <= age <= 8:
    print('You are allowed to go on the Fortress of Fun!')

if height > 80:
    print('You are allowed to go on the Log Flume, Gold Rush, Family Karts (passenger only), Dogems (passenger only)')

if height > 90 and age >= 5:
    print('You are allowed to go on the Los Banditos')

if height > 90 and age >= 8:
    print('You are allowed to go on the Robot Riot')

if height > 120:
    print('You are allowed to go on the Fearfall, Invader, Corkscrew Roller Coaster, and Bumber Boats')

if height > 150:
    print('You are allowed to go on the Stratosfear, Family Karts, and Scorpion Karts')

if height < 80 and age > 3:
    print('Sorry! You are not allowed to go on any of the rides')

