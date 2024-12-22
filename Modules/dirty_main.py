from application.salary import *
from application.db.people import *
from datetime import datetime

def main():
    print(f"Текущая дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()