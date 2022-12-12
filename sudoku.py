import pygame

bg_color = (0, 0, 0)  # (255, 255, 255)
font_color = (0, 255, 255)
grid_color = (0, 255, 0)
input_color = (255, 215, 0)

grid = [[1, 5, 0, 0, 0, 0, 0, 0, 0],
        [3, 9, 6, 2, 1, 0, 0, 0, 0],
        [0, 0, 4, 0, 5, 3, 1, 0, 6],
        [4, 1, 0, 9, 0, 2, 0, 7, 8],
        [7, 0, 3, 0, 0, 5, 4, 0, 8],
        [0, 0, 8, 3, 0, 0, 5, 6, 1],
        [0, 0, 0, 0, 3, 0, 0, 8, 0],
        [8, 3, 0, 6, 0, 0, 2, 0, 0],
        [0, 4, 0, 0, 0, 7, 0, 1, 3]]
sd_grid = [[1, 5, 0, 0, 0, 0, 0, 0, 0],
           [3, 9, 6, 2, 1, 0, 0, 0, 0],
           [0, 0, 4, 0, 5, 3, 1, 0, 6],
           [4, 1, 0, 9, 0, 2, 0, 7, 8],
           [7, 0, 3, 0, 0, 5, 4, 0, 8],
           [0, 0, 8, 3, 0, 0, 5, 6, 1],
           [0, 0, 0, 0, 3, 0, 0, 8, 0],
           [8, 3, 0, 6, 0, 0, 2, 0, 0],
           [0, 4, 0, 0, 0, 7, 0, 1, 3]]


# function to check that input number is valid or not
def search(mat, a, b, val):
    if a < 3:
        if b < 3:
            a, b = 0, 0
        elif 3 <= b < 6:
            a, b = 0, 3
        elif 6 <= b < 9:
            a, b = 0, 6
    elif 3 <= a < 6:
        if b < 3:
            a, b = 3, 0
        elif 3 <= b < 6:
            a, b = 3, 3
        elif 6 <= b < 9:
            a, b = 3, 6
    elif a >= 6:
        if b < 3:
            a, b = 6, 0
        elif 3 <= b < 6:
            a, b = 6, 3
        elif 6 <= b < 9:
            a, b = 6, 6

    x, y = a + 3, b + 3
    while a < x:
        b = y - 3
        while b < y:
            if mat[a][b] == val:
                return False
            b += 1
        a += 1
    return True


def check(mat, i, j, val):
    if val in mat[i]:
        return False
    a = 0
    while a < 9:
        if val == mat[a][j]:
            return False
        a += 1
    return search(mat, i, j, val)
    # if i < 3:
    #     if j < 3:
    #         return search(mat, 0, 0, val)
    #     elif 3 <= j < 6:
    #         return search(mat, 0, 3, val)
    #     elif j > 5:
    #         return search(mat, 0, 6, val)
    # elif 3 <= i < 6:
    #     if j < 3:
    #         return search(mat, 3, 0, val)
    #     elif 3 <= j < 6:
    #         return search(mat, 3, 3, val)
    #     elif j > 5:
    #         return search(mat, 3, 6, val)
    # elif i > 5:
    #     if j < 3:
    #         return search(mat, 5, 0, val)
    #     elif 3 <= j < 6:
    #         return search(mat, 5, 3, val)
    #     elif j > 5:
    #         return search(mat, 5, 6, val)


# For input
def insert(screen, position):
    myfont = pygame.font.SysFont('Comic Sans MS', 35)
    buffer = 5

    while True:
        i, j = position[1], position[0]
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if grid[i - 1][j - 1] != 0:
                    return

                # backspace button to delete a input
                if event.key == pygame.K_BACKSPACE:
                    pygame.draw.rect(screen, bg_color,
                                     (j * 50 + buffer, i * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                    sd_grid[i - 1][j - 1] = 0
                    pygame.display.update()
                    return
                if 1 <= event.key - 48 <= 9:

                    # to show input in red color if input is wrong one

                    ans = check(sd_grid, i - 1, j - 1, event.key - 48)
                    if ans:

                        pygame.draw.rect(screen, bg_color,
                                         (j * 50 + buffer, i * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        value = myfont.render(str(event.key - 48), True, input_color)
                        sd_grid[i - 1][j - 1] = event.key - 48
                        screen.blit(value, (j * 50 + 2 * buffer, i * 50))
                        pygame.display.update()
                    else:
                        pygame.draw.rect(screen, bg_color, (
                            j * 50 + buffer, i * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                        value = myfont.render(str(event.key - 48), True, (255, 0, 0))
                        sd_grid[i - 1][j - 1] = event.key - 48
                        screen.blit(value, (j * 50 + 2 * buffer, i * 50))
                        pygame.display.update()
                # x = 0
                # while x < 9:
                #     y = 0
                #     while y < 9:
                #         if sd_grid[x][y] != 0:
                #             ans = check(sd_grid, x, y, sd_grid[x][y])
                #             if ans:
                #                 pygame.draw.rect(screen, bg_color,
                #                                  ((x + 1) * 50 + buffer, (x + 1) * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
                #                 value = myfont.render(str(sd_grid[x][y]), True, input_color)
                #                 screen.blit(value, ((x + 1) * 50 + 2 * buffer, (x + 1) * 50))
                #                 pygame.display.update()
                #             else:
                #                 pygame.draw.rect(screen, bg_color,
                #                                  ((x + 1) * 50 + buffer, (x + 1) * 50 + buffer, 50 - 2 * buffer,
                #                                   50 - 2 * buffer))
                #                 value = myfont.render(str(sd_grid[x][y]), True, (255, 0, 0))
                #                 screen.blit(value, ((x + 1) * 50 + 2 * buffer, (x + 1) * 50))
                #                 pygame.display.update()
                #         y += 1
                #     x += 1

                return


def sudoku():
    pygame.font.init()

    screen = pygame.display.set_mode((550, 550))

    # code below is for icon, it's commmented becuase you will have to download the image
    # img = pygame.image.load("download.jpg")
    # pygame.display.set_icon(img)

    screen.fill(bg_color)
    pygame.display.set_caption("SUDOKU")

    myfont = pygame.font.SysFont('Comic Sans MS', 35)

    # screen.fill(251, 247, 245)
    x = 0
    z = 0

    diff = 500 / 9

    for i in range(10):
        if i % 3 == 0:
            pygame.draw.line(screen, grid_color, (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pygame.draw.line(screen, grid_color, (50, 50 + 50 * i), (500, 50 + 50 * i), 5)

        else:
            pygame.draw.line(screen, grid_color, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
            pygame.draw.line(screen, grid_color, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)

    pygame.display.update()

    # plotting numbers

    for i in range(0, 9):
        for j in range(0, 9):
            if 10 > grid[i][j] > 0:
                value = myfont.render(str(grid[i][j]), True, font_color)
                screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()

    while True:
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                insert(screen, (pos[0] // 50, pos[1] // 50))

            if event.type == pygame.QUIT:
                print(sd_grid)
                pygame.quit()
                return


sudoku()
