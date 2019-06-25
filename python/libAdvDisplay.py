from PIL import ImageFont
width = 128
font = ImageFont.load_default()
cinzel15 = ImageFont.truetype("Cinzel-Regular.otf", 15)
cinzel10 = ImageFont.truetype("Cinzel-Regular.otf", 10)


def draw_center_text_font(text, y, fill, draw, customFont):
    draw_text(text, y, fill, draw, customFont)


def draw_text(text, y, fill, draw, customFont):
    xText = customFont.getsize(text)[0]
    draw.text(((width - xText) / 2, y), text, font=customFont, fill=fill)


def draw_centered_text(text, y, fill, draw):
    draw_text(text, y, fill, draw, font)