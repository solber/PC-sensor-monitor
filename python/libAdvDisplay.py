from PIL import ImageFont
width = 128
font = ImageFont.load_default()
cinzel_15 = ImageFont.truetype("./fonts/Cinzel-Regular.otf", 15)
cinzel_10 = ImageFont.truetype("./fonts/Cinzel-Regular.otf", 10)


def draw_center_text_font(text, y, fill, draw, custom_font):
    draw_text(text, y, fill, draw, custom_font)


def draw_text(text, y, fill, draw, custom_font):
    x_text = custom_font.getsize(text)[0]
    draw.text(((width - x_text) / 2, y), text, font=custom_font, fill=fill)


def draw_centered_text(text, y, fill, draw):
    draw_text(text, y, fill, draw, font)
