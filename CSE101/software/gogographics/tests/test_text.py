import gogographics


def test_text(drawing):
    e = drawing.new_ellipse().fill((0, 0, 0)).width(2).height(2).stroke_width(0)

    print('text...')
    drawing.get_point()
    t = drawing.new_text()

    print(f'current centre is {t.centre()}')
    print('move...')
    drawing.get_point()
    t.move(100, 50)

    print(f'new centre is {t.centre()}')
    print('centre')
    drawing.get_point()
    t.centre((50, 50))

    print(f'new centre is {t.centre()}')
    print('string...')
    drawing.get_point()
    t.string('a much longer string than truly necessary')

    print('fill...')
    drawing.get_point()
    t.fill((250, 175, 175))

    print('typeface...')
    drawing.get_point()
    t.typeface('Times')


gogographics.go(test_text)
