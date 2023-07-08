def get_color_name(rgb):
    colors = {
        "red_slow": (233, 2, 1),
        "red_green_cactus": (49, 158, 73),
        "green_boost": (1, 194, 1),
        "blue_water": (87, 184, 241),
        "brown_barrel": (233, 177, 128),
        "brown_wall": (152, 75, 38),
        "brown_crate": (255, 192, 131),
        "yellow_grass": (225, 109, 23),
        "black_spikes": (0, 0, 0),
        "white_bones": (255, 227, 202),
    }
    min_distance = float("inf")
    closest_color = None
    for color, value in colors.items():
        distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
        if distance < min_distance:
            min_distance = distance
            closest_color = color
    return closest_color

def get_color(rgb):
    colors = {
        "red_slow": (233, 2, 1),
        "red_green_cactus": (49, 158, 73),
        "green_boost": (1, 194, 1),
        "blue_water": (87, 184, 241),
        "brown_powerup": (236, 158, 88),
        "brown_barrel": (233, 177, 128),
        "brown_wall": (152, 75, 38),
        "brown_crate": (255, 192, 131),
        "yellow_grass": (225, 109, 23),
        "black_spikes": (0, 0, 0),
        "white_bones": (255, 227, 202),
    }
    min_distance = float("inf")
    closest_color = None
    for color, value in colors.items():
        distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
        if distance < min_distance:
            min_distance = distance
            closest_color = value
    return closest_color


# Testing
from PIL import Image

source_image = Image.open("image.jpg").convert('RGB')
source_image = source_image.resize((60, 60))
map_of_assets = [[0] * 60 for i in range(60)]
pixels = source_image.load()
for x in range(60):
    for y in range(60):
        pixel = pixels[x, y]
        pixels[x, y] = get_color((pixel[0], pixel[1], pixel[2]))
        map_of_assets[x][y] = get_color_name((pixel[0], pixel[1], pixel[2]))
#         if pixel[0] > 128 and pixel[1] > 128 and pixel[2] > 128:
#             pixels[x, y] = (255, 255, 255)
#         elif pixel[0] <= 128 and pixel[1] <= 128 and pixel[2] <= 128:
#             pixels[x, y] = (0, 0, 0)
#         elif pixel[0] > pixel[1] and pixel[0] > pixel[2]:
#             pixels[x, y] = (pixel[0], 0, 0)
#         elif pixel[1] > pixel[0] and pixel[1] > pixel[2]:
#             pixels[x, y] = (0, pixel[1], 0)
#         elif pixel[2] > pixel[0] and pixel[2] > pixel[1]:
#             pixels[x, y] = (0, 0, pixel[2])
for i in range(60):
    for j in range(60):
        print(map_of_assets[i][j])

result_image = Image.new('RGB', ((2400,2400)), (0,0,0))
images = [[0] * 60 for i in range(60)]
for x in range(60):
    for y in range(60):
        images[x][y] = Image.open('assets\\showdown\\' + map_of_assets[x][y] + '.png').resize((40, 40)).convert('RGBA')
        result_image.paste(images[x][y], (x*40,y*40))
result_image.save('result.png')
