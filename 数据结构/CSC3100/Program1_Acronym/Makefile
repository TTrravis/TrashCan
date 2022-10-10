# A simple Makefile example for g++ compiler
# written by I-am-Future

all: acronym

acronym: acronym.o
	g++ -std=c++17 acronym.o -o acronym

acronym.o: acronym.cpp
	g++ -c -std=c++17 acronym.cpp -o acronym.o

# below clean is only valid in Linux/MacOS.
clean:
	rm -f *.o acronym
