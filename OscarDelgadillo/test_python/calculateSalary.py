import classPerson
import classEmployee

print("Enter quantity of employees: ", end='')
quantity = int(input())

employees = []


def generate_id(index, type_emp):
    if type_emp == "c":
        return "CE_00{0}".format(index + 1)
    else:
        return "PE_00{0}".format(index + 1)


def print_employees():
    print("Employee ID | Name \t | Department \t | Global Salary | Total Discount | Net Salary")
    for x in range(0, len(employees)):
        print(employees[x].get_employee())


if quantity >= 3 and quantity <= 15:
    for x in range(0, quantity):
        print("Enter name: ", end='')
        name = input()
        print("Enter last name:", end='')
        lastname = input()
        print("Enter first letter for the type of employee [comercial = c][production = p]: ", end='')
        type_emp = input()

        if type_emp == 'c':
            print("Enter amount of pieces sell: ", end='')
            pieces_sell = int(input())
            emp_id = generate_id(x, type_emp)
            emp = classEmployee.Employee(emp_id, name, lastname, type_emp, pieces_sell, 0, 0)
            employees.append(emp)

        elif type_emp == 'p':
            print("Enter amount of pieces produced: ")
            pieces_produced = int(input())
            print("Enter amount of pieces defective: ")
            pieces_defective = int(input())
            emp_id = generate_id(x, type_emp)
            emp = classEmployee.Employee(emp_id, name, lastname, type_emp, 0, pieces_produced, pieces_defective)
            employees.append(emp)

print_employees()
