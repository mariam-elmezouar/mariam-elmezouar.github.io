import gogographics


def fading(drawing):
    level = 0
    t = drawing.new_text().string("Help, I'm fading!")
    t.fill((level, level, level))
    for _ in range(51):
        drawing.pause(40)
        level = level + 5
        t.fill((level, level, level))


gogographics.go(fading)
