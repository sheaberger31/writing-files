def new_file():
    fav_team = input("what is your favourite NHL team?")
    player = input("who is your favourite NHL player?")
    file = fav_team + '.txt.'
    save = open(file, 'w')
    save.write("team,")
    save.write(fav_team + ',')
    save.write("Player,")
    save.write(player +",")
    
new_file()