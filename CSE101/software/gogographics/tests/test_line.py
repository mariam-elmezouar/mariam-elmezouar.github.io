import gogographics


def test_line(drawing):
    print('new line')
    line = drawing.new_line()
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('move centre')
    line.centre((100, 700))
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('change start and end')
    line.start((100, 200)).end((600, 700))
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('move')
    line.move(-50, 200)
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('stroke')
    line.stroke((100, 150, 100))
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('stoke width')
    line.stroke_width(10)
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('end')
    line.end((790, 600))
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('length')
    line.length(400)
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('start and end')
    line.start((700, 100)).end((100, 700))
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')

    print('length')
    line.length(300)
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')
    drawing.get_point()

    print('all chained')
    line.length(100).start((100, 200)).end((200, 300)).stroke((75, 75, 255)).stroke_width(6).move(100, 100).length(500)
    print(f'{line.start()=}, {line.end()=}, {line.length()=}')

    drawing.new_text().string('done')


gogographics.go(test_line)
