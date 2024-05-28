import tkinter as tk

class GridApp:
    def __init__(self, root, rows=10, cols=10, cell_size=50):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cell_size = cell_size
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        self.canvas = tk.Canvas(root, width=cols * cell_size, height=rows * cell_size)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        for i in range(self.rows):
            for j in range(self.cols):
                x0 = j * self.cell_size
                y0 = i * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                color = "white" if self.grid[i][j] == 0 else "blue"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

    def on_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        # Toggle the grid cell state
        self.grid[row][col] = 1 if self.grid[row][col] == 0 else 0

        # Pass the coordinates to another function
        self.process_coordinates((row, col))

        # Redraw the grid
        self.draw_grid()

    def process_coordinates(self, coords):
        print(f"Processing coordinates: {coords}")

# Create the main window
root = tk.Tk()
root.title("Real-Time Updating Grid")

# Initialize the GridApp
app = GridApp(root)

# Start the Tkinter event loop
root.mainloop()
