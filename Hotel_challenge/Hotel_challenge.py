def greeting():
    
    guests = ['Amase','Rodgers','Petina','David','Berenice','Kago']
    rooms = [1,2,3,4,5,6]
    chosen={}
    print("Welcome to our hotel!")
    
    for guest in guests:
        print(f"hello {guest}")
        print(f'rooms available {rooms}')
        rooms_input = int(input(f"which room would you want? {guest}"))
        if rooms_input in rooms:
            print(f"Thank you for choosing room {rooms_input}. Enjoy your stay!")
            chosen[guest] = rooms_input
            rooms.remove(rooms_input) 
        else:
            while True:
                print(f"Sorry, room {rooms_input} is already booked. Please choose another room.")
                rooms_input = int(input(f"which room would you want? {guest}"))
                if rooms_input in rooms:
                    print(f"Thank you for choosing room {rooms_input}. Enjoy your stay!")
                    chosen[guest] = rooms_input
                    rooms.remove(rooms_input) 
                    break   
                continue   
                    
    for guest,room_chosen in chosen.items():
        print(f'This guest {guest} has chosen room {room_chosen}')      
             
greeting()


