# A simple Makefile example for g++ compiler
# written by I-am-Future

all: piglatin

piglatin: piglatin.o
	g++ -std=c++17 piglatin.o -o piglatin

piglatin.o: piglatin.cpp
	g++ -c -std=c++17 piglatin.cpp -o piglatin.o

# below clean is only valid in Linux/MacOS.
clean:
	rm -f *.o piglatin
