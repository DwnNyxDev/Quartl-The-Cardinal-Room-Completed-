import sys
import time
door_status = "closed"
door_status = str(door_status)
inventory = []
exit_known = 0
room_known = 0
door_close = 0
lights_on = 0
def GameOver():
  print("Game Over")
  time.sleep(3)
  print("Play Again?")
  restart = input(">")
  if "yes" or "Yes" in restart:
    Lying_Down1()
  elif "no" or "No" in restart:
    print("Okay, Maybe Next Time.")
    sys.exit(0)
  else:
    print("It's a yes or no question")
    GameOver()
def b_GameOver():
  print("Okay, Maybe Next Time")
  sys.exit(0)



print("Welcome to Quartl")
time.sleep(1)
print("What is your name? (Capitals matter)")
user_name = input(">")
time.sleep(1.5)
print("Hello",user_name)
time.sleep(1)
print ("type start to begin")
begin = input(">")
if begin == "start":
  time.sleep(2)
  print("You are a normal person in an abnormal place")
  time.sleep(2)
  print("Your game. Your choices.")
  time.sleep(2)
  print("throughout the game you will be given more and more choices but for now...")
  time.sleep(3)
  print ("type (stand) to stand up")
  time.sleep(1.2)
  print ("type (sit) to sit up")
  time.sleep(1.2)
  print ("type (lie down) to lie down")
  time.sleep(1.2)
  print("type (look) to look around")
  time.sleep(1.2)
  print("type (search) + object name to look at or through object")
  time.sleep(1.2)
  print("type (use) + object name to use object")
  time.sleep(1.2)
  print("type (north) to go north")
  time.sleep(1.2)
  print("type (south) to go south")
  time.sleep(1.2)
  print("type (east) to go east")
  time.sleep(1.2)
  print("type (west) to go west")
  time.sleep(1.2)
  print("type (open) to open something")
  time.sleep(1.2)
  print("type (fight) + creature to fight creature")
  time.sleep(1.2)
  print("type (dodge) + direction (left,right,forward,backward) to dodge something")
  time.sleep(1.7)
  print ("type (pick up) + item to pick up something")
  time.sleep(1.2)
  print ("type (exit) to exit a place")
  time.sleep(1.2)
  print("Whether you live or die is up to you")
  time.sleep(1.2)
  print("so... let us begin")
  time.sleep(3)
  print()
  print()
  print("You awaken in a large empty room.")
  time.sleep(1)
  print("You have no idea how you got there")
  time.sleep(1)
  game_begin = time.time()
  def gas_door():
    print("You are at a door")
    gasdoor = input(">")
    if "use key" in gasdoor:
      print("This door cannot be unlocked with a key from this side")
      
      gas_door()
    elif "look" in gasdoor:
      print("try to be more specific")
      
      gas_door()
    elif "search door" in gasdoor:
      print("You look at the door and see a question on a screen in the door and a keyboard")
      print("new command gained (play quiz)")
      gas_door()
    elif "play quiz" in gasdoor:
      score = 0
      print ("What is the name of this game?")
      answer1 = input(">")
      if "Quartl" in answer1:
        score += 1
      elif "quartl" in answer1:
        score = score + 1
      print("What is your name?")
      answer2 = input(">")
      if user_name in answer2:
        score = score + 1
      print ("How many doorways were there in the room you woke up in?")
      answer3 = input(">")
      if str(4) in answer3:
        score = score+1
      print ("What was the south doorway?")
      answer4 = input(">")
      if "exit" or "Exit" in answer4:
        score=score+1
      if score == 4:
        print ("You win the quiz.")
        time.sleep(.7) 
        print ("Transporting you to middle room")
        stand2()
      elif score < 4:
        print ("You lost the quiz")
        time.sleep(1)
        print("The gas fills the room and kills you")
        GameOver()
    elif "west" in gasdoor:
      print("The door is locked")
      
      gas_door()
    elif "open" in gasdoor:
      print("The door is locked")
      
      gas_door()
    elif "exit" in gasdoor:
      print("The door is locked")
      
      gas_door()
    else:
      print ("this command is currently unavailavle")
      gas_door()
  def middle_of_east_room2():
    print("You are in the middle of the hallway")
    getkey2 = input(">")
    if "east" in getkey2:
      
      westkey()
    elif "west" in getkey2:
      
      gas_door()
    else:
      print("command is currently unavailable")
      middle_of_east_room2()
  def westkey():
    print ("You are at the end of the hallway")
    getkey2 = input(">")
    if "look" in getkey2:
      print("there is a key on a table")
      
      westkey()
    elif "pick up key" in getkey2:
      print("You have picked up the key")
      inventory.append("west key")
      
      westkey()
    elif "west" in getkey2:
      middle_of_east_room2()
      
    else:
      print("command is currently unavailable")
      
      westkey()
  def middle_of_east_room():
    global gas
    gas = 0
    print ("Halfway to the key, you hear a creak.")
    time.sleep(1)
    print("You quickly turn back and watch the door behind you close")
    time.sleep(1)
    print("A purple gas starts entering the room from air grates above")
    getkey4 = input(">")
    if "east" in getkey4:
      westkey()
      
    elif "west" in getkey4:
      gas_door()
      
    else:
      print("command is currently unavailable")
      
      middle_of_east_room2()
  def east_room():
    print("You are in the east room")
    east_room_actions = input(">")
    if "look" in east_room_actions:
      print("You look and see that the east room is actually a hallway")
      time.sleep(1.3)
      print("You see a key at the end of the hallway")
      east_room()
    elif "exit" in east_room_actions:
      stand2()
    elif "east" in east_room_actions:
      middle_of_east_room()
    else:
      print("command is currently unavailable")
      east_room()
  def east1unlocked():
    print ("You are at an open door")
    print("Tip from creator: Try searching the south door window before you enter.")
    go_back_west2 = input(">")
    if "west" in go_back_west2:
      stand2()
    elif "east" in go_back_west2:
      east_room()
    else:
      print ("command is currently unavailable")
      east1unlocked()
  def unlock_east_door():
    print ("You have unlocked the east door")
    open_east_door = input(">")
    if "open" in open_east_door:
      east1unlocked()
    elif "east" in open_east_door:
      print("Maybe you should open the door first")
      unlock_east_door()
    else:
      "command is currently unavailable"
      unlock_east_door()
  def stand2():
    print ("You are now standing in a room.")
    do_what4 = input(">")
    if "look" in do_what4:
      print("You look around and see open doorways to the east and north, and closed doorways to the west and south")
      stand2()
    elif "north" in do_what4:
      north1()
    elif "east" in do_what4:
      east1unlocked()
    elif "west" in do_what4:
      west1()
    if "south" in do_what4:
      south1()
    else:
      print("command is currently unavailable")
      stand2()
  def east1():
    print ("You are at a",str(door_status),"door")
    go_back_west = input(">")
    if "west" in go_back_west:
      stand1()
    elif "use key" in go_back_west:
      if "east key" in inventory:
        unlock_east_door()
        inventory.remove("east key")
      else:
        print ("You do not own the correct item")
        east1()
    else:
      print ("command is currently unavailable")
      east1()
  def newlobby():
    print ("You are now standing in a room.")
    do_what8 = input(">")
    if "look" in do_what8:
      print ("You look around and see open doorways north, east, and west, and south")
      newlobby()
    elif "north" in do_what8:
      print("You are so close to winning the game, try again.")
      newlobby()
    elif "east" in do_what8:
      print("You are so close to winning the game, try again.")
      newlobby()
    elif "west" in do_what8:
      print("You are so close to winning the game, try again.")
      newlobby()
    elif "south" in do_what8:
      openexit()
    else:
      print("command is currently unavailable")
      newlobby()
  def exit_room():
    print("There is an club with nothing in it.")
    exit_room1 = input(">")
    if "exit" in exit_room1:
      stand3()
    elif "east" in exit_room1:
      stand3()
    elif "pick up club" in exit_room1:
      print("The club is too big")
      exit_room()
    else:
      print("This command is currently not available")
      exit_room()
  def search_club():
    print("There's a key inside the club.")
    get_key9 = input(">")
    if "pick up key" in get_key9:
      print("You have picked up the key")
      inventory.append("south key")
      exit_room()
    else:
      print("command is currently unavailable")
      search_club()
  def findsword():
    print("You can see something shining in the orge's club")
    get_key8 = input(">")
    if "west" in get_key8:
      print("Your way is blocked by a giant club")
    elif "look" in get_key8:
      print ("You look and see the body of an orge in the middle of the room")
      time.sleep(1)
      print("The ogre's club is directly in front of you")
    elif "pick up key" in get_key8:
      print("you must search the club first")
      findsword()
    elif "search club" in get_key8:
      search_club()
    else:
      print("this command is currently unavailable") 
      findsword()
  def breaksword():
    print ("You run away from the ogre, but he is too quick.")
    time.sleep(1)
    print("As he runs towards you, he steps on the sword and breaks it.")
    time.sleep(1.5)
    print("He reaches you in a matter of seconds.")
    no_sword = input(">")
    if "fight ogre" in no_sword:
      print ("You punch the ogre with your bare hands and barely do any damage.")
      time.sleep(1)
      print("The ogre, now mad, pulls out a club, and horizantly swings at you")
      bad_punch = input()
      if "dodge backward" or "dodge backwards" in bad_punch:
        print("You successfully dodge backwards")
        time.sleep(1)
        print("The ogre, missing his swing, clubs himself over the head, knocking himself out.")
        time.sleep(1)
        findsword()
      else:
        print("You fail to dodge and die")
        GameOver()
    elif "east" in no_sword:
      print("You fail to run away and the orge kills you with a club")
      GameOver()
    else:
      print("This command is currently unavailable")
      breaksword()
  def getkey4():
      print("The ogre drops what looks like a club. There is something shining in the club.")
      get_key4 = input(">")
      if "west" in get_key4:
        print("Your way is blocked by a giant club")
      if "look" in get_key4:
        print ("You look and see the body of an orge in the middle of the room")
        time.sleep(1)
        print("The ogre's club is directly in front of you")
      if "search club" in get_key4:
        search_club()
      if "pick up key" in get_key4:
        print("You must search the club first")
        getkey4()
      else:
        print("command is currently unavailable")
        getkey4()
  def middle_of_west_room():
    print ("You are in the middle of the west room")
    time.sleep(1)
    print("You hear loud thuds but you don't know where it's coming from...")
    time.sleep(1.5)
    print("Suddenly, an ogre enters from the giant hole")
    pick_up_sword = input(">")
    if "east" in pick_up_sword:
      breaksword()
    elif "look" in pick_up_sword:
      print("There is a sword on the ground in front of you")
      middle_of_west_room()
    elif "east" in pick_up_sword:
      breaksword()
    elif "pick up sword" in pick_up_sword:
      print("You picked up the sword. The ogre starts running towards you")
      inventory.append("sword")
      use_sword = input()
      if "use sword" in use_sword:
        print("You use the sword and kill the ogre easily.")
        time.sleep(1)
        getkey4()  
      elif "fight ogre" in use_sword:
        print("You use the sword and kill the ogre easily.")
        time.sleep(1)
        getkey4()
      else:
        print("Your indecisiveness has cost you your life")
        GameOver()
    else:
      print("This command is currently unavailable")
      middle_of_west_room()

  def west_room():
    print("You are in the west room")
    west_room_actions = input(">")
    if "look" in west_room_actions:
      print ("You look around and see bones littering the edges of the room.")
      time.sleep(1)
      print("A key is nowhere to be found.")
      time.sleep(.8)
      print("A sword is in the middle of the room. A giant hole is at the end of the room")
      time.sleep(1)
      west_room()
    elif "exit" in west_room_actions:
      stand3()
    elif "west" in west_room_actions:
      middle_of_west_room()
    elif "east" in west_room_actions:
      west1unlocked()
    else:
      print ("command is currently unavailable")
      west_room()
  def stand3():
    print ("You are now standing in a room.")
    do_what6 = input(">")
    if "look" in do_what6:
      print ("You look around and see open doorways north, east, and west, and a closed doorway south")
      stand3()
    elif "north" in do_what6:
      north1()
    elif "east" in do_what6:
      east1unlocked()
    elif "west" in do_what6:
      west1unlocked()
    if "south" in do_what6:
      south1()
    else:
      print("command is currently unavailable")
      stand3()
  def west1unlocked():
    print ("You are at an open door")
    go_back_east2 = input(">")
    if "east" in go_back_east2:
      stand3()
    elif "west" in go_back_east2:
      west_room()
    else:
      print ("command is currently unavailable")
      west1unlocked() 
  def unlock_west_door():
    print ("You have unlocked the west door")
    open_west_door = input(">")
    if "open" in open_west_door:
      west1unlocked()
    elif "west" in open_west_door:
      print("Maybe you should open the door first")
      unlock_west_door()
    else:
      "command is currently unavailable"
      unlock_west_door()
  def west1():
    print("You are at a closed door")
    go_back_east = input(">")
    if "east" in go_back_east:
      stand1()
    elif "use key" in go_back_east:
      if "west key" in inventory:
        unlock_west_door()
        inventory.remove("west key")
      else:
        print ("You do not own the correct item")
        west1()
    if "open" in go_back_east:
      print("You try to open the door, but it is locked. You need a key")
      west1()
    else:
      print ("command is currently unavailable")
      west1()
  def win():
    game_end = time.time()
    print("Congratulations", user_name, "You have beat Quartl")
    score = game_end - game_begin
    score = int(score)
    time.sleep(1)
    print("Your score is",score,"seconds.")
    print("Here's the gamecode for the next game: 338729")
    sys.exit(0)
  def openexit():
    print("You are at the open exit")
    win_ner = input(">")
    if "north" in win_ner:
      newlobby()
    elif "exit" in win_ner:
      win()
    elif "south" in win_ner:
      win()
    else:
      print("this command is currently unavailable")
      openexit()
  def unlock_exit():
    print("You have unlocked the exit")
    open_exit = input(">")
    if "open" in open_exit:
      openexit()
    if "north" in open_exit:
      newlobby()
    else:
      print("command is currently unavailable")
      unlock_exit()
  def south1():
    print("You are at a closed door with a window")
    exit_action = input(">")
    if "use key" in exit_action:
      if "south key" in inventory:
        unlock_exit()
      else:
        print("You do not own the right item")
        south1()
    if "open" in exit_action:
      print ("You try to open the door, but it is locked. You need a key")
      south1()
    if "north" in exit_action:
      stand1()
    if "search window" in exit_action:
      print ("You look through window and see a path leading to a road. This must be the exit.")
      south1() 
    else:
      print("command is currently unavailable")
      south1()
  def north_room_light():
    print("You turn on the lights")
    north_room2()
  def pick_up_key():
    print ("You have picked up the key")
    inventory.append("east key")
    other_side_of_north_room()
  def other_side_of_north_room():
    print ("You are at the other end of the room")
    other_side_of_north_room_actions = input(">")
    if "look" in other_side_of_north_room_actions:
      print ("You look around and see a key on the ground in front of you.")
      other_side_of_north_room()
    elif "pick up key" in other_side_of_north_room_actions:
      pick_up_key()
    elif "use ladder" in other_side_of_north_room_actions:
      north_room()
    else:
      print("command is currently unavailable")
      other_side_of_north_room()
  def north_room_look():
      print("You look but the lights are off and you can barely see anything")
      print ("You make out a light switch right next to you")
      north_room()
  def look_lights_on():
    print ("You look and see a pit filled with spikes in front of you")
    time.sleep(1)
    print ("You see a ladder spanning the gap and what looks like a key on the other side")
    time.sleep(1.5)
    north_room()
  def north_room_pit_trap():
    print ("You fall in a pit filled with spikes and die")
    GameOver()
  def north_room2():
    lights_on = True
    print("You are in the north room")
    north_room_actions2 = input(">")
    if "exit" in north_room_actions2:
      stand1()
    elif "south" in north_room_actions2:
      stand1()
    elif "use lightswitch" in north_room_actions2:
      print("The lights are already on.")
      lights_on = True
      north_room2()
    elif "look" in north_room_actions2:
      if lights_on == False:
        north_room_look()
      if lights_on == True:
        look_lights_on()
    elif "north" in north_room_actions2:
      north_room_pit_trap()
    elif "searh lightswitch" in north_room_actions2:
      print("You search the lightswitch and see that it's a normal lightswitch")
      north_room2()
    elif "use ladder" in north_room_actions2:
      other_side_of_north_room()
    else:
      print ("command is currently unavailable")
      north_room2()
  def north_room():
    lights_on = False
    print("You are in the north room")
    north_room_actions = input(">")
    if "exit" in north_room_actions:
      stand1()
    elif "south" in north_room_actions:
      stand1()
    elif "use lightswitch" in north_room_actions:
      north_room_light()
      lights_on = True
    elif "use light switch" in north_room_actions:
      north_room_light()
      lights_on = True
    elif "look" in north_room_actions:
      if lights_on == False:
        north_room_look()
      if lights_on == True:
        look_lights_on()
    elif "north" in north_room_actions:
      north_room_pit_trap()
    elif "searh lightswitch" in north_room_actions:
      print("You search the lightswitch and see that it's a normal lightswitch")
      north_room()
    elif "use ladder" in north_room_actions:
      other_side_of_north_room()
    else:
      print ("command is currently unavailable")
      north_room()
  def look_in_north_door1():
    print("You look inside the room from the entrance, but the lights are off, and you can't see anything.")
    north1()    
  def north1():
    print ("You are at a open door")
    north_door_entrance = input(">")
    if "north" in north_door_entrance:
      if lights_on == False:
        north_room()
      else:
        north_room2()
    elif "south" in north_door_entrance:
      stand1()
    elif "look" in north_door_entrance:
      look_in_north_door1()
    else:
      print ("command is currently available")
      north1()
  def sit1():
    print( "You are sitting on the floor")
    do_what3 = input(">")
    if "stand" in do_what3:
      stand1()
    elif "lie down" in do_what3:
      Lying_Down1()
    elif "look" in do_what3:
      print("You look around and see 4 doorways, but because your sitting, your can't see much else")
      sit1()
    else:
      sit1()
  def stand1():
    print ("You are now standing in a room.")
    do_what2 = input(">")
    if "sit" in do_what2:
      sit1()
    elif "stand" in do_what2:
      print("You are already standing")
      stand1()  
    elif "lie down" in do_what2:
      Lying_Down1()
    elif "look" in do_what2:
      print("You look around and see an open doorway north, and closed doorways west, east, and south. ")
      stand1()
    elif "north" in do_what2:
      north1()
    elif "east" in do_what2:
      east1()
    elif "west" in do_what2:
      west1()
    elif "south" in do_what2:
      south1()
    else:
      print("command is currently unavailable")
      stand1()
  def Lying_Down1():
    print("You are lying on the floor")
    do_what = input(">")
    if "stand" in do_what:
      stand1()
    elif "sit" in do_what:
      sit1()
    elif "look" in do_what:
      print("You turn your head left and right, and see a doorway on each side.")
      Lying_Down1()
    else:
      print("command is currently unavailable")
      Lying_Down1()
  Lying_Down1()
else:
  print("Okay, maybe next time.")
  b_GameOver()  



