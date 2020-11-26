# Anything that has a walking animation left and right, no jumps
from game.constants import DISTANCE_PER_FRAME, ZONE_NO_ANIMATION
import arcade
import os
import os.path
from . import constants


class Entity(arcade.Sprite):
    def __init__(self, name):
        super().__init__()
        partial_path = "assets/"
        if name == "main_char":
            partial_path += "main_char_walking"
            self.char = True
        elif name == "main_char_mask":
            partial_path += "main_char_mask_walking"
            self.char = True
        elif name == "main_char_gas":
            partial_path += "main_char_gas_walking"
            self.char = True
        elif name == "hazmat":
            partial_path += "hazmat_walking"
            self.char = True
        elif name == "fatman":
            partial_path += "fatman_walking"
            self.char = False
        elif name == "karen":
            partial_path += "karen_walking"
            self.char = False
        elif name == "employee":
            partial_path += "employee_walking"
            self.char = False
        else:
            raise Exception("Name provided for entity didn't match: " + name)
        if self.char:
            self.scale = constants.SCALING_ENTITY
        else:
            self.scale = constants.SCALING_TILES
        self.num = 0
        self.stand_right = arcade.load_texture_pair(
            f"{partial_path}/1.png")
        self.jump_right = arcade.load_texture_pair(
            f"{partial_path}/5.png")
        self.walk_right = []
        fns = os.listdir(f"{partial_path}/")
        fns.sort(key=lambda fn: int(fn[:len(fn) - 4]))
        for fn in fns:
            self.walk_right.append(arcade.load_texture_pair(
                f"{partial_path}/{fn}"))
        # Initial
        self.facing_left = 0
        self.texture = self.stand_right[self.facing_left]
        self.hit_box = self.texture.hit_box_points  # Sets it based on first one
        self.distance_travelled_with_texture = 0
        self.walk_curr_index = 0

    def pymunk_moved(self, physics_engine, dx, dy, dtheta):
        # Facing
        if dx < -constants.ZONE_NO_ANIMATION and not self.facing_left:
            self.facing_left = 1
            self.walk_curr_index = 0
        elif dx > constants.ZONE_NO_ANIMATION and self.facing_left:
            self.facing_left = 0
            self.walk_curr_index = 0

        grounded = physics_engine.is_on_ground(self)
        self.distance_travelled_with_texture += dx

        if not grounded:
            if dy > ZONE_NO_ANIMATION or dy < -ZONE_NO_ANIMATION:
                self.texture = self.jump_right[self.facing_left]
            self.walk_curr_index = 0

        if abs(dx) <= ZONE_NO_ANIMATION:
            self.texture = self.stand_right[self.facing_left]
            self.walk_curr_index = 0
            return

        if abs(self.distance_travelled_with_texture) > DISTANCE_PER_FRAME:
            self.distance_travelled_with_texture = 0
            self.walk_curr_index += 1
            if self.walk_curr_index >= len(self.walk_right):
                self.walk_curr_index = 0
            self.texture = self.walk_right[self.walk_curr_index][self.facing_left]

    def move_enemy(self):
        if self.walk_curr_index >= len(self.walk_right):
            self.walk_curr_index = 0
        self.texture = self.walk_right[self.walk_curr_index][self.facing_left]
