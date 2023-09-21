import gogographics


def test_move(drawing):
    c = drawing.new_ellipse()
    print(c.centre())
    c.move(100, 100)
    print(c.centre())


gogographics.go(test_move)
