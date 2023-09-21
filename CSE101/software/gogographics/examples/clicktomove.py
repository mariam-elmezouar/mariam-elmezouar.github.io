import gogographics

STEPS = 60
PAUSE_LENGTH = 500 / STEPS
START_X, START_Y = 70, 45


def click_to_move(drawing):
    ellipse = drawing.new_ellipse()
    ellipse.width(100).height(75).centre((START_X, START_Y))
    ellipse.fill((230, 100, 140)).stroke_width(3).stroke((100, 130, 255))

    while True:
        start_x, start_y = ellipse.centre()
        txt = drawing.new_text().string('Click to move').height(50)

        end_x, end_y = drawing.get_point()
        txt.visible(False)
        dx = (end_x - start_x) / STEPS
        dy = (end_y - start_y) / STEPS

        for _ in range(STEPS):
            ellipse.move(dx, dy)
            drawing.pause(PAUSE_LENGTH)


gogographics.go(click_to_move)
