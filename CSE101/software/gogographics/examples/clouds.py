import gogographics

GREY = (220, 230, 240)


def get_sunny(drawing):
    (drawing.new_rectangle().centre((400, 400)).width(800).height(800)
     .fill((103, 157, 202)).stroke_width(0))
    (drawing.new_rectangle().centre((400, 100)).width(800).height(200)
     .fill((103, 193, 53)).stroke_width(0))
    sun = (drawing.new_ellipse().visible(False).centre((300, 500)).width(125).height(125)
           .fill((255, 255, 20))).stroke_width(2).stroke((253, 128, 8))
    clouds = [
        (drawing.new_ellipse().visible(False).centre((200, 540)).fill(GREY)
         .height(180).width(200).stroke_width(0)),
        (drawing.new_ellipse().visible(False).centre((340, 470)).fill(GREY)
         .height(100).width(400).stroke_width(0)),
        (drawing.new_ellipse().visible(False).centre((390, 600)).fill(GREY)
         .height(250).width(340).stroke_width(0)),
        (drawing.new_ellipse().visible(False).centre((510, 500)).fill(GREY)
         .height(100).width(100).stroke_width(0))
    ]
    sun.visible(True)
    for cloud in clouds:
        cloud.visible(True)

    invite = drawing.new_text().string('Click to animate').fill((255, 255, 10))
    drawing.get_point()
    invite.visible(False)

    stepx = 6
    stepy = 1.5
    for _ in range(140):
        for cloud in clouds:
            cloud.move(stepx, stepy)
        drawing.pause(30)

    drawing.new_text().string('Done').fill((255, 255, 10))


gogographics.go(get_sunny)
