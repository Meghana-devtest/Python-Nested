def dataretrival(Employee_details):
    for key, value in Employee_details.items():
        if type(value) is dict:
            dataretrival(value)
        else:
            print(key, ":", value)

Employee_details = {"meghana": {"employee_id": 1234},"abc": {"employee_id": 2345}}

dataretrival(Employee_details)
dataretrival(Employee_details['meghana'])
print(dataretrival(Employee_details['meghana']))
