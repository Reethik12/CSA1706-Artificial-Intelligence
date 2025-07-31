#8 Puzzle problem
from collections import deque
goal_state = [[1,2,3],[4,5,6],[7,8,0]]
moves = [(-1,0),(1,0),(0,-1),(0,1)]
def board_to_tuple(board):
    return tuple(tuple(row) for row in board)
def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return (i, j)
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3
def solve_puzzle(start_board):
    visited = set()
    queue = deque()
    queue.append((start_board, 0))
    while queue:
        board, moves_count = queue.popleft()
        if board == goal_state:
            return moves_count
        visited.add(board_to_tuple(board))
        x, y = find_zero(board)
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                new_board = [row[:] for row in board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                board_tuple = board_to_tuple(new_board)
                if board_tuple not in visited:
                    queue.append((new_board, moves_count + 1))
    return -1

start = [[1,2,3],[4,0,6],[7,5,8]]
steps = solve_puzzle(start)
print("Minimum moves to solve the puzzle:", steps)
