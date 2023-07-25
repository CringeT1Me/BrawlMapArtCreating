class GetColor:
    def __init__(self):
        self.colors = {
            "red_slow": (233, 2, 1),
            "red_green_cactus": (49, 158, 73),
            "green_boost": (1, 194, 1),
            "blue_water": (87, 184, 241),
            "brown_barrel": (233, 177, 128),
            "brown_wall": (152, 75, 38),
            "brown_crate": (255, 192, 131),
            "yellow_grass": (225, 109, 23),
            "black_spikes": (30, 30, 30),
            "white_bones": (255, 227, 202)
        }
        self.colors_with_map_cells = {
            "red_slow": (233, 2, 1),
            "red_green_cactus": (49, 158, 73),
            "green_boost": (1, 194, 1),
            "blue_water": (87, 184, 241),
            "brown_barrel": (233, 177, 128),
            "brown_wall": (152, 75, 38),
            "brown_crate": (255, 192, 131),
            "yellow_grass": (225, 109, 23),
            "black_spikes": (30, 30, 30),
            "white_bones": (255, 227, 202),
            "brown_map_cell_light": (249, 166, 118),
            "brown_map_cell_dark": (236, 158, 109)
        }

    def get_color(self, rgb):
        min_distance = float("inf")
        closest_color = None
        for color, value in self.colors.items():
            distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
            if distance < min_distance:
                min_distance = distance
                closest_color = color
        return closest_color

    def get_color_map_cells(self, rgb):
        min_distance = float("inf")
        closest_color = None
        for color, value in self.colors_with_map_cells.items():
            distance = sum([(i - j) ** 2 for i, j in zip(rgb, value)])
            if distance < min_distance:
                min_distance = distance
                closest_color = color
        return closest_color

    def get_item_color(self, item):
        return self.colors_with_map_cells.get(item)