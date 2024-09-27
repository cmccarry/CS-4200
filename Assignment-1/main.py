import tkinter as tk
from tkinter import messagebox

class EightQueensGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("8-Queens Problem")
        self.board_size = 8
        self.all_solutions = []
        self.shown_solutions = []
        self.current_solution_index = 0

        self.board = [[0 for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.create_widgets()
        self.find_all_solutions()
        self.show_solution(0)

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, padx=10)

        # Label for showing total number of solutions
        self.solution_count_label = tk.Label(self.frame, text="Total Solutions: 0")
        self.solution_count_label.pack()

        # Listbox for displaying shown solutions
        self.solution_listbox = tk.Listbox(self.frame, height=10, width=20)
        self.solution_listbox.pack(side=tk.LEFT)

        # Button to go to the next solution
        self.next_button = tk.Button(self.frame, text="Next Solution", command=self.next_solution)
        self.next_button.pack(pady=5)

        # Button to go to the previous solution
        self.prev_button = tk.Button(self.frame, text="Previous Solution", command=self.prev_solution)
        self.prev_button.pack(pady=5)

        # Canvas for the chessboard
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack(side=tk.RIGHT)

        self.draw_board()

    def draw_board(self):
        cell_size = 400 // self.board_size
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "gray"
                x1 = col * cell_size
                y1 = row * cell_size
                x2 = x1 + cell_size
                y2 = y1 + cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def draw_queens(self, solution):
        cell_size = 400 // self.board_size
        self.canvas.delete("queen")  # Clear previous queens
        for row in range(self.board_size):
            col = solution[row] - 1  # Convert to 0-indexed
            x1 = col * cell_size + 10
            y1 = row * cell_size + 10
            x2 = (col + 1) * cell_size - 10
            y2 = (row + 1) * cell_size - 10
            self.canvas.create_oval(x1, y1, x2, y2, fill="red", tags="queen")

    def is_safe(self, board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve_n_queens_util(self, row, board):
        if row == self.board_size:
            self.all_solutions.append(board[:])  # Store a copy of the board state
            return

        for col in range(1, self.board_size + 1):
            if self.is_safe(board, row, col):
                board[row] = col
                self.solve_n_queens_util(row + 1, board)

    def find_all_solutions(self):
        board = [0] * self.board_size
        self.solve_n_queens_util(0, board)

    def show_solution(self, index):
        if self.all_solutions:
            solution = self.all_solutions[index]
            self.draw_queens(solution)
            if index >= len(self.shown_solutions):
                self.shown_solutions.append(solution)
                self.add_solution_to_list(solution)

    def add_solution_to_list(self, solution):
        # Convert solution to string and add it to the listbox
        solution_str = str(solution)
        self.solution_listbox.insert(tk.END, solution_str)
        self.solution_count_label.config(text=f"Total Solutions: {len(self.shown_solutions)}")

    def next_solution(self):
        if self.current_solution_index < len(self.all_solutions) - 1:
            self.current_solution_index += 1
            self.show_solution(self.current_solution_index)

    def prev_solution(self):
        if self.current_solution_index > 0:
            self.current_solution_index -= 1
            self.show_solution(self.current_solution_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = EightQueensGUI(root)
    root.mainloop()
