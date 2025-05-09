
# OOP-Based Company System

This project demonstrates a simple object-oriented Python application that simulates interactions between persons, employees, cars, and office management. It includes class relationships, encapsulation, and behavior modeling.

---

## Classes Overview

### 1. `Person`
Represents a general person with attributes for name, money, mood, and health. Includes methods to simulate common actions.

#### Methods:
- `sleep(hours)`: Updates mood based on hours of sleep.
- `eat(meals)`: Sets health rate depending on meals consumed.
- `buy(items)`: Deducts money when purchasing items and handles conditions for item buying.

---

### 2. `Car`
Represents a vehicle with fuel and velocity attributes. Supports traveling behavior.

#### Methods:
- `run(velocity, distance)`: Simulates running the car at a given speed over a distance, considering fuel limits.
- `stop(remaining_distance)`: Stops the car and reports whether the destination was reached or fuel ran out.

---

### 3. `Employee` (Inherits from `Person`)
Extends `Person` to include employee-specific information and actions.

#### Attributes:
- `id`, `car`, `email`, `salary`, `distanceToWork`

#### Methods:
- `work(hours)`: Updates mood based on work hours.
- `drive(distance, velocity)`: Drives the assigned car to a distance.
- `refuel(gasAmount)`: Refuels the car, ensuring the fuel doesn't exceed 100%.
- `send_mail(to, subject, body)`: Simulates sending an email from the employee.

---

### 4. `Office`
Manages a list of employees and provides methods for common office operations.

#### Methods:
- `get_all_employees()`: Returns all employees in the office.
- `get_employee(empid)`: Finds an employee by ID.
- `hire(employee)`: Adds an employee to the office.
- `fire(empid)`: Removes an employee by ID.
- `calculate_lateness(empid, moveHour, velocity)`: Determines if an employee is late based on travel time and speed.
- `deduct(empid, amount)`: Deducts a salary penalty.
- `reward(empid, amount)`: Rewards an employee by increasing salary.

---

## Purpose

This code can be used for:
- Learning and practicing object-oriented programming concepts.
- Simulating basic interactions in a company setting.
- Understanding class inheritance and real-world behavior mapping.


