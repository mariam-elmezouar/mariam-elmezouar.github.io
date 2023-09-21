import gogographics


def test_shape2d(drawing):
    print('rectangle centred at point...')
    centre = drawing.get_point()
    r = drawing.new_rectangle()
    r.centre(centre)

    print('ellipse centred at point...')
    centre = drawing.get_point()
    e = drawing.new_ellipse()
    e.centre(centre)

    print('stroke width...')
    drawing.get_point()
    r.stroke_width(5)
    e.stroke_width(1)

    print('stroke colour...')
    drawing.get_point()
    r.stroke((200, 50, 50))
    e.stroke((50, 50, 255))

    print('fill colour...')
    drawing.get_point()
    r.fill((200, 200, 255))
    e.fill((255, 150, 150))

    print('width...')
    drawing.get_point()
    r.width(150)
    e.width(500)

    print('height...')
    drawing.get_point()
    r.height(250)
    e.height(25)

    print('move')
    drawing.get_point()
    e.move(100, 200)
    r.move(-50, -75)

    print('blink...')
    drawing.get_point()
    e.visible(False)
    r.visible(False)
    drawing.pause(100)
    e.visible(True)
    r.visible(True)

    print('chain all....')
    drawing.get_point()
    (r.move(200, -200)
     .visible(False)
     .visible(True)
     .width(1.5*r.width())
     .height(0.75*r.height())
     .fill((250, 250, 75))
     .stroke((50, 50, 100))
     .stroke_width(10)
     .centre((400, 400))
     .move(50, -50))


gogographics.go(test_shape2d)
