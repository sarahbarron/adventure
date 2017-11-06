from data import locations
# dictionary of directions if we are currently at (1, 1) moving east will result in (1+1,1+0) = (2,1)
directions = {
    'west': (-1, 0),
    'east': (1, 0),
    'north': (0, -1),
    'south': (0, 1),
}

position = (0, 0)  # starting position

while True:
    location = locations[position]  # returns the actual name of our location imported from data so starts at house
    print 'you are at the %s' % location  # prints the location you are currently at

    valid_directions = {}
    for k, v in directions.iteritems():  # k=key v=value.
        possible_position = (position[0] + v[0], position[1] + v[1])  # calcs the new position if we were to go that way
        possible_location = locations.get(possible_position)  # checks if the new position is in locations
        if possible_location:  # if the possible location exists
            print 'to the %s a %s' % (k, possible_location)  # prints the key from directions & location from data
            valid_directions[k] = possible_position  # add the location to a dictionary

    direction = raw_input('which direction do you want to go?\n')  # ask the user for a direction
    position = valid_directions[direction]  # passes the direction to the function
