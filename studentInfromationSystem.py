from prettytable import PrettyTable

table = PrettyTable()

table.field_names = ["First Name", "Last Name", "Middle Name", "Subjects","GWA","Equivalent","Status"]

def getAverage(subjects):
    sum = 0
    for subject,score in subjects.items():
        sum += score
    return sum / len(subjects)

def getEquivalent(average):
    if average >= 98:
        return "1.0"
    elif average >= 95:
        return "1.25"
    elif average >= 92:
        return "1.50"
    elif average >= 89:
        return "1.75"
    elif average >= 86:
        return "2.0"
    elif average >= 83:
        return "2.25"
    elif average >= 80:
        return "2.50"
    elif average >= 77:
        return "2.75"
    elif average >= 75:
        return "3.0"
    else:
        return "5.0"
    
def getStatus(Average):
    return "passed" if average >=75 else "failed"

studentInfo = [
    {
    "firstName" : "KRISA MAY",
    "lastName" : "BANDONILL",
    "middleName" : "PALES",
    "subject" : {
        "OOP" : 74,
        "STS" : 75,
        "FL" : 89,
        "PE3" : 97,
        "DSAL" : 77,
    }
    },
    {
    "firstName" : "KING JAMES PHILIP",
    "lastName" : "BELLO",
    "middleName" : "AGUDON",
    "subject" : {
        "OOP" : 87,
        "STS" : 73,
        "FL" : 85,
        "PE3" : 99,
        "DSAL" : 78,
    }
    },
    {
    "firstName" : "APRILLYN MAE",
    "lastName" : "BERBON",
    "middleName" : "PALES",
    "subject" : {
        "OOP" : 88,
        "STS" : 77,
        "FL" : 67,
        "PE3" : 88,
        "DSAL" : 91,
    }
    },
    {
    "firstName" : "Clarissa Mae",
    "lastName" : "Agudon",
    "middleName" : "Pacleba",
    "subject" : {
        "OOP" : 88,
        "STS" : 77,
        "FL" : 67,
        "PE3" : 88,
        "DSAL" : 91,
    }
    }
]
for student in studentInfo:# this looping is for getting individual students data
    table.add_row([
        student["firstName"],
        student["lastName"],
        student["middleName"],
        student["subject"],
        getAverage(student["subject"]),
        "",
        ""
    ])

print(table)