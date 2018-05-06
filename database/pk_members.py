import sqlite3
from member import Member

conn = sqlite3.connect('members.db')

c = conn.cursor()

c.execute("""CREATE TABLE members (
            name text,
            address text,
            phone_number integer,
            age integer,
            interests text
            )""")


def insert_member(member):
    with conn:
        c.execute("INSERT INTO Members VALUES (:name, :address, :phone_number, :age, :interests)",
         {'name': member.name, 'address': member.address, 'phone_number': member.phone_number, 
         'age': member.interests, 'interests': member.interests})

def get_members_by_name(name):
    c.execute("SELECT * FROM Members WHERE name=:name", {'name': name})
    return c.fetchall()


def remove_member(member):
    with conn:
        c.execute("DELETE from Members WHERE first = :first AND last = :last",
                  {'first': member.first, 'last': member.last})

member_1 = Member('Tom Longboat', 'Alberta', 6135772461, 16, 'physics')
member_1 = Member('Kateri Tekakwitha ', 'Alberta', 6135157716, 10, 'arts family love')


insert_member(member_1)
insert_member(member_2)

mem = get_members_by_name('Tom Longboat')
print(mem)

mem = get_members_by_name('Kateri Tekakwitha')
print(mem)

conn.close()