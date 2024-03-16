TARGET = proj1
LIBS = -lgmp
CC = gcc
CFLAGS = -g -Wall -Wextra -pedantic -O0

.PHONY: clean all default

default: $(TARGET)
all: default

OBJECTS := $(patsubst %.c, %.o, $(wildcard *.c))
HEADERS := $(wildcard *.h)

%.o: %.c $(HEADERS)
	$(CC) $(CFLAGS) -c $< -o $@

.PRECIOUS: $(TARGET) $(OBJECTS)

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -Wall $(LIBS) -o $@

clean:
	-rm -f *.o
	-rm -f $(TARGET)