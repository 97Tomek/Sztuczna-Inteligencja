from copy import deepcopy
from os import system, name
from time import sleep
from random import randint

class Board:
    def __init__(self, board, fork_pos, palete_pos, fruit_pos, electro_pos, cloth_pos):
        self.board = deepcopy(board)
        self.fork_x = int(fork_pos[0])
        self.fork_y = int(fork_pos[1])
        self.palete_x = int(palete_pos[0])
        self.palete_y = int(palete_pos[1])
        self.fruit_x = int(fruit_pos[0])
        self.fruit_y = int(fruit_pos[1])
        self.electro_x = int(electro_pos[0])
        self.electro_y = int(electro_pos[1])
        self.cloth_x = int(cloth_pos[0])
        self.cloth_y = int(cloth_pos[1])

        self.board[self.fork_x][self.fork_y] = "X"
        self.board[self.palete_x][self.palete_y] = "P"
        self.board[self.fruit_x][self.fruit_y] = "F"
        self.board[self.electro_x][self.electro_y] = "E"
        self.board[self.cloth_x][self.cloth_y] = "C"

        for line_index, line in enumerate(self.board):
            for elem_index, elem in enumerate(line):
                self.board[line_index][elem_index] = str(self.board[line_index][elem_index])

    def drawBoard(self):
        for line in self.board:
            print(line)

    def move(self, path):
        fruit = (self.fruit_x, self.fruit_y)
        palette = (self.palete_x, self.palete_y)
        electronics = (self.electro_x, self.electro_y)
        clothes = (self.cloth_x, self.cloth_y)
        for step in path:
            spot = (self.fork_x,  self.fork_y)
            if spot == fruit:
                self.board[spot[0]][spot[1]] = "F"
            elif spot == palette:
                self.board[self.fork_x][self.fork_y] = "P"
            elif spot == clothes:
                self.board[self.fork_x][self.fork_y] = "C"
            elif spot == electronics:
                self.board[self.fork_x][self.fork_y] = "E"
            else:
                self.board[self.fork_x][self.fork_y] = "0"
            self.fork_x = step[0]
            self.fork_y = step[1]
            self.board[self.fork_x][self.fork_y] = "X"
            clear()
            self.drawBoard()
            sleep(0.5)


class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def generate():
    how_many = 1
    szklo = ["tak", "nie"]
    uelektroniczne = ["tak", "nie"]
    waga = [1, 2, 3]
    ksztalt = ["plaski", "prostopadloscienny", "okragly", "podluzny"]
    faktura = ["gladka", "chropowata"]
    kolor = ["zolty", "zielony", "czarny", "fioletowy", "brazawy", "rozowy", "bialy", "srebrny"]
    objects = list()

    for i in range(1, how_many + 1):
        objects.append(str("szklo(" + "o" + str(i) + "," + str(szklo[randint(0, len(szklo) - 1)]) + ")."))
        objects.append(str("uelektroniczne(" + "o" + str(i) + "," + str(uelektroniczne[randint(0, len(uelektroniczne) - 1)]) + ")."))
        objects.append(str("waga(" + "o" + str(i) + "," + str(waga[randint(0, len(waga) - 1)]) + ")."))
        objects.append(str("ksztalt(" + "o" + str(i) + "," + str(ksztalt[randint(0, len(ksztalt) - 1)]) + ")."))
        objects.append(str("faktura(" + "o" + str(i) + "," + str(faktura[randint(0, len(faktura) - 1)]) + ")."))
        objects.append(str("kolor(" + "o" + str(i) + "," + str(kolor[randint(0, len(kolor) - 1)]) + ")."))
    objects.sort()
    return objects


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    #start = (0, 0)
    #end = (7, 6)
    hasItem = False
    recognizedItem = False
    fruits = list()
    clothes = list()
    electronics = list()

    #fork_pos = tuple(map(int, input("Input the forklift initial position as a tuple: ").split(',')))
    #palete_pos = tuple(map(int, input("Input the palette initial position as a tuple: ").split(',')))
    #fruit_pos = tuple(map(int, input("Input the fruits initial position as a tuple: ").split(',')))
    #electro_pos = tuple(map(int, input("Input the electronics initial position as a tuple: ").split(',')))
    #cloth_pos = tuple(map(int, input("Input the clothes initial position as a tuple: ").split(',')))
    #board = Board(maze, fork_pos, palete_pos, fruit_pos, electro_pos, cloth_pos)


    iterations = int(input("Enter the number of iterations: "))
    board = Board(maze, (5, 4), (9, 0), (0, 0), (0, 9), (9, 9))
    board.drawBoard()
    destinations = [(board.fruit_x, board.fruit_y), (board.cloth_x, board.cloth_y), (board.electro_x, board.electro_y)]
    while iterations:
        if not hasItem:
            start = (board.fork_x, board.fork_y)
            end = (board.palete_x, board.palete_y)
            path = astar(maze, start, end)
            board.move(path)
            item = generate()
            print(item)
            sleep(2)
            hasItem = True

        if hasItem and not recognizedItem:
            destination = destinations[randint(0, len(destinations) - 1)]
            print("Driving to: " + str(destination))
            sleep(2)
            start = (board.fork_x, board.fork_y)
            end = (destination[0], destination[1])
            path = astar(maze, start, end)
            board.move(path)
            hasItem = False
            print("Siedzi")
            sleep(2)
        iterations -= 1

    #path = astar(maze, start, end)
    #print(path)
    #board.move(path)


if __name__ == '__main__':
    main()
