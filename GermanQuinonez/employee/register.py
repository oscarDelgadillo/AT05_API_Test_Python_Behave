list_employees = []

from employee import Employee


def input_employee():
    print("Select the kind of employee :")
    print("1 :Commmercial")
    print("2 :Production:")
    kind = int(input())
    if kind == 1:
        print("Enter name")
        name = input()
        print("Enter last name")
        last_name = input()
        print("Enter User ID")
        user_id = input()
        employee = Employee(name, last_name, user_id, "Commercial")
        print("Enter total sum of pieces send")
        total = int(input())
        employee.set_total_sum_of_pieces_send(total)
        return employee
    else:
        print("Enter name")
        name = input()
        print("Enter last name")
        last_name = input()
        print("Enter User ID")
        user_id = input()
        employee = Employee(name, last_name, user_id, "Production")
        print("Enter total effective")
        total = int(input())
        employee.set_amount_of_effective_pieces(total)
        print("Enter total defective")
        total = int(input())
        employee.set_amount_of_defective_pieces(total)
        return employee


def employees():
    """
    This function asks to the user the number of employees
    """
    print("Enter the number of employees")
    number = int(input())
    if number > 3 & number < 13:
        for i in range(number):
            list_employees.append(input_employee())


def print_employees():
    print("Employee ID | Name | Deparment | Global Salary | Total Discount | Net Salary")
    for i in list_employees:
        print((f'{i.get_id()} | {i.get_name()}| {i.get_global_salary()} | {i.get_discount()} | {i.get_net_salary()}'))

employees()
print_employees()
