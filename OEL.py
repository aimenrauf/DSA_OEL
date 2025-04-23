class Parking_lot_System:
    def __init__(self):
        self.slots = {
    "A": [[None for _ in range(4)] for _ in range(3)],
    "B": [[None for _ in range(4)] for _ in range(3)]
}
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
        print("Welcome to Smart City Parking System")
        print("1. Park a Vehicle")
        print("2. Remove a Vehicle")
        print("3. Show All Parking Slots")
        print("4. Show Available Slots for EVs")
        print("5. Show Priority Vehicles")
        print("6. Exit")
    
    def park(self, zone, level, slot, number, vehicle_type):
        if self.slots[zone][level][slot] is None:
            self.slots[zone][level][slot] = {
                "number": number,
                "type": vehicle_type
            }
            print(f"Vehicle {number} parked at Zone {zone}, Level {level + 1}, Slot {slot + 1}")
        else:
            print("Slot already occupied.")
    def remove(self, zone, level, slot):
        try:
            if self.slots[zone][level][slot] is not None:
                vehicle = self.slots[zone][level][slot]
                print(f"Removing vehicle {vehicle['number']} from Zone {zone}, Level {level + 1}, Slot {slot + 1}")
                self.slots[zone][level][slot] = None
            else:
                print("No vehicle parked in this slot.")
        except (KeyError, IndexError):
            print("Invalid zone, level, or slot! Please check your input.")


system = Parking_lot_System()
system.display()
while (True):
      
    choice = input("Choose Option: ")
        
    if choice == '1':
        zone = input("Enter Zone (A/B): ").upper()         
        level = int(input("Enter Level (1-2): ")) - 1      
        slot = int(input("Enter Slot (1-3): ")) - 1        
        number = input("Enter Vehicle Number: ")           
        vehicle_type = input("Enter Vehicle Type: ")
        system.park(zone,level,slot,number,type)
    elif choice == '2':
        zone = input("Enter Zone (A/B): ").upper()
        level = int(input("Enter Level (1-2): ")) - 1
        slot = int(input("Enter Slot (1-3): ")) - 1
        system.remove(zone,level,slot)
    elif choice == '3':
        system.show_Slots()
    elif choice == '4':
        system.available_Slots()  
    elif choice == '5':
        print("Priority Vehicles:")  
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid Option. Please try again.")           