from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today().date())

    @staticmethod
    def new_task():
        user_task = input('Enter task \n')
        user_deadline = input('Enter deadline\n')
        new_row = Task(task=user_task, deadline=datetime.strptime(f'{user_deadline}', '%Y-%m-%d'))
        session.add(new_row)
        session.commit()
        print('The task has been added!')
        main_menu()

    @staticmethod
    def print_date(date):
        today_tasks = session.query(Task).filter(Task.deadline == date).all()
        if len(today_tasks) == 0:
            print('Nothing to do!')
        else:
            counter = 1
            for task in today_tasks:
                print(f"{counter}. {task.task}")
                counter += 1
        print()

    @staticmethod
    def today_tasks():
        print(f"Today {datetime.today().day} {datetime.today().strftime('%b')}")
        Task.print_date(datetime.today())
        main_menu()

    @staticmethod
    def week_tasks():
        week = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: "Saturday", 6: 'Sunday'}
        for i in range(7):
            day = datetime.today().date() + timedelta(days=i)
            print(f"{week[day.weekday()]} {day.day} {day.strftime('%b')}")
            Task.print_date(day)
        main_menu()

    @staticmethod
    def all_tasks():
        print('All tasks:')
        all_tasks = session.query(Task).order_by(Task.deadline).all()
        if len(all_tasks) == 0:
            print('Nothing to do!')
        else:
            counter = 1
            for task in all_tasks:
                print(f"{counter}. {task.task}. {task.deadline.day} {task.deadline.strftime('%b')}")
                counter += 1
            print()
            main_menu()

    @staticmethod
    def missed_tasks():
        miss_task = session.query(Task).filter(Task.deadline < datetime.today().date()).order_by(Task.deadline).all()
        if len(miss_task) == 0:
            print('Nothing is missed!')
        else:
            counter = 1
            for task in miss_task:
                    print(f"{counter}. {task.task} {task.deadline.day} {task.deadline.strftime('%b')}")
                    counter += 1
        print()
        main_menu()

    @staticmethod
    def delete_task():
        print('Choose the number of the task you want to delete:')
        miss_task = session.query(Task).filter(Task.deadline <= datetime.today().date()).order_by(Task.deadline).all()
        if len(miss_task) == 0:
            print('Nothing to delete')
        else:
            counter = 1
            for task in miss_task:
                if task.deadline:
                    print(f"{counter}. {task.task} {task.deadline.day} {task.deadline.strftime('%b')}")
                    counter += 1
            user_choice = int(input())
            delete_row = miss_task[user_choice - 1]
            session.delete(delete_row)
            session.commit()
            print('The task has been deleted!')
        main_menu()


def main_menu():
    print("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit")
    user_input = int(input())
    task = Task()
    if user_input == 1:
        Task.today_tasks()
    elif user_input == 2:
        Task.week_tasks()
    elif user_input == 3:
        Task.all_tasks()
    elif user_input == 4:
        print('Missed tasks:')
        Task.missed_tasks()
    elif user_input == 5:
        Task.new_task()
    elif user_input == 6:
        Task.delete_task()
    elif user_input == 0:
        print('Bye!')
        exit()


Base.metadata.create_all(engine)
main_menu()
