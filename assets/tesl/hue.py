from PIL import Image
import colorsys

def recolor_hue(input_path, output_path, target_hue):
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue

            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
            if s > 0.05:
                h = target_hue

            r2, g2, b2 = colorsys.hsv_to_rgb(h, s, v)
            pixels[x, y] = (
                int(r2 * 255),
                int(g2 * 255),
                int(b2 * 255),
                a
            )

    img.save(output_path)

def recolor_with_luminance(input_path, output_path, target_rgb):
    """
    target_rgb: (R, G, B) tuple, 0–255
    """
    img = Image.open(input_path).convert("RGBA")
    pixels = img.load()

    tr, tg, tb = target_rgb

    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue

            # Perceptual luminance
            lum = (0.2126 * r + 0.7152 * g + 0.0722 * b) / 255.0
            lum = pow(lum,0.85)

            # Apply luminance to target color
            pixels[x, y] = (
                int(tr * lum),
                int(tg * lum),
                int(tb * lum),
                a
            )

    img.save(output_path)

def to_grayscale(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    gray = img.convert("L")
    gray = Image.merge("RGBA", (gray, gray, gray, img.split()[3]))
    gray.save(output_path)

def main():
    recolor_with_luminance("icon_blue.png", "icon_orange2.png", (255, 165, 0))
    recolor_with_luminance("icon_blue.png", "icon_green2.png", (46, 204, 113))
    #to_grayscale("icon_blue.png", "icon_gray.png")

if __name__ == "__main__":
    main()

