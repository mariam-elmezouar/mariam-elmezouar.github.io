.. footer::

   ###Page###/###Total###

=================================
GoGoGraphics package reference
=================================

.. sectnum::

.. contents::
   :backlinks: none

Overview
========

GoGoGraphics is a simple, object-oriented graphics library for Python.

In GoGoGraphics, all drawing and interaction takes place on an area called “the drawing.” You can add lines, rectangles, ellipses and text “shapes” to the drawing. You can change these shapes’ sizes and colours, you can move them around, and you can make them appear and disappear. You can wait for the user to click on the drawing and find out where the click happened. You can also create simple animations.

Here's a minimal example:

.. include:: ../examples/minimal.py
   :literal:

We first import the ``gogographics`` library. Then we define a function (here, called ``minimal``) that takes one parameter. By convention, the parameter is named ``drawing``. The body of the function is our program. This program creates a single ellipse on the drawing, with the default properties for a new ellipse. Finally, we call the ``gogoggraphics.go`` method, passing it the function we defined. (Note that we don't actually *call* the function by adding parentheses after its name, we just pass the function itself as a parameter to ``go``.)

Here’s a longer and more interesting example. It places a red elllipse with a narrow blue border, 100 units wide and 75 units high, at the drawing’s bottom left corner. It asks the user to click somewhere, then moves the ellipse, in an animation lasting about one second, until the ellipse is centred where the user clicked. This process repeats indefinitely.

.. include:: ../examples/clicktomove.py
   :literal:

    
Key concepts
==============

This section describes the key concepts of the GoGoGraphics package. Subsequent sections provide references for each of the shape types.

The drawing and drawing coordinates (points)
--------------------------------------------

The drawing is a square area, 800 by 800 pixels in extent. There is only one drawing at a time in a GoGoGraphics program. The lower left corner of the drawing is the point ``(0, 0)`` and the upper right is ``(800, 800)``. The first coordinate in a point is its horizontal distance from the origin, the second coordinate its vertical distance. Points are just Python tuples containing two numbers.

All locations, displacements, widths and heights are specified in drawing units. Drawing units are real-valued and can have any precision. So, for example, a width of ``32.5`` is fine, as is the point ``(129.0721, 936.58)``.

Shapes
------

GoGoGraphics provides four shape types: ``line``, ``rectangle``, ``ellipse``, and ``text``. You can create as many of each of these shape types as you like. All shapes have a centre and can be either visible or hidden. Each shape also has other properties, depending what it is. Lines have start points, end points, lengths, stroke widths, and stroke colours; text shapes have fill colours, heights, and strings (the text itself); and ellipses and rectangles have widths, heights, fill colours, stroke widths, and stroke colours.

Shapes are created by calling shape creation functions and may have their properties queried and modified by invoking methods on them. The `Shapes reference`_ section provides a complete list and description of the shape creation and property-querying and -modifying methods available for each shape type. In this section we explain how these methods can be used in your programs.

If a shape extends past the edge of the drawing it will be “clipped” so the part that is “off drawing” is not shown.

Creating shapes
~~~~~~~~~~~~~~~

To create a shape you call the corresponding method on the drawing. For example, you create a new ellipse like this::

    drawing.new_ellipse()
    
Each shape is created with a default set of properties. A new ellipse will be visible, 50 pixels wide and high, light grey with a darker grey border 1 pixel wide, centred on the point (400, 400).

Of course, if you want to do anything with a shape later you need to assign it to a variable, like this::

    e = drawing.new_ellipse()
    
or store it in a list, like this::

    ellipse_list = [ ]
    # lots of other ellipses added here...
    ellipse_list.append(drawing.new_ellipse())
    
Querying and modifying shape properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A shape’s properties can be queried by invoking methods on the shape. For instance, in this code fragment we create a new ellipse, name it ``e``, then ask for ``e``’s width::

   e = drawing.new_ellipse()
   w = e.width()

See the second line? The code ``e.width()`` means “invoke (execute) the ``width`` method of the shape referred to by ``e``.” Invoking the ``width`` method like this, without providing any parameters, will return the current value of ``e``’s ``width`` property. After running this code the value of the variable ``w`` will be 50, which is the default width for a new ellipse.

A shape’s properties can be set by invoking the appropriate method and providing a parameter of the correct type. Continuing the example above, we can change ``e``’s width to 375.5 like this::

    e.width(375.5)

Each method that modifies a shape’s properties returns a reference to the shape itself. So if we do this::

    f = e.height(55)
    
then the height of ``e`` will be set to 55 and ``f`` will refer to *the same ellipse* as ``e``. 

Method chaining
~~~~~~~~~~~~~~~

Returning a reference to the shape itself is a useful feature because it lets us do a trick called “method chaining.” This is where we invoke several methods in a row, like this::

    e.height(99).width(132).stroke_width(5).centre((300, 700))
    
In the line above we first set ``e``’s height to 99. The ``height`` method returns the ellipse it was called on, so we can then immediately invoke that ellipse’s ``width`` method, followed by its ``stroke_width`` method, and finally its ``centre`` method. The line above is exactly equivalent to this::

    e.height(99)
    e.width(132)
    e.stroke_width(5)
    e.centre([300 700])
    
\... but quite a bit more compact! A warning though: if there’s an error on a method-chained line it may be difficult to tell which method call is causing it. If this happens, a good debugging technique is to split the chain into separate calls.

Colours
-------

Colours in GoGoGraphics are given as tuples containing three numbers between 0 and 255. The first number in the list indicates the amount of red in the colour, the second the amount of green, and the third the amount of blue. 0 means “none of this” and 255 means “the maximum amount,” so (0, 0, 0) (no colour at all) is black and (255, 255, 255) (full intensity of all the colour components) is white. Any colour that can be displayed on screen can be specified this way.

Here are a few more examples: 

- bright red: ``(255, 0, 0)``
- darker red: ``(127, 0, 0)``
- bright green: ``(0, 255, 0)``
- bright blue:  ``(0, 0, 255)``
- bright yellow: ``(255, 255, 0)``
- bright magenta: ``(255, 0, 255)``
- bright cyan: ``(0, 255, 255)``
- tangerine orange: ``(255, 127, 0)``
- mocha brown: ``(127, 63, 0)``
- eggplant purple: ``(63, 0, 127)``
- medium grey: ``(127, 127, 127)``

You can access the red, green, and blue colour components by indexing into the tuple using the usual Python indexing syntax. So, if you have a colour ``c`` and want to get its components, you can do this::

    r = c[0]
    g = c[1]
    b = c[2]

You can also use Python’s “destructuring assignment” mechanism to access the components like this::

    r, g, b = c

User interaction (get_point)
----------------------------

GoGoGraphics offers one mechanism for accepting user input: the ``drawing.get_point`` method. When called, it waits for the user to click on the drawing then returns the point on which the user clicked. For example if we execute the line::

    p = drawing.get_point()

and the user clicks towards in the lower right of the drawing, ``p`` will be equal to something like (752, 156) afterwards.

We often need separate access to the ``x`` and ``y`` coordinates of a point. If we have a point ``p`` as above, the ``x`` coordinate is ``p[0]`` and the ``y`` coordinate is ``p[1]``. You can also use Python’s “destructuring assignment” mechanism to directly get the coordinates, like this::

    x, y = drawing.get_point()

Animation
---------

GoGoGraphics provides a simple animation capability. By calling ``drawing.pause`` with a time in milliseconds as a parameter, you can temporarily halt program execution. This statement::

    drawing.pause(16)

will cause a 16ms pause, which is about right for 60 frame per second animation.

For example, to create a text object, set its colour to black, and then cause it to fade to white over a period of about two seconds, we can do this::

    level = 0
    t = drawing.new_text()
    t.string('Help, I''m fading!').fill((level, level, level))
    for _ in range(51):
        drawing.pause(40)
        level = level + 5
        t.fill((level, level, level))

The initial text appears almost immediately. By default, a new text shape is filled with (204, 204, 204) so we start by setting its fill to (0, 0, 0) (black). In the for loop we fade the text to (255, 255, 255) (white) by adding 5 to each component of its colour 51 times. 

Calling ``drawing.pause(40)`` before each colour change causes GoGoGraphics to wait about 0.04 seconds (one twenty-fifth of a second). This means that the fifty-five step for loop will take a bit more than two seconds (0.04 x 51) to execute.


Shapes reference
================

All shapes
----------

Each shape can be visible or hidden and has a centre point. These properties can be changed by calling the appropriate method. For convenience, a ``move`` method is provided, which acts on the centre point.

visible
~~~~~~~

Invoked with no arguments, returns the shape’s current visibility, either ``True`` or ``False``::

    v = shape.visible()
    
Invoked with a boolean as argument, sets that as the shape’s visibility and returns the shape::

    shape.visible(False)

centre
~~~~~~

Invoked with no arguments, returns the current centre point of the shape::

    p = shape.centre()
    
Invoked with a point as argument, sets that as the shape’s centre point and returns the shape::

    shape.centre((400, 700))
 
move
~~~~

Invoked with two numbers representing horizontal and vertical displacement, adds those numbers to the shape’s centre point and returns the shape::

    shape.move(10, 20)
    
Of course, the same effect can be achieved using the centre method::

    shape.centre(shape.centre()[0] + 10, shape.centre()[1] + 20)
    
Ellipses and rectangles
-----------------------

Ellipses and rectangles offer exactly the same methods as one another. The only difference is that ellipses are curved and rectangles have corners. Go figure. An ellipse or rectangle has a height, a width, a fill colour, a stroke width (the stroke is the border around the shape) and a stroke colour.

See also the methods ``visible``, ``centre``, and ``move``.

drawing.new_ellipse
~~~~~~~~~~~~~~~~~~~

Creates a new ellipse centred at (400, 400), 50 wide, 50 high, with a stroke width of 1, a colour of (204, 204, 204) (light grey) and a stroke colour of (76, 76, 76) (darker grey)::

    e = new_ellipse()

drawing.new_rectangle
~~~~~~~~~~~~~~~~~~~~~

Creates a new rectangle centred at (400, 400), 50 wide, 50 high, with a stroke width of 1, a colour of (204, 204, 204) and a stroke colour of (76, 76, 76)::

    r = new_rectangle()

height
~~~~~~

Invoked with no arguments, returns the current height of the ellipse or rectangle::

    h = e.height()
    
Invoked with a number, sets the ellipse or rectangle’s height to that number and returns the shape::

    e.height(250)
    
width
~~~~~

Invoked with no arguments, returns the current width of the ellipse or rectangle::

    w = r.width()
    
Invoked with a number, sets the ellipse or rectangle’s width to that number and returns the shape::

    r.width(250)

stroke_width
~~~~~~~~~~~~

Invoked with no arguments, returns the current stroke width of the ellipse or rectangle::

    sw = e.stroke_width()
    
Invoked with a number, sets the ellipse or rectangle’s stroke width to that number and returns the shape. The stroke is *centred on* the edge of the shape, so making the stroke wider will eat into the middle of the shape by half the stroke width, and make the shape larger by the other half.::

    e.stroke_width(20)

 
fill
~~~~~~~~~~~~~~~~~

Invoked with no arguments, returns the current fill colour of the shape, which will be a three-element tuple with values between (0, 0, 0) and (255, 255, 255). See `Colours`_ for more details::

    c = shape.fill()
    
Invoked with a colour, sets the shape’s fill colour to that value and returns the shape::

    shape.fill((27, 129, 88))
    

stroke
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Invoked with no arguments, returns the current stroke colour of the shape, which will be a three-element tuple with values between (0, 0, 0) and (255, 255, 255). See `Colours`_ for more details::

    c = shape.stroke()
  
Invoked with a colour, sets the shape’s stroke colour to that value and returns the shape::

    shape.stroke((204, 102, 255))

Lines
-----

A line has a start point, end point, length and stroke width, and stroke colour. See also the methods ``visible``, ``centre``, and ``move`` in `All shapes`_. 

Moving a line’s centre changes its start and end points but not its length. Changing a line’s length changes its start and end points but not its centre.

drawing.new_line
~~~~~~~~~~~~~~~~

Creates a line from (375, 375) to (425, 425), and therefore about 70.7 long and centred at (400, 400), with a stroke width of 2 and a stroke colour of (76, 76, 76)::

    ln = drawing.new_line()

start
~~~~~

Invoked with no arguments, returns the current start point of the line::

    s = ln.start()
    
Invoked with a point, changes the line’s start point to that point. Changing a line’s start point may affect its length and centre::

    ln.start((25, 25))

end
~~~

Invoked with no arguments, returns the current end point of the line::

    e = ln.end()
    
Invoked with a point, changes the line’s end point to that point and returns the line. Changing a line’s end point may affect its length and centre::

    ln.end((775, 775))


length
~~~~~~

Invoked with no arguments, returns the current length of the line::

    lg = ln.length()
    
Invoked with a number, changes the line’s length to match that number and returns the line. The line is extended or contracted around its centre. Changing a line’s length may affect its start point and end point::

    ln.length(275)


stroke_width
~~~~~~~~~~~~

Invoked with no arguments, returns the current stroke width of the line::

    w = ln.stroke_width()
    
Invoked with a number, sets the line’s width to that number and returns the line::

    ln.stroke_width(15)

stroke
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Invoked with no arguments, returns the current stroke colour of the line, which will be a three-element tuple with values between (0, 0, 0) and (255, 255, 255). See `Colours`_ for more details::

    c = ln.stroke()
  
Invoked with a colour, sets the line’s stroke colour to that value and returns the line::

    ln.stroke((204, 102, 255))

Text
----

Text shapes have a string (the text itself), a height, and a fill. See also the methods ``visible``, ``centre``, and ``move`` in `All shapes`_.

*A text shape does not have a width property!* Calling ``width`` on a text shape will result in an error.

drawing.new_text
~~~~~~~~~~~~~~~~

Creates a new text shape with the string “default text”, set in your computer's default system font (likely Helvetica or Arial), centred at (400, 400), coloured (76, 76, 76), with a height of 24::

    t = drawing.new_text()
    
string
~~~~~~

Invoked with no arguments, returns the current string value of the text shape::

    s = t.string()
    
Invoked with a string, sets the text’s string value to that string and returns the text shape::

    t.string('Now I''m something new!')
    
height
~~~~~~

Invoked with no arguments, returns the current height of the text shape::

    h = t.height()
    
Invoked with a number, sets the text shape’s height to that number and returns the text shape::

    t.height(75)

fill
~~~~~~~~~~~~~~~~~

Invoked with no arguments, returns the current fill colour of the text, which will be a three-element tuple with values between (0, 0, 0) and (255, 255, 255). See `Colours`_ for more details::

    c = t.fill()

Invoked with a colour, sets the text’s fill colour to that value and returns the shape::

    t.fill((27, 129, 88))


Copyright information
=================================================

The GoGoGraphics library, including this document, is copyright His Majesty in Right of Canada, ©2023. Unlimited use permitted within the Government of Canada; all other use subject to the `GNU General Public License version 3 <http://www.gnu.org/copyleft/gpl.html>`_.

Version 1.0: Greg Phillips, 16 May 2023