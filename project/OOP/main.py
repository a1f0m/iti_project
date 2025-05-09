from project import Person, Car, Employee, Office

def main():
    cars = {}  # Store cars by name
    employees = {}  # Store employees by ID
    offices = {}  # Store offices by name

    while True:
        print("\n=== Company Management System ===")
        print("1. Create a Car")
        print("2. Create an Employee")
        print("3. Create an Office")
        print("4. Employee Actions")
        print("5. Office Actions")
        print("6. Exit")
        choice = input("Enter choice (1-6): ")

        if choice == "1":
            name = input("Enter car name (e.g., Fiat): ")
            try:
                fuelRate = float(input("Enter fuel rate (0-100): "))
                velocity = float(input("Enter initial velocity (0-200): "))
                cars[name] = Car(name, fuelRate, velocity)
                print(f"Car {name} created.")
            except ValueError:
                print("Invalid input. Use numbers for fuel rate and velocity.")

        elif choice == "2":
            id = input("Enter employee ID (e.g., E001): ")
            name = input("Enter employee name: ")
            try:
                money = float(input("Enter money (e.g., 100): "))
                healthRate = float(input("Enter health rate (0-100): "))
                salary = float(input("Enter salary (e.g., 5000): "))
                distanceToWork = float(input("Enter distance to work (km): "))
            except ValueError:
                print("Invalid input. Use numbers for money, health, salary, distance.")
                continue
            mood = input("Enter mood (e.g., happy, tired, lazy): ")
            email = input("Enter email (e.g., samy@iti.com): ")
            car_name = input("Enter car name (or leave blank for none): ")
            car = cars.get(car_name) if car_name else None
            employees[id] = Employee(name, money, mood, healthRate, id, car, email, salary, distanceToWork)
            print(f"Employee {name} (ID: {id}) created.")

        elif choice == "3":
            name = input("Enter office name (e.g., ITI): ")
            offices[name] = Office(name)
            print(f"Office {name} created.")

        elif choice == "4":
            if not employees:
                print("No employees created yet.")
                continue
            emp_id = input("Enter employee ID: ")
            emp = employees.get(emp_id)
            if not emp:
                print("Employee not found.")
                continue
            print("\nEmployee Actions:")
            print("1. Sleep")
            print("2. Eat")
            print("3. Buy items")
            print("4. Work")
            print("5. Drive")
            print("6. Refuel car")
            print("7. Send email")
            action = input("Enter action (1-7): ")

            try:
                if action == "1":
                    hours = float(input("Enter hours slept: "))
                    emp.sleep(hours)
                elif action == "2":
                    meals = int(input("Enter number of meals (1-3): "))
                    emp.eat(meals)
                elif action == "3":
                    items = int(input("Enter number of items to buy: "))
                    emp.buy(items)
                elif action == "4":
                    hours = float(input("Enter hours worked: "))
                    emp.work(hours)
                elif action == "5":
                    distance = float(input("Enter distance to drive (km): "))
                    velocity = float(input("Enter velocity (km/h): "))
                    emp.drive(distance, velocity)
                elif action == "6":
                    gas = float(input("Enter gas amount to refuel: "))
                    emp.refuel(gas)
                elif action == "7":
                    to = input("Enter recipient email: ")
                    subject = input("Enter subject: ")
                    body = input("Enter email body: ")
                    emp.send_mail(to, subject, body)
                else:
                    print("Invalid action.")
            except ValueError:
                print("Invalid input. Use numbers where required.")

        elif choice == "5":
            if not offices:
                print("No offices created yet.")
                continue
            office_name = input("Enter office name: ")
            office = offices.get(office_name)
            if not office:
                print("Office not found.")
                continue
            print("\nOffice Actions:")
            print("1. Hire employee")
            print("2. Fire employee")
            print("3. Check lateness")
            print("4. Deduct salary")
            print("5. Reward salary")
            print("6. List all employees")
            action = input("Enter action (1-6): ")

            try:
                if action == "1":
                    emp_id = input("Enter employee ID to hire: ")
                    emp = employees.get(emp_id)
                    if emp:
                        office.hire(emp)
                        print(f"Employee {emp_id} hired.")
                    else:
                        print("Employee not found.")
                elif action == "2":
                    emp_id = input("Enter employee ID to fire: ")
                    office.fire(emp_id)
                elif action == "3":
                    emp_id = input("Enter employee ID: ")
                    moveHour = float(input("Enter move hour (e.g., 8.0 for 8 AM): "))
                    velocity = float(input("Enter velocity (km/h): "))
                    is_late = office.calculate_lateness(emp_id, moveHour, velocity)
                    print(f"Employee is {'late' if is_late else 'on time'}.")
                elif action == "4":
                    emp_id = input("Enter employee ID: ")
                    amount = float(input("Enter amount to deduct: "))
                    office.deduct(emp_id, amount)
                elif action == "5":
                    emp_id = input("Enter employee ID: ")
                    amount = float(input("Enter amount to reward: "))
                    office.reward(emp_id, amount)
                elif action == "6":
                    emps = office.get_all_employees()
                    if emps:
                        for emp in emps:
                            print(f"ID: {emp.id}, Name: {emp.name}")
                    else:
                        print("No employees in this office.")
                else:
                    print("Invalid action.")
            except ValueError:
                print("Invalid input. Use numbers where required.")

        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()