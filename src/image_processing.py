import random
from pathlib import Path
from time import perf_counter

from PIL import Image, ImageOps, ImageDraw, ImageFont

from src.prime_search import next_prime


def load_image(path: str, width: int, height: int) -> Image.Image:
    with Image.open(path) as image:
        image = ImageOps.exif_transpose(image)

        return image.convert("RGB").resize(
            (width, height),
            Image.Resampling.LANCZOS
        )

def color_err(
    pixel: tuple[int, int, int],
    color: tuple[int, int, int]
) -> int:
    # Calculate the squared Euclidean distance between two RGB colors.
    return sum((p - c) ** 2 for p, c in zip(pixel, color))

def closest_color(
    pixel: tuple[int, int, int],
    palette: list[tuple[int, int, int]]) -> int:
    # Return the index of the palette colour closest to pixel.
    min_index = 0
    min_distance = color_err(pixel, palette[0])
    for i in range(1, len(palette)):
        distance = color_err(pixel, palette[i])
        if distance < min_distance:
            min_distance = distance
            min_index = i
    return min_index
    
def average_color(
    pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:

    # Return the component-wise average RGB colour.
    r_total = sum(p[0] for p in pixels)
    g_total = sum(p[1] for p in pixels) 
    b_total = sum(p[2] for p in pixels)
    n = len(pixels)
    return (round(r_total / n), round(g_total / n), round(b_total / n))

def kmeans(
    pixels: list[tuple[int, int, int]],
    k: int = 10,
    max_iterations: int = 100
) -> list[tuple[int, int, int]]:
    # Find k representative colours using K-means clustering.
    rng = random.Random(67)
    palette = rng.sample(pixels, k)
    for _ in range(max_iterations):
        clusters = [[] for _ in range(k)]
        for pixel in pixels:
            index = closest_color(pixel, palette)
            clusters[index].append(pixel)
        new_palette = [
            average_color(cluster) if cluster else palette[i]
            for i, cluster in enumerate(clusters)
        ]
        if new_palette == palette:
            break
        palette = new_palette
    return palette

def quantize_pixels(
    pixels: list[tuple[int, int, int]],
    palette: list[tuple[int, int, int]]
) -> list[tuple[int, int, int]]:
    # Replace every pixel with its closest palette colour.
    return [palette[closest_color(pixel, palette)] for pixel in pixels]

def pixels_to_digits(
    pixels: list[tuple[int, int, int]],
    palette: list[tuple[int, int, int]]
) -> str:
    # Convert every pixel into its closest palette index.
    return ''.join(str(closest_color(pixel, palette)) for pixel in pixels)

def render_prime_image(
        digits: str,
        palette: list[tuple[int, int, int]],
        width: int,
        height: int,
        cell_size: int = 20) -> Image.Image:
        # Create a canvas with one cell per digit.
        canvas = Image.new(
            "RGB",
            (width * cell_size, height * cell_size),
            (0, 0, 0)
        )

        draw = ImageDraw.Draw(canvas)
        font = ImageFont.truetype("consolab.ttf", 20)

        for i, digit in enumerate(digits):
            row = i // width
            col = i % width

            x = col * cell_size + cell_size / 2
            y = row * cell_size + cell_size / 2

            color = palette[int(digit)]

            draw.text(
                (x, y),
                digit,
                fill=color,
                font=font,
                anchor="mm",
                stroke_width=1,
                stroke_fill=color
            )

        return canvas

if __name__ == "__main__":
    image = load_image("images/sample.jpg", 36, 48)

    print("Dimensions:", image.size)
    print("Top-left pixel:", image.getpixel((0, 0)))

    image.resize((360, 480), Image.Resampling.NEAREST).save(
        "images/resized_sample.png"
    )

    pixels = list(image.get_flattened_data())
    palette = kmeans(pixels)

    print("\nRepresentative colours:")
    for i, color in enumerate(palette):
        print(f"{i}: {color}")

    quantized_pixels = quantize_pixels(pixels, palette)

    quantized_image = Image.new("RGB", image.size)
    quantized_image.putdata(quantized_pixels)

    quantized_image.resize(
        (360, 480),
        Image.Resampling.NEAREST
    ).save("images/quantized_sample.png")

    with Image.open("images/sample.jpg") as original:
        print("Original dimensions:", original.size)
        print("EXIF orientation:", original.getexif().get(274))

    digits = pixels_to_digits(pixels, palette)

    print("\nNumber of digits:", len(digits))
    print("First 100 digits:", digits[:100])
    print("Last 100 digits:", digits[-100:])
    print("First digit:", digits[0])

    number = int(digits)

    # print("\nInteger digit count:", len(str(number)))

    # for length in (100, 500, 1000):
    #     number = int(digits[:length])

    #     start = perf_counter()
    #     prime = next_prime(number)
    #     elapsed = perf_counter() - start

    #     print(f"\n{length}-digit benchmark:")
    #     print(f"Time: {elapsed:.4f} seconds")
    #     print(f"Prime gap: {prime - number}")

    # print("\nStarting full 1728-digit prime search...")

    # number = int(digits)

    # start = perf_counter()
    # prime = next_prime(number)
    # elapsed = perf_counter() - start

    # prime_gap = prime - number
    # prime_digits = str(prime)

    # print("\nFull image results:")
    # print(f"Time: {elapsed:.4f} seconds")
    # print(f"Prime gap: {prime_gap}")
    # print(f"Prime digit count: {len(prime_digits)}")

    # changed_pixels = sum(
    #     a != b
    #     for a, b in zip(digits, prime_digits)
    # )

    # print(f"Changed pixels: {changed_pixels}")
    # print(f"Original ending: {digits[-12:]}")
    # print(f"Prime ending:    {prime_digits[-12:]}")

    # Path("images/prime_digits.txt").write_text(prime_digits)
    # Path("images/prime_gap.txt").write_text(str(prime_gap))

    # print("\nPrime and prime gap saved successfully.")

    prime_digits = Path("images/prime_digits.txt").read_text().strip()

    assert len(prime_digits) == image.width * image.height

    artwork = render_prime_image(
        prime_digits,
        palette,
        image.width,
        image.height
    )

    artwork.save("images/prime_image.png")
    print("Prime Image saved!")

    