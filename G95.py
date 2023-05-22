#BFS 
graph = {
 'A' : ['B','C','D'],
 'B' : ['E'],
 'C' : ['D','F'],
 'D' : [],
 'E' : [],
 'F' : []
}
visited = [] # List to keep track of visited nodes.
queue = [] #Initialize a queue
def bfs(visited, graph, node):
 visited.append(node)
 queue.append(node)
 while queue:
 s = queue.pop(0)
 print (s, end = " ")
 for neighbour in graph[s]:
 if neighbour not in visited:
 visited.append(neighbour)
 queue.append(neighbour)
# Driver Code
print("Following is the Path using Breadth-First Search")
bfs(visited, graph, 'A')


#DFS

graph = {
'5' : ['3','7'],
'3' : ['2', '4'],
'7' : ['8'],
'2' : [],
'4' : ['8'],
'8' : []
}
visited = set() # Set to keep track of visited nodes of graph.
def dfs(visited, graph, node): #function for dfs
if node not in visited:
print (node)
visited.add(node)
for neighbour in graph[node]:
dfs(visited, graph, neighbour)
# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')



# Define a dictionary of common problems and their solutions
problem_dict = {
"Printer not working": "Check that it's turned on and connected to the network",
"Can't log in": "Make sure you're using the correct username and password",
"Software not installing": "Check that your computer meets the system requirements",
"Internet connection not working": "Restart your modem or router",
"Email not sending": "Check that you're using the correct email server settings"
}
# Define a function to handle user requests
def handle_request(user_input):
if user_input.lower() == "exit":
return "Goodbye!"
elif user_input in problem_dict:
return problem_dict[user_input]
else:
return "I'm sorry, I don't know how to help with that problem."
# Main loop to prompt user for input
while True:
user_input = input("What's the problem? Type 'exit' to quit. ")
response = handle_request(user_input)
print(response)


#Selection Sort
x = []
n = int(input("Enter how many elements you want for sorting"))
for i in range(n):
print("Enter list elements")
a = int(input(""))
x.append(a)
print("unsorted Elements list is: ", x)
for i in range(0,len(x)-1):
for j in range(i+1,len(x)):
if x[i]>x[j]:
c=x[i]
x[i]=x[j]
x[j]=c
print("Sorted Elements List is: ",x)


#ChatBot

def greet(bot_name, birth_year):
print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
def remind_name():
print('Please, remind me your name.')
name = input()
print("What a great name you have, {0}!".format(name))
def guess_age():
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is {0}; that's a good time to start programming!".format(age))
def count():
print('Now I will prove to you that I can count to any number you want.')
num = int(input())
counter = 0
while counter <= num:
print("{0} !".format(counter))
counter += 1
def test():
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
answer = 2
guess = int(input())
while guess != answer:
print("Please, try again.")
guess = int(input())
print('Completed, have a nice day!')
print('.................................')
print('.................................')
print('.................................')
def end():
print('Congratulations, have a nice day!')
print('.................................')
print('.................................')
print('.................................')
input()
greet('TE-Chatbot', '2022') # change it as you need
remind_name()
guess_age()
count()
test()
end()


#a_star_algorithm

from collections import deque
class Graph:
# example of adjacency list (or rather map)
# adjacency_list = {
# 'A': [('B', 1), ('C', 3), ('D', 7)],
# 'B': [('D', 5)],
# 'C': [('D', 12)]
# }
def __init__(self, adjacency_list):
self.adjacency_list = adjacency_list
def get_neighbors(self, v):
return self.adjacency_list[v]
# heuristic function with equal values for all nodes
def h(self, n):
H = {
'A': 1,
'B': 1,
'C': 1,
'D': 1
}
return H[n]
def a_star_algorithm(self, start_node, stop_node):
# open_list is a list of nodes which have been visited, but who's neighbors
# haven't all been inspected, starts off with the start node
# closed_list is a list of nodes which have been visited
# and who's neighbors have been inspected
open_list = set([start_node])
closed_list = set([])
# g contains current distances from start_node to all other nodes
# the default value (if it's not found in the map) is +infinity
g = {}
g[start_node] = 0
# parents contains an adjacency map of all nodes
parents = {}
parents[start_node] = start_node
while len(open_list) > 0:
n = None
# find a node with the lowest value of f() - evaluation function
for v in open_list:
if n == None or g[v] + self.h(v) < g[n] + self.h(n):
n = v;
if n == None:
print('Path does not exist!')
return None
# if the current node is the stop_node
# then we begin reconstructin the path from it to the start_node
if n == stop_node:
reconst_path = []
while parents[n] != n:
reconst_path.append(n)
n = parents[n]
reconst_path.append(start_node)
reconst_path.reverse()
print('Path found: {}'.format(reconst_path))
return reconst_path
# for all neighbors of the current node do
for (m, weight) in self.get_neighbors(n):
# if the current node isn't in both open_list and closed_list
# add it to open_list and note n as it's parent
if m not in open_list and m not in closed_list:
open_list.add(m)
parents[m] = n
g[m] = g[n] + weight
# otherwise, check if it's quicker to first visit n, then m
# and if it is, update parent data and g data
# and if the node was in the closed_list, move it to open_list
else:
if g[m] > g[n] + weight:
g[m] = g[n] + weight
parents[m] = n
if m in closed_list:
closed_list.remove(m)
open_list.add(m)
# remove n from the open_list, and add it to closed_list
# because all of his neighbors were inspected
open_list.remove(n)
closed_list.add(n)
print('Path does not exist!')
return None
adjacency_list = {
'A': [('B', 1), ('C', 3), ('D', 7)],
'B': [('D', 5)],
'C': [('D', 12)]
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')



#N Queen

n = int(input("Enter the value for n\n"))
board = [[0 for i in range(n)] for i in range(n)]
def check_column(board, row, column):
for i in range(row, -1, -1):
if board[i][column] == 1:
return False
return True
def check_diagonal(board, row, column):
for i, j, in zip(range(row, -1, -1), range(column, -1, -1)):
if board[i][j] == 1:
return False
for i, j, in zip(range(row, -1, -1), range(column, n)):
if board[i][j] == 1:
return False
return True
def nqn(board, row):
if row == n:
return True
for i in range(n):
if (check_column(board, row, i) == True and check_diagonal(board, row, i) == True):
board[row][i] = 1
if nqn(board, row + 1):
return True
board[row][i] = 0
return False
nqn(board, 0)
for row in board:
print(row)
