import AddressBook_pb2

person = AddressBook_pb2.Person()
person.id = 123
person.name = "John"
person.email = "john@gmail.com"

phone = person.phones.add()
phone.number = "123-1234"
phone.type = AddressBook_pb2.Person.HOME

print(person.id)


"""
# This is the output we get: #

name: "John"
id: 123
email: "john@gmail.com"
phones {
  number: "123-1234"
  type: HOME
}
"""