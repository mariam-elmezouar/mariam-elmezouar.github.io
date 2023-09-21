import math

# 0.8 is about the bounciness of a good silicone rubber ball
ELASTICITY = 0.8


def bounce(ball, vx, vy, post):
    """
    Because the ball moves discretely, it may actually be overlapping
    the post position when a collision occurs. So, two phases: first,
    compute where the ball would have first touched the post, based on
    its velocity, and reset the ball's centre to there. Second, compute
    the new velocity by computing the collision line (tangent to the
    point where the balls touch), the angle of incidence to that line
    based on the ball's velocity, and the reflection line.

    There is an analytic solution for determining where the ball first
    touched the post. Here we use a computational approximation: move the ball
    backwards along its velocity line until it's before the post, then
    move it forward and backward in successively smaller increments until
    it's within one pixel of the post.
    """
    # reset ball position
    r = ball.width() / 2 + post.width() / 2
    bx, by = ball.centre()
    px, py = post.centre()
    d = math.sqrt((bx - px) ** 2 + (by - py) ** 2)
    v_mag = math.sqrt(vx ** 2 + vy ** 2)
    scale = 4
    while abs(d - r) > 1:
        bx = bx - scale * r * vx / v_mag
        by = by - scale * r * vy / v_mag
        d = math.sqrt((bx - px) ** 2 + (by - py) ** 2)
        scale = -0.5 * abs(scale) if d > r else 0.5 * abs(scale)
    ball.centre((bx, by))
    # compute bounce
    collision_line = math.atan2(py - by, px - bx) + math.pi / 2
    v_angle = math.atan2(vy, vx)
    incidence = v_angle - collision_line + math.pi
    reflection = (v_angle - 2 * incidence) % (2 * math.pi)
    bounce_magnitude = math.sqrt((vx ** 2 + vy ** 2)) * ELASTICITY
    vx = bounce_magnitude * math.cos(reflection)
    vy = bounce_magnitude * math.sin(reflection)
    return vx, vy
