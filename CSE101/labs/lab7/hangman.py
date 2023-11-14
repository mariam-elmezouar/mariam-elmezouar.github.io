import gogographics
import math
from randomword import random_word

LTRS = 'abcdefghijklmnopqrstuvwxyz'
WDTH = 750 / len(LTRS) * 2
HGHT = WDTH*1.5

# Constants for the scaffold drawing
BASE_HEIGHT = 400  # Higher base height for guesses and letters
SCAFFOLD_HEIGHT = 350  # The height of the scaffold from the base
OVERHANG_WIDTH = 100  # The overhang of the top beam
LEFT_PADDING = 550 # Padding from the left of the canvas
ROPE_LENGTH = 80  # Longer rope so it's clearly visible

# Scaffold coordinates
# Scaffold Base
base_start_x = LEFT_PADDING
base_end_x = base_start_x + OVERHANG_WIDTH
base_y = BASE_HEIGHT

# Scaffold Pillar
pillar_x = base_start_x + OVERHANG_WIDTH // 2
pillar_top_y = BASE_HEIGHT + SCAFFOLD_HEIGHT
pillar_bottom_y = BASE_HEIGHT

# Scaffold Top Beam
beam_start_x = pillar_x
beam_end_x = pillar_x - OVERHANG_WIDTH
beam_y = pillar_top_y

# Scaffold Rope
rope_x = beam_end_x
rope_start_y = beam_y
rope_end_y = beam_y - ROPE_LENGTH  # The rope should hang down from the top beam

SCAFFOLD_COORDS = [
    (base_start_x, base_y, base_end_x, base_y),  # Base
    (pillar_x, pillar_bottom_y, pillar_x, pillar_top_y),  # Pillar
    (beam_start_x, beam_y, beam_end_x, beam_y),  # Top Beam
    (rope_x, rope_start_y, rope_x, rope_end_y),  # Rope
]



def setup_scaffold(drawing):
    # Drawing scaffold
    for coord in SCAFFOLD_COORDS:
        line = drawing.new_line().start(coord[:2]).end(coord[2:])
        line.stroke_width(15).stroke((128, 64, 0))



def setup_body(drawing):
    #sizes for the body parts
    HEAD_RADIUS = 20  
    BODY_LENGTH = 80  
    ARM_LENGTH = 40  
    LEG_LENGTH = 60  
    ARM_ANGLE = 45  
    LEG_ANGLE = 45  

    # Coordinates for the body parts
    # Head (ellipse)
    head_centre_x = rope_x
    head_centre_y = rope_end_y - HEAD_RADIUS

    # Body (line)
    body_start_x = head_centre_x
    body_start_y = head_centre_y - HEAD_RADIUS
    body_end_x = body_start_x
    body_end_y = body_start_y - BODY_LENGTH

    # Arms (lines)
    arm_offset_x = ARM_LENGTH * math.cos(math.radians(ARM_ANGLE))
    arm_offset_y = ARM_LENGTH * math.sin(math.radians(ARM_ANGLE))

    # Legs (lines)
    leg_offset_x = LEG_LENGTH * math.cos(math.radians(LEG_ANGLE))
    leg_offset_y = LEG_LENGTH * math.sin(math.radians(LEG_ANGLE))

    body_parts = {
        'head': drawing.new_ellipse().centre((head_centre_x, head_centre_y)).width(HEAD_RADIUS * 2).height(HEAD_RADIUS * 2)
                                      .fill((204, 26, 26)).stroke_width(0).visible(False),
        'body': drawing.new_line().start((body_start_x, body_start_y)).end((body_end_x, body_end_y))
                                      .stroke_width(15).stroke((204, 26, 26)).visible(False),
        'left_arm': drawing.new_line().start((body_start_x, body_start_y - (BODY_LENGTH / 4))).end((body_start_x - arm_offset_x, body_start_y - (BODY_LENGTH / 4) - arm_offset_y))
                                      .stroke_width(15).stroke((204, 26, 26)).visible(False),
        'right_arm': drawing.new_line().start((body_start_x, body_start_y - (BODY_LENGTH / 4))).end((body_start_x + arm_offset_x, body_start_y - (BODY_LENGTH / 4) - arm_offset_y))
                                      .stroke_width(15).stroke((204, 26, 26)).visible(False),
        'left_leg': drawing.new_line().start((body_end_x, body_end_y)).end((body_end_x - leg_offset_x, body_end_y - leg_offset_y))
                                      .stroke_width(15).stroke((204, 26, 26)).visible(False),
        'right_leg': drawing.new_line().start((body_end_x, body_end_y)).end((body_end_x + leg_offset_x, body_end_y - leg_offset_y))
                                      .stroke_width(15).stroke((204, 26, 26)).visible(False),
    }

    return body_parts

def setup_letters(drawing):
    letters = []
    for idx in range(1, len(LTRS)+1):
        ctr = [((idx - 1) % 13 + 1.5) * WDTH - 50, (1 - ((idx - 1) // 13)) * HGHT + 0.5 * HGHT]
        letter = drawing.new_text().string(LTRS[idx-1]).fill((0, 150, 0)).centre(ctr).height(45)
        letters.append(letter)
    return letters

def setup_random_word(drawing):
    rand_word = random_word()
    for ix in range(1, len(rand_word)+1):
        ln = drawing.new_line().stroke_width(7).stroke((0, 0, 0)).length(WDTH * 0.7)  # Set line length based on WDTH
        x = ((13 - len(rand_word)) / 2 - 0.5 + ix) * WDTH
        ln.start([x, HGHT * 3]).end([x+25, HGHT * 3])  # Set the center of the line
    return rand_word

def hangman_game(drawing):
    setup_scaffold(drawing)
    body_parts = setup_body(drawing)
    letters = setup_letters(drawing)
    rand_word = setup_random_word(drawing)

    # Game play logic goes here
    # ...



# Run the game
gogographics.go(hangman_game)
