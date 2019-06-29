import globalVars

#font5L = globalVars.ImageFont.truetype("./fonts/lucidaSTW.ttf", 10)
font_3G0 = globalVars.ImageFont.truetype("./fonts/lucidaSTWB.ttf", 14)
font_3G1 = globalVars.ImageFont.truetype("./fonts/lucidaSTW.ttf", 7)


def scale_value(actual_value, min_value, max_value, graph_length):  # Used to match a sensor value range with a graph length
    if actual_value >= max_value:
        scaled_value = graph_length
    else:
        scaled_value = (graph_length * (actual_value - min_value)) / (max_value - min_value)
    return int(scaled_value)


def draw_3graph(title, subtitle, position,
                (actual_value, min_value, max_value), draw):  # Designed to draw 3 graph on top of each other

    graph_3_y = [0, 22, 44]
    g3_text_y = [2, 24, 46]
    title_size = font_3G0.getsize(title)

    draw.rectangle((0, graph_3_y[position], title_size[0] + 6, graph_3_y[position] + 18), outline=255,
                   fill=1)  # Device name area
    draw.text((2, g3_text_y[position]), title, font=font_3G0, fill=0)  # Device name
    draw.text((title_size[0] + 8, graph_3_y[position]), subtitle, font=font_3G1, fill=1)  # Value name
    draw.polygon([(title_size[0], graph_3_y[position]), (title_size[0] + 6, graph_3_y[position]),
                  (title_size[0] + 6, graph_3_y[position] + 6)], outline=0, fill=0)  # Cropped angle for device name area

    draw.rectangle((title_size[0] + 6, graph_3_y[position] + 8, 127, graph_3_y[position] + 18), outline=255,
                   fill=0)  # Empty graph

    fill = scale_value(actual_value, min_value, max_value, 125 - (title_size[0] + 8))
    draw.rectangle((title_size[0] + 8, graph_3_y[position] + 10, (title_size[0] + 8) + fill, graph_3_y[position] + 16),
                   outline=0, fill=1)  # Filling graph
