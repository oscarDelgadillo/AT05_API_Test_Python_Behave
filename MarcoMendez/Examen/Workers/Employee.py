import re

from Examen.Workers.Person import Person
from Examen.CalculatorSalary.CalculateDiscount import discountSalary
from Examen.CalculatorSalary.CalculateGLobalSalary import getGlobalSalary, getGlobalSalaryProduct
from Examen.CalculatorSalary.CalculateNetSalary import netSalary

import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# create a file handler
handler = logging.FileHandler('aplicacion.log')
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)




class Employee(Person):
    def __init__(self,name):
        Person.__init__(self, name)
        self.EmployeeId = ""
        self.Departmet = ""
        self.GlobalSalary = ""
        self.TotalDiscount = ""
        self.NetSalry = ""
        self.RegisterEmployye = {}

    # def __init__(self, name, department, globalSalary,employeeId,totalDiscount,netSalary):
    #     Person.__init__(self,name)
    #     self.EmployeeId = employeeId
    #     self.Departmet = department
    #     self.GlobalSalary = globalSalary
    #     self.TotalDiscount = totalDiscount
    #     self.NetSalry = netSalary
    #     self.RegisterEmployye = {}


    logger.info('Metod - register employee ')
    # register Employee in a dictonary
    def registerEmployee(self):
        acount=int(input("cantidad de empleados"))
        if(acount >=3 and acount<=15):
            i = 0
            while(i<acount):
                name = input(" inserte user name")
                employeeId = input(" inserte un UserId")
                department = input("Inserte un Departmento *comercial *produccion ")
                pieces = input("inserte las piesas")
                expreUserId = re.compile("[0-9]{0,3}$")
                result = str(expreUserId.match(employeeId))
                if (str(department)[0].lower() == 'c' and result != 'None'):
                    globalSalary =float(getGlobalSalary(float(pieces),str(department)))
                    discount= float(discountSalary(globalSalary))
                    netSalario = float(netSalary(globalSalary,discount))
                    self.RegisterEmployye["CE_"+employeeId] = "Name :" +name + "|" +"Department " +str(department) + "|" + "Global Salary"+str(globalSalary)\
                                                              + "|" + " Total Discount "+ str(discount)\
                                                              + "|" +"Net Salary"+ str(netSalario)

                if (str(department)[0].lower() == 'p' and result != 'None'):
                    globalSalary = float(getGlobalSalaryProduct(float(pieces), str(department)))
                    discount = float(discountSalary(globalSalary))
                    netSalario = float(netSalary(globalSalary, discount))
                    self.RegisterEmployye["CE_" + employeeId] = "Name :" + name + "|" + "Department " + str(
                        department) + "|" + "Global Salary" + str(globalSalary) \
                                                                + "|" + " Total Discount " + str(discount) \
                                                                + "|" + "Net Salary" + str(netSalario)
                    logger.info("empleado guardado correctamente")
                i += 1

        else:
            print("La cantidad de empleados tiene que ser mayor a 3 y menor 15  incorrectamente")


    def getResult(self):
        print(self.RegisterEmployye)