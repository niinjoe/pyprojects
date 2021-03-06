class Snake:
    from turtle import Turtle

    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    for position in starting_positions:
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        segments.append(new_segment)


        for seg_num in range(len(segments) - 1, 0, -1):
            new_x = segments[seg_num - 1].xcor()
            new_y = segments[seg_num - 1].ycor()
            segments[seg_num].goto(new_x, new_y)
        segments[0].fd(20)
        segments[0].lt(90)
