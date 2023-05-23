
from proj08 import by_dev

print("Dictionary from games_clean_small.csv")
master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
              'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                  'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                      'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                          'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                              'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                  'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']]}



dev = 'Valve'
print("Developer:",dev)
instructor = ['Artifact', 'Dota 2', 'Counter-Strike: Global Offensive']
print("Instructor:")
print(instructor)
student = by_dev(master_D,dev)
print("Student:")
print(student)

assert student == instructor
print("\n"+"-"*20)
print("Dictionary from games_medium.csv")
master_D = {'Grand Theft Auto V': ['13/04/2015', ['Rockstar North'], ['Action', 'Adventure'], 1, 0.0, 'Positive', 349924, 78, ['win_support']], \
              'DayZ': ['13/12/2018', ['Bohemia Interactive'], ['Action', 'Adventure', 'Massively Multiplayer'], 0, 33.588, 'Positive', 55690, 87, ['win_support']], \
                  'Bloons TD 6': ['17/12/2018', ['Ninja Kiwi'], ['Strategy'], 1, 5.268, 'Positive', 442, 90, ['win_support', 'mac_support']], \
                      'Counter-Strike: Global Offensive': ['21/08/2012', ['Valve', 'Hidden Path Entertainment'], ['Action', 'Free to Play'], 0, 0.0, 'Positive', 6774812, 88, ['win_support', 'mac_support', 'lin_support']], \
                          'Dota 2': ['9/7/2013', ['Valve'], ['Action', 'Free to Play', 'Strategy'], 0, 0.0, 'Positive', 1885261, 82, ['win_support', 'mac_support', 'lin_support']], \
                              'Artifact': ['28/11/2018', ['Valve'], ['Strategy'], 1, 3.588, 'Positive', 309, 71, ['win_support']], \
                                  'SkiFy': ['24/01/2018', ['Blup Games'], ['Casual', 'Indie', 'Simulation'], 1, 0.504, 'Mixed', 18, 55, ['win_support']], \
                                      'X3: Terran Conflict': ['16/10/2006', ['Egosoft'], ['Action', 'Simulation', 'Strategy'], 1, 6.228, 'Positive', 2801, 95, ['win_support', 'mac_support', 'lin_support']], \
                                          'X3: Reunion': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 4.428, 'Positive', 57, 84, ['win_support', 'mac_support', 'lin_support']], \
                                              'X2: The Threat': ['21/07/2006', ['Egosoft'], ['Strategy'], 1, 3.108, 'Positive', 2506, 86, ['win_support']]}



dev = 'Egosoft'
print("Developer:",dev)
instructor = ['X3: Terran Conflict', 'X3: Reunion', 'X2: The Threat']
print("Instructor:")
print(instructor)
student = by_dev(master_D,dev)
print("Student:")
print(student)

assert student == instructor