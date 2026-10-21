from src.image_processing import (
    color_err,
    closest_color,
    average_color,
    pixels_to_digits
)


def test_color_err():
    assert color_err((184, 194, 204), (180, 190, 200)) == 48
    assert color_err((0, 0, 0), (0, 0, 0)) == 0
    assert color_err((255, 255, 255), (0, 0, 0)) == 195075


def test_closest_color():
    palette = [
        (180, 190, 200),
        (50, 100, 150),
        (0, 0, 0)
    ]

    assert closest_color((184, 194, 204), palette) == 0
    assert closest_color((45, 95, 145), palette) == 1
    assert closest_color((5, 5, 5), palette) == 2

def test_average_color():
    pixels = [
        (100, 150, 200),
        (120, 160, 180),
        (140, 170, 160)
    ]

    assert average_color(pixels) == (120, 160, 180)
    assert average_color([(255, 0, 100)]) == (255, 0, 100)
    assert average_color([(0, 0, 0), (255, 255, 255)]) == (128, 128, 128)

def test_average_color():
    pixels = [
        (100, 150, 200),
        (120, 160, 180),
        (140, 170, 160)
    ]

    assert average_color(pixels) == (120, 160, 180)
    assert average_color([(255, 0, 100)]) == (255, 0, 100)
    assert average_color([(0, 0, 0), (255, 255, 255)]) == (128, 128, 128)

def test_pixels_to_digits():
    palette = [
        (0, 0, 0),
        (255, 255, 255),
        (255, 0, 0)
    ]

    pixels = [
        (250, 10, 10),
        (5, 5, 5),
        (250, 250, 250),
        (0, 0, 0)
    ]

    assert pixels_to_digits(pixels, palette) == "2010"