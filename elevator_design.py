Build an Elevator class and implement the following two methods:

Method 1: void pressButton(int startFloor, int endFloor, Direction direction)
This method is called when a person presses the elevator button. 
For example, if I want to go from floor 1 to floor 15, I’ll call pressButton(1, 15, Direction.UP). 
When I want to go home for the day, I'll call pressButton(15, 1, Direction.DOWN)

Method 2: int nextFloor();
This method is called when we want to get/move to the next floor the elevator will visit.

Note: This Elevator’s behavior is simple and efficient. While the Elevator is going up, it should 
stop at all the floors necessary to transfer people who are going up. 
When the Elevator has done all that it can do, it should change directions 
and stop at all the floors necessary to transfer people who are going down. 
This isn't a First-In-First-Out solution.
"""
# Sample 1
# If the elevator is currently on floor 5, and heading in Direction.UP:
# pressButton(5, 8, Direction.UP)
# pressButton(6, 10, Direction.UP)
# nextFloor() // returns 6
# nextFloor() // returns 8
# nextFloor() // returns 10


# Sample 2
# If the elevator is currently on floor 5, and heading in Direction.UP:
# pressButton(5, 8, Direction.UP)
# pressButton(7, 3, Direction.DOWN)
# pressButton(6, 10, Direction.UP)
# nextFloor() // returns 6, dir.UP 
# nextFloor() // returns 7, dir.UP
# nextFloor() // returns 8, dir.UP
# nextFloor() // returns 10, dir.DOWN
# nextFloor() // returns 3

class Elevator:
  
  def __init__(self, start_floor, end_floor, direction):
    self.start_floor = start_floor
    self.end_floor = end_floor
    self.requested_floors_UP = set()
    self.requested_floors_DOWN = set()
    self.current_direction = direction
    
  # making the requests
  def pressButton(self, start_floor, end_floor, direction):
    if direction == 'UP':
      self.requested_floors_UP.add((start_floor, end_floor)) # (s, end) - (5,7)
    
    else:
      self.requested_floors_DOWN.add((start_floor, end_floor))
    
  def nextFloor(self):
    
    if current_direction == 'UP':
    while self.requested_floors: # (5,7), (6,8), (10, 12)
      next_floor = min(self.requested_floors, key=self.get_closest_floor)
      self.requested_floors.discard(next_floor) # we have visted this 
      return next_floor
      
  def get_closest_floor(self, floor):
    return abs(self.start_floor - floor)
    
  
  
    
  
  


## work on this
