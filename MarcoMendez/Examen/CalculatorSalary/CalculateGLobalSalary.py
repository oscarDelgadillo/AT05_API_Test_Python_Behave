def getGlobalSalary(pieces,department):
    auxDepet=str(department)
    if(auxDepet[0].lower() == "c"):
        return float(pieces) * 2.5

def getGlobalSalaryProduct(pieces,department):
    auxDepet = str(department)
    if (auxDepet[0].lower() == "p"):
        return float(pieces) * 2.5
