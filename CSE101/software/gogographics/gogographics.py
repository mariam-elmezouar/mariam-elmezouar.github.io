"""
GoGoGraphics

A graphics library created for the Royal Military College of Canada course
CSE/INF101, supporting the display and animation of rectangles, ellipses,
lines and text. A minimal program is:

```
    import gogographics

    def minimal(drawing):
        drawing.new_ellipse()

    gogographics.go(minimal)
```

Implementation note: GoGoGraphics is built on top of the tkinter Canvas but
controls it "from the outside", i.e. from a separate thread. Reaching into
tkinter for Canvas object properties from the outside is subject to race
conditions, slow, or both, so GoGoGraphics stores duplicate properties in
its own Shape objects.

Copyright His Majesty in right of Canada, 2023. Unlimited use permitted within
the Government of Canada; all other use subject to the GNU General Public
License version 3.0 https://www.gnu.org/licenses/gpl-3.0.en.html

Version 1.01, 2023-05-16, by Greg Phillips

"""

import math
import tkinter as tk
from abc import ABC, abstractmethod
from queue import Queue
from threading import Thread, Lock
from time import sleep
from typing import Sequence

DRAWING_SIZE = 800
DEFAULT_SHAPE_SIZE = 50
X0 = Y0 = (DRAWING_SIZE - DEFAULT_SHAPE_SIZE) / 2
X1 = Y1 = (DRAWING_SIZE + DEFAULT_SHAPE_SIZE) / 2
DEFAULT_BBOX = (X0, Y0, X1, Y1)
DEFAULT_FILL = (204, 204, 204)
DEFAULT_STROKE = (76, 76, 76)
DEFAULT_STROKE_WIDTH = 1
DEFAULT_LINE_WIDTH = 2

DEFAULT_TEXT_HEIGHT = 24
DEFAULT_STRING = 'default text'


class Drawing(tk.Frame):

    def __init__(self, master):
        super().__init__(master=master)
        self.canvas = tk.Canvas(width=DRAWING_SIZE, height=DRAWING_SIZE,
                                background='white', borderwidth=0, highlightthickness=0)
        self.canvas.grid(row=0, column=0)
        self.__lock = Lock()
        self.__queue = Queue()
        self.__awaiting_click = False
        self.canvas.bind('<Button-1>', self.__handle_click)

    # ----- Internal-only methods -----

    def __handle_click(self, event):
        if self.__awaiting_click:
            self.__awaiting_click = False
            self.__queue.put((event.x, event.y))

    def __new_shape(self, shape):
        self.__lock.acquire()

        def create_shape():
            shape.make()
            shape.initialize()
            self.__lock.release()

        self.after_idle(create_shape)
        self.__lock.acquire()
        self.__lock.release()
        return shape

    @staticmethod
    def __rgb_to_hex_string(rgb):
        r, g, b = [int(max(0, min(255, n))) for n in rgb]
        return f'#{r:02x}{g:02x}{b:02x}'

    @staticmethod
    def __hex_string_to_rgb(hex_string):
        return [int(hex_string[n:n + 2], 16) for n in [1, 3, 5]]

    @staticmethod
    def __flip_vertical(bbox):
        x0, y0, x1, y1 = bbox
        return x0, DRAWING_SIZE - y0, x1, DRAWING_SIZE - y1

    # ----- Readable attributes

    @property
    def width(self):
        return self.canvas.winfo_width()

    @property
    def height(self):
        return self.canvas.winfo_height()

    # ----- Methods for direct client programmer use

    def get_point(self):
        self.__awaiting_click = True
        x, y = self.__queue.get()
        return x, DRAWING_SIZE - y

    def new_line(self):
        return self.__new_shape(Line(self))

    def new_ellipse(self):
        return self.__new_shape(Ellipse(self))

    def new_rectangle(self):
        return self.__new_shape(Rectangle(self))

    def new_text(self):
        return self.__new_shape(Text(self))

    @staticmethod
    def pause(ms):
        sleep(ms / 1000)

    # ---- Methods for use by shape objects -----

    def make_rectangle(self, bbox):
        return self.canvas.create_rectangle(*self.__flip_vertical(bbox))

    def make_ellipse(self, bbox):
        return self.canvas.create_oval(*self.__flip_vertical(bbox))

    def make_line(self, bbox):
        return self.canvas.create_line(*self.__flip_vertical(bbox))

    def make_text(self, x, y):
        return self.canvas.create_text(x, y, justify=tk.CENTER)

    def move(self, _id, dx, dy):
        self.canvas.move(_id, dx, -dy)

    def set_visible(self, _id, visibility):
        self.canvas.itemconfig(_id, state=tk.NORMAL if visibility else tk.HIDDEN)

    def set_fill(self, _id, rgb):
        self.canvas.itemconfig(_id, fill=self.__rgb_to_hex_string(rgb))

    def set_stroke(self, _id, rgb):
        self.canvas.itemconfig(_id, outline=self.__rgb_to_hex_string(rgb))

    def set_stroke_width(self, _id, width):
        self.canvas.itemconfig(_id, width=width)

    def set_bbox(self, _id, bbox):
        self.canvas.coords(_id, self.__flip_vertical(bbox))

    def set_string(self, _id, string):
        self.canvas.itemconfig(_id, text=string)

    def set_font(self, _id, font):
        self.canvas.itemconfig(_id, font=font)


# ---- Parameter errors ----

class GoGoParameterError(Exception):

    def __init__(self, thing, value, required):
        super().__init__(f'\n\n  The parameter to "{thing}" must be {required}.\n  You provided {value}.')


def requires_boolean(thing, value):
    if not isinstance(value, bool):
        raise GoGoParameterError(thing, value, 'a boolean value (True or False)')


def requires_positive_number(thing, value):
    if not isinstance(value, int | float) or value < 0:
        raise GoGoParameterError(thing, value, 'a positive number')


def requires_two_numbers(thing, first, second):
    if not isinstance(first, int | float) or not isinstance(second, int | float):
        raise GoGoParameterError(thing, f'{first} and {second}', 'two numbers')


def requires_point(thing, value):
    if (not isinstance(value, Sequence) or not len(value) == 2
            or not isinstance(value[0], int | float) or not isinstance(value[1], int | float)):
        raise GoGoParameterError(thing, value, 'a point, consisting of two numbers')


def requires_colour(thing, value):
    if (not isinstance(value, Sequence) or not len(value) == 3
            or not isinstance(value[0], int | float) or not 0 <= value[0] <= 255
            or not isinstance(value[1], int | float) or not 0 <= value[1] <= 255
            or not isinstance(value[2], int | float) or not 0 <= value[2] <= 255):
        raise GoGoParameterError(thing, value, 'a colour, consisting of three numbers between 0 and 255')


def requires_string(thing, value):
    """tkinter converts anything to a character string"""
    pass


# ---- Shapes ----

class Shape(ABC):

    def __init__(self, drawing):
        self.drawing = drawing
        self._id = None
        self._visible = True
        self._bbox = DEFAULT_BBOX

    @abstractmethod
    def make(self):
        pass

    @abstractmethod
    def initialize(self):
        pass

    def _set_or_get(self, thing, value, validator):
        if value is not None:
            validator(thing, value)
            self.__setattr__(f'_{thing}', value)
            self.drawing.__getattribute__(f'set_{thing}')(self._id, value)
            return self
        else:
            return self.__getattribute__(f'_{thing}')

    def move(self, dx, dy):
        requires_two_numbers('move', dx, dy)
        x0, y0, x1, y1 = self._bbox
        self._bbox = (x0 + dx, y0 + dy, x1 + dx, y1 + dy)
        self.drawing.set_bbox(self._id, self._bbox)
        return self

    def visible(self, value=None):
        return self._set_or_get('visible', value, requires_boolean)

    def _geometry(self, thing, value, validator):
        if value is not None:
            validator(thing, value)
            self.__setattr__(f'_{thing}', value)
            self.drawing.set_bbox(self._id, self._bbox)
            return self
        else:
            return self.__getattribute__(f'_{thing}')

    def centre(self, point=None):
        return self._geometry('centre', point, requires_point)

    @property
    def _centre(self):
        x0, y0, x1, y1 = self._bbox
        return (x0 + x1) / 2, (y0 + y1) / 2

    @_centre.setter
    def _centre(self, point):
        xp, yp = point
        xc, yc = self._centre
        dx = xp - xc
        dy = yp - yc
        x0, y0, x1, y1 = self._bbox
        self._bbox = x0 + dx, y0 + dy, x1 + dx, y1 + dy


class Shape2D(Shape, ABC):

    def __init__(self, drawing):
        super().__init__(drawing)
        self._fill = DEFAULT_FILL
        self._stroke = DEFAULT_STROKE
        self._stroke_width = DEFAULT_STROKE_WIDTH

    def initialize(self):
        self.fill(self._fill)
        self.stroke(self._stroke)
        self.stroke_width(self._stroke_width)

    def fill(self, value=None):
        return self._set_or_get('fill', value, requires_colour)

    def stroke(self, value=None):
        return self._set_or_get('stroke', value, requires_colour)

    def stroke_width(self, value=None):
        return self._set_or_get('stroke_width', value, requires_positive_number)

    def width(self, width=None):
        return self._geometry('width', width, requires_positive_number)

    def height(self, height=None):
        return self._geometry('height', height, requires_positive_number)

    @property
    def _width(self):
        x0, y0, x1, y1 = self._bbox
        return abs(x0 - x1)

    @_width.setter
    def _width(self, width):
        xc, yc = self._centre
        new_x0 = xc + width / 2
        new_x1 = xc - width / 2
        x0, y0, x1, y1 = self._bbox
        self._bbox = new_x0, y0, new_x1, y1

    @property
    def _height(self):
        x0, y0, x1, y1 = self._bbox
        return abs(y0 - y1)

    @_height.setter
    def _height(self, height):
        xc, yc = self._centre
        new_y0 = yc + height / 2
        new_y1 = yc - height / 2
        x0, y0, x1, y1 = self._bbox
        self._bbox = x0, new_y0, x1, new_y1


class Ellipse(Shape2D):

    def make(self):
        self._id = self.drawing.make_ellipse(self._bbox)


class Rectangle(Shape2D):

    def make(self):
        self._id = self.drawing.make_rectangle(self._bbox)


class Line(Shape):

    def __init__(self, drawing):
        super().__init__(drawing)
        self._fill = DEFAULT_STROKE
        self._stroke_width = DEFAULT_LINE_WIDTH

    def make(self):
        self._id = self.drawing.make_line(self._bbox)

    def initialize(self):
        self.stroke(self._fill)
        self.stroke_width(self._stroke_width)

    def start(self, point=None):
        return self._geometry('start', point, requires_point)

    def end(self, point=None):
        return self._geometry('end', point, requires_point)

    def length(self, new_length=None):
        return self._geometry('length', new_length, requires_positive_number)

    def stroke(self, colour=None):
        return self._set_or_get('fill', colour, requires_colour)

    def stroke_width(self, width=None):
        return self._set_or_get('stroke_width', width, requires_positive_number)

    @property
    def _start(self):
        return self._bbox[0], self._bbox[1]

    @_start.setter
    def _start(self, value):
        self._bbox = (value[0], value[1], self._bbox[2], self._bbox[3])

    @property
    def _end(self):
        return self._bbox[2], self._bbox[3]

    @_end.setter
    def _end(self, value):
        self._bbox = (self._bbox[0], self._bbox[1], value[0], value[1])

    @property
    def _length(self):
        x0, y0, x1, y1 = self._bbox
        return math.sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)

    @_length.setter
    def _length(self, new_length):
        x0, y0, x1, y1 = self._bbox
        length = self._length
        new_signed_width = (x1 - x0) / length * new_length
        new_signed_height = (y1 - y0) / length * new_length
        cx, cy = self._centre
        new_x0 = cx - new_signed_width / 2
        new_x1 = cx + new_signed_width / 2
        new_y0 = cy - new_signed_height / 2
        new_y1 = cy + new_signed_height / 2
        self._bbox = (new_x0, new_y0, new_x1, new_y1)


class Text(Shape):

    def __init__(self, drawing):
        super().__init__(drawing)
        self._string = DEFAULT_STRING
        self._height = DEFAULT_TEXT_HEIGHT
        self._fill = DEFAULT_FILL
        self._centre = (DRAWING_SIZE / 2, DRAWING_SIZE / 2)

    def make(self):
        self._id = self.drawing.make_text(*self._centre)

    def initialize(self):
        self.string(self._string)
        self.drawing.set_font(self._id, (None, self._height))

    def move(self, dx, dy):
        requires_two_numbers('move', dx, dy)
        x, y = self._centre
        self._centre = x + dx, y + dy
        self.drawing.move(self._id, dx, dy)
        return self

    def centre(self, point=None):
        if point is not None:
            requires_point('centre', point)
            cx, cy = self._centre
            px, py = point
            return self.move(px - cx, py - cy)
        else:
            return self._centre

    def string(self, new_string):
        return self._set_or_get('string', new_string, requires_string)

    def fill(self, new_fill=None):
        return self._set_or_get('fill', new_fill, requires_colour)

    def height(self, new_height=None):
        if new_height is not None:
            requires_positive_number('height', new_height)
            self._height = new_height
            self.drawing.set_font(self._id, (None, self._height))
            return self
        else:
            return self._height


def go(user_program):
    root = tk.Tk()
    drawing = Drawing(root)
    root.resizable(False, False)
    Thread(target=lambda: user_program(drawing), daemon=True).start()
    drawing.master.mainloop()


__all__ = ['go']
