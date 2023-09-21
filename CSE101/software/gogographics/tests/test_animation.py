import gogographics


def animate(drawing):
    c = drawing.new_rectangle()
    c.fill((0, 0, 0))
    for _ in range(126):
        c.move(1, 1)
        r, g, b = c.fill()
        c.fill((r + 2, g, b))
        drawing.pause(16)
    for _ in range(50):
        c.move(0, -2)
        drawing.pause(16)


gogographics.go(animate)
