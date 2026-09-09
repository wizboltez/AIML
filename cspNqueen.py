# A CSP is a problem where:

# We have some variables, each variable can take values from a domain, and we need to assign values such that all constraints are satisfied.
# 3 components : 1. variable , 2.domain 3.constraints

# for n queens we have 2 constraint 
# 1. no same column
# 2. no same diagonal
# They are on the same diagonal when:

# |row1 - row2|==|column1 - column2|

# basic mental model :
# Try a value → check whether it is valid → continue if valid → go back if it leads to failure.

# visual flow : 
#                  Start
#                    |
#              Place Queen 1
#               /    |    \
#              /     |     \
#           valid   valid   invalid
#            |
#      Place Queen 2
#        /       \
#     valid     invalid
#       |
#  Place Queen 3
#       |
#    failure
#       |
#    BACKTRACK
#       |
#  Try another position

#for a board 
# index -> row [cause we're palcing one queen in one row ] 
# val -> col

def is_safe(board,row,col): #this is helper function which is used to understand if its safe to place the queen on the particular position
    #here board is the current board position , row is the row where we're wanting to place our queeen, col is the col where we're wanting to place our queeen
    for i in range(row):#we're checking if prev row have any queen and if yes are they troublesome 
        if board[i]==col:
            return False
        if abs(board[i]-col) == abs(i-row):
            return False
    return True
    
    
#backtracking function
def solve_n_queens(board,row,n):#here n is no of queens
    if row==n:#we've placed all n queens
        return True
    for col in range(n):#traverse every possible column for the current row
        if is_safe(board,row,col):
            board[row]=col#assign that row and col to that queen
            
            if solve_n_queens(board,row+1,n):#we've placed current queen -> move to the next queen
                return True 
                # Recursively solve the remaining rows
                # If a complete solution is found, return True
                # Each recursive call is added to the call stack.
                # When a call returns, it is removed from the stack,
                # allowing the previous call to continue.
                
            board[row]=-1#Undo the current assignment because it led to a dead end
    
    return False#no solution possible for current state

def print_board(board,n):
    for row in range(n):
        for col in range(n):
            if board[row]==col:
                print("Q", end=" ")
            else:
                print("-", end=" ")#end() -> print the q or - and stays on the same line
        print()#move to the next line

n=int(input("enter the number of queens : "))
board=[-1]*n# e.x. n=4 -> [-1]*4 -> [-1,-1,-1,-1] which states that there are no queens
if solve_n_queens(board,0,n):
    print("\nsolution : ")
    print_board(board,n)
else:
    print("no solution exists")

        #rough idea of what the tree looks like
        #              Row 0
        #         /      |      \
        #       C0       C1       C2
        #       |        |        |
        #     Row 1    Row 1    Row 1
        #    / | \      / \       |
        #   ×  ×  ×    ×  C3      ...
        #              |
        #            Row 2
        #           /    \
        #          ×      C0
        #                 |
        #               Row 3
        #                 |
        #                C2
        #                 |
        #              SOLUTION

# why n-queens is a csp problem : 
# N-Queens is a Constraint Satisfaction Problem because it consists of
#  variables representing the queen positions, domains representing 
# possible columns for each queen, and constraints ensuring that no two 
# queens share the same column or diagonal.

#constraint propagation -> process of using existing constraints to eliminate values from the domains of variables, thereby reducing the search space