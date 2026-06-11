from PIL import Image, ImageDraw, ImageFont


def create_collection_image(
    movies,
    series,
    anime,
    favorites,
    items,
    page
):

    width = 1080
    height = 1350

    image = Image.new(
        "RGB",
        (width, height),
        (0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    title_font = ImageFont.load_default()
    normal_font = ImageFont.load_default()

    green = (0, 255, 127)

    draw.text(
        (330, 40),
        "CINEVAULT COLLECTION",
        fill=green,
        font=title_font
    )

    draw.text(
        (70, 140),
        f"Movies : {movies}",
        fill="white",
        font=normal_font
    )

    draw.text(
        (70, 190),
        f"Series : {series}",
        fill="white",
        font=normal_font
    )

    draw.text(
        (70, 240),
        f"Anime : {anime}",
        fill="white",
        font=normal_font
    )

    draw.text(
        (70, 290),
        f"Favorites : {favorites}",
        fill="white",
        font=normal_font
    )

    y = 400

    for item in items:

        draw.text(
            (90, y),
            item,
            fill="white",
            font=normal_font
        )

        y += 45

    draw.text(
        (450, 1250),
        f"Page {page}",
        fill=green,
        font=normal_font
    )

    path = "collection.png"

    image.save(path)

    return path