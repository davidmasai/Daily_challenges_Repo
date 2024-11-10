biodata = {'Lewis Hamilton': 'Mercedes', 'Max Verstappen': 'RedBull', 'Lando Norris': 'McLaren','Charles Leclerc':'Ferrari','Alpine':'Esteban Ocon','Aston Martin':'Sebastian Vettel','Williams':'Alex Albon','Kick Sauber':'Valtteri Bottas','HAAS':'Mick Schumacher','RB':'Yuki Tsunoda'}


def passkeys():
    # This function takes the password of each driver to authenticate during raceday
    global biodata
    
    password = {} # storage for all passwords
    
    print("It's 3 days to Raceday! Each driver will need to be authenticated to race.")
    
    print('The following drivers are present:')
    
    for driver, brand in biodata.items():
        print(f'{driver} racing for {brand}')
        
    print('Select a passcode to authenticate driver during raceday:')
    
    for driver in biodata.keys():
        keyword = input(f'{driver} passcode: ')
        password[driver] = keyword
        
    return password

def raceday():
    
    global biodata
    password = passkeys()
    racers = []
    
    for driver, passkey in password.items():
        attempts = 0
        authenticated = False
        
        while attempts < 4:
            
            passcode = input(f'What is the passcode for {driver}: ').lower()
            attempts += 1
            if passcode == passkey:
                print('Driver can race'.upper())
                racers.append(driver)
                authenticated = True
                break
                
            else:
                print('Try again, or race again next race day'.upper())
                

        if not authenticated:
            print(f'{driver} failed authentication test and cannot race'.upper())

    print('Drivers racing this weekend are:')
    for char in racers:
        print(char)
        
raceday()