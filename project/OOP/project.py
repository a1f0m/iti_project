class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50

    def buy(self, items):
        if items == 0:
            print('No items bought')
        for i in range(items):
            if self.money < 0:
                print(f'Bought {items} items')
                break
            else:
                self.money -= 10
        print(f'Bought {items} ')

class Car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate     
        self.velocity = velocity

    def run(self, velocity, distance):
        if not 0 <= velocity <= 200:
            print("Velocity must be between 0 and 200 km/h")
            return
        self.velocity = velocity
        if self.fuelRate >= distance:
            self.fuelRate -= distance
            self.stop(0)
        else:
            traveled = self.fuelRate
            self.fuelRate = 0
            remaining = distance - traveled
            self.stop(remaining)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"Out of fuel, {remaining_distance} km left")
        else:
            print("Arrived!")

class Employee(Person):
    def __init__(self, name, money, mood, healthRate, id, car, email, salary, distanceToWork):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance, velocity):
        if self.car:
            self.car.run(velocity, distance)

    def refuel(self, gasAmount):
        if self.car:
            self.car.fuelRate += gasAmount
            if self.car.fuelRate > 100:
                self.car.fuelRate = 100

    def send_mail(self, to, subject, body):
        print(f"From: {self.email}\nTo: {to}\nSubject: {subject}\n{body}")

class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empid):
        for emp in self.employees:
            if emp.id == empid:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, empid):
        emp = self.get_employee(empid)
        if emp:
            self.employees.remove(emp)

    def calculate_lateness(self, empid, moveHour, velocity):
        emp = self.get_employee(empid)
        if not emp:
            return False
        distance = emp.distanceToWork
        if velocity <= 0:
            return True
        time_to_work = distance / velocity
        arrival_time = moveHour + time_to_work
        return arrival_time > 9

    def deduct(self, empid, amount):
        emp = self.get_employee(empid)
        if emp:
            emp.salary -= amount

    def reward(self, empid, amount):
        emp = self.get_employee(empid)
        if emp:
            emp.salary += amount