class Member:
    def __init__(self, name, plan):
        self.name = name
        self.plan = plan
        self.check_ins = 0

    def show_member(self):
        print('Name: ' + self.name + ' | Plan: ' + self.plan + ' | Check-ins: ' + str(self.check_ins))

    def check_in(self):
        self.check_ins += 1


members = []

try:
    with open ('members.txt', 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            loaded_member = Member(parts[0],parts[1])
            loaded_member.check_ins = int(parts[2])
            members.append(loaded_member)
except FileNotFoundError:
    print('No saved members yet')


for member in members:
    member.show_member()

choice = 2
while choice != 4:
    print('1. Add member')
    print('2. View members')
    print('3. Check in member')
    print('4. Exit')
    try:
        choice = int(input('What do you need assistance with? '))
    except ValueError:
        print('Please enter a number.')
    else:
        if choice == 2:
            for member in members:
                member.show_member()
        elif choice == 1:
            member_name = input('What is your name? ')
            member_plan = input('What is the plan? ')
            new_member = Member(member_name,member_plan)
            members.append(new_member)
        elif choice == 3:
            check_name = input('What is the name? ')
            found = False
            for member in members:
                if member.name == check_name:
                    found = True
                    member.check_in()
            if not found:
                print('Member not found')
        elif choice == 4:
            with open('members.txt', 'w') as file:
                for member in members:
                    file.write(member.name + ',' + member.plan + ',' + str(member.check_ins) + '\n')
            print('Goodbye')
        else:
            print('That option doesnt exist')