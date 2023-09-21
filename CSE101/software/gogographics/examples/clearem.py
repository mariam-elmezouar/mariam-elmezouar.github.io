import math

import gogographics
from bounce import bounce

BALL_RADIUS = 28
BALL_COLOUR = (204, 0, 0)
POST_RADIUS = 16
POST_COLOUR = (120, 120, 120)
ROWS = 6
BOTTOM_ROW_HEIGHT = 120
ROW_SEPARATION = 50
COLUMNS = 6
GRAVITY = -1.5
TICK_MS = 30
START_HEIGHT = 750
BALLS_USED_COLOUR = (25, 25, 175)
POSTS_LEFT_COLOUR = (25, 175, 25)
GO_COLOUR = (125, 25, 125)


def make_posts(drawing):
    posts = []
    for row_index in range(ROWS):
        for col_index in range(COLUMNS):
            post = drawing.new_ellipse().height(2 * POST_RADIUS).width(2 * POST_RADIUS)
            x = 800 / COLUMNS * (col_index + 0.25 + 0.5 * (row_index % 2))
            y = BOTTOM_ROW_HEIGHT + row_index * 2 * ROW_SEPARATION
            post.centre((x, y))
            post.stroke_width(0).fill(POST_COLOUR)
            posts.append(post)
    return posts


def clearem(drawing):
    posts = make_posts(drawing)
    balls_used = 0
    ball = (drawing.new_ellipse().visible(False)
            .height(2 * BALL_RADIUS).width(2 * BALL_RADIUS).
            stroke_width(0).fill(BALL_COLOUR))
    drawing.new_text().string('balls used').fill(BALLS_USED_COLOUR).centre((725, 770))
    balls_used_display = (drawing.new_text().string(balls_used).fill(BALLS_USED_COLOUR)
                          .centre((725, 725)).height(50))
    drawing.new_text().string('posts left').fill(POSTS_LEFT_COLOUR).centre((75, 770))
    posts_remaining_display = (drawing.new_text().string(len(posts)).fill(POSTS_LEFT_COLOUR)
                               .centre((75, 725)).height(50))
    go_display = drawing.new_text().string('go go!').fill(GO_COLOUR).height(200).centre((400, 450))

    while posts:
        go_display.visible(True)
        launch_x, _ = drawing.get_point()
        go_display.visible(False)
        ball.visible(True)
        balls_used += 1
        balls_used_display.string(balls_used)
        ball.centre((launch_x, START_HEIGHT))
        ball.visible(True)
        vx = vy = 0
        while ball.centre()[1] > -BALL_RADIUS:
            vy = vy + GRAVITY
            ball.move(vx, vy)
            bx, by = ball.centre()
            if bx < BALL_RADIUS or bx > 800 - BALL_RADIUS:
                vx = -vx
                bx = BALL_RADIUS if bx < BALL_RADIUS else 800 - BALL_RADIUS
                ball.centre((bx, by))
            for post in posts:
                px, py = post.centre()
                distance = math.sqrt((bx - px) ** 2 + (by - py) ** 2)
                if distance < BALL_RADIUS + POST_RADIUS:
                    vx, vy = bounce(ball, vx, vy, post)
                    posts.remove(post)
                    post.visible(False)
                    posts_remaining_display.string(len(posts))
            drawing.pause(TICK_MS)
    (drawing.new_text().string(f'cleared in {balls_used} balls!')
     .fill(GO_COLOUR).centre((400, 450)).height(60))


gogographics.go(clearem)
