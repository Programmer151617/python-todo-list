import pygame
import random
import sys

# Configuration
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10

# Colors
ALIVE_COLOR = (0, 255, 0)
DEAD_COLOR = (10, 10, 10)
GRID_COLOR = (40, 40, 40)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

# Grid state
def create_grid(randomize=False):
    return [[random.choice([0, 1]) if randomize else 0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid(grid):
    screen.fill(DEAD_COLOR)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1)
            color = ALIVE_COLOR if grid[y][x] else DEAD_COLOR
            pygame.draw.rect(screen, color, rect)
    pygame.display.flip()

def count_neighbors(grid, x, y):
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx) % GRID_WIDTH, (y + dy) % GRID_HEIGHT
            count += grid[ny][nx]
    return count

def update_grid(grid):
    new_grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x] == 1:
                new_grid[y][x] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[y][x] = 1 if neighbors == 3 else 0
    return new_grid

# Main game loop
def main():
    grid = create_grid(randomize=True)
    paused = False

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_c:
                    grid = create_grid(randomize=False)
                elif event.key == pygame.K_r:
                    grid = create_grid(randomize=True)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                x, y = mx // CELL_SIZE, my // CELL_SIZE
                grid[y][x] = 1 - grid[y][x]  # Toggle cell

        if not paused:
            grid = update_grid(grid)

        draw_grid(grid)

if __name__ == "__main__":
    main()
