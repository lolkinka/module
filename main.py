from package.application.salary import calculate_salary
from package.application.db.people import get_employees
from datetime import datetime
if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(datetime.now())