import heapq
class Parking_lot_System:
    def __init__(self):
        self.slots = {
            "A": [[None for _ in range(4)] for _ in range(3)],
            "B": [[None for _ in range(4)] for _ in range(3)]
        }
        self.pqueue = []  
        self.location = {}  
        self.priorityQueue()

    def priorityQueue(self):
        for zone in ['A', 'B']:
            for level in range(len(self.slots[zone])):
                for slot in range(len(self.slots[zone][level])):
                    priority = 1 if zone == 'A' else 2
                    heapq.heappush(self.pqueue, (priority, zone, level, slot))

    def show_Slots(self):
        for zone in self.slots:  
            print(f"\nZone {zone} Status:")
            for level in range(len(self.slots[zone])):
                for slot in range(len(self.slots[zone][level])):
                    data = self.slots[zone][level][slot]
                    if data:
                        print(f"  Level {level+1}, Slot {slot+1} => {data['number']} ({data['type']})")
                    else:
                        print(f"  Level {level+1}, Slot {slot+1} => Available")

    def available_Slots(self):
        for zone in self.slots:  
            print(f"\nAvailable slots in Zone {zone}:")
            available = False
            for level in range(len(self.slots[zone])):
                for slot in range(len(self.slots[zone][level])):
                    if self.slots[zone][level][slot] is None:
                        print(f"  Level {level + 1}, Slot {slot + 1} is available")
                        available = True
            if not available:
                print("No available slots in this zone.")

    def display(self):
        print("\nWelcome to Smart City Parking System")
        print("1. Park a Vehicle")
        print("2. Remove a Vehicle")
        print("3. Show All Parking Slots")
        print("4. Show Available Slots")
        print("5. Show Priority Vehicles")
        print("6. Exit")

    def park(self, number, type):
        if not self.pqueue:
            print("Parking lot is full!")
            return       
        priority, zone, level, slot = heapq.heappop(self.pqueue)
        self.slots[zone][level][slot] = {
            "number": number,
            "type": type
        }
        self.location[number] = (zone, level, slot)
        print(f"Vehicle {number} parked at Zone {zone}, Level {level + 1}, Slot {slot + 1}")

    def remove(self, number):
        if number not in self.location:
            print("Vehicle not found!")
            return       
        zone, level, slot = self.location[number]
        print(f"Removing vehicle {number} from Zone {zone}, Level {level + 1}, Slot {slot + 1}")
        self.slots[zone][level][slot] = None
        priority = 1 if zone == 'A' else 2
        heapq.heappush(self.pqueue, (priority, zone, level, slot))
        del self.location[number]

    def priority_vehicles(self):
        print("\nPriority Vehicles (Zone A):")
        found = False
        for level in range(len(self.slots['A'])):
            for slot in range(len(self.slots['A'][level])):
                data = self.slots['A'][level][slot]
                if data:
                    print(f"  {data['number']} ({data['type']}) at Level {level+1}, Slot {slot+1}")
                    found = True
        if not found:
            print("No priority vehicles parked.")

system = Parking_lot_System()
while True:
    system.display()
    choice = input("\nChoose Option: ")   
    if choice == '1':
        number = input("Enter Vehicle Number: ")
        type = input("Enter Vehicle Type: ")
        system.park(number, type)
    elif choice == '2':
        number = input("Enter Vehicle Number to Remove: ")
        system.remove(number)
    elif choice == '3':
        system.show_Slots()
    elif choice == '4':
        system.available_Slots()
    elif choice == '5':
        system.priority_vehicles()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Option. Please try again.")
