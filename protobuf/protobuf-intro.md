# Intro to Protobuf
Protocol buffers is a way of packetizing data developed by Google. It allows us to have a common protocol to transmit some data between programs. It is written in C++ but has support for other languages such as python!

## Compiling the proto file into a python class
Sample command: `protoc -I. --python_out=. .\AddressBook.proto`
Where:
* `-I` is the directory we search for dependencies.
* --python_out is where the pythono object will be created. (could be --cpp_out depending on the language).
* path to the proto file we want to compile.

## References:
* https://www.freecodecamp.org/news/googles-protocol-buffers-in-python/
