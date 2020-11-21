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
        elif name == "fatman":
            partial_path += "fatman_walking"
            self.char = False
        elif name == "hazmat":
            partial_path += "hazmat_walking"
            self.char = False
        elif name == "karen":
            partial_path += "karen_walking"
            self.char = False
        else:
            raise Exception("Name provided for entity didn't match: " + name)
        if self.char:
            self.scale = constants.SPRITE_SCALING_PLAYER
        else:
            self.scale = constants.SPRITE_SCALING_TILES
        self.num = 0
        self.stand_right = arcade.load_texture_pair(
            f"{partial_path}_right/1.png")
        self.stand_left = arcade.load_texture_pair(
            f"{partial_path}_left/1.png")
        self.jump_right = arcade.load_texture_pair(
            f"{partial_path}_right/5.png")
        self.jump_left = arcade.load_texture_pair(
            f"{partial_path}_left/5.png")
        self.walk_right = []
        fns = os.listdir(f"{partial_path}_right/")
        fns.sort(key=lambda fn: int(fn[:len(fn) - 4]))
        for fn in fns:
            self.walk_right.append(arcade.load_texture_pair(
                f"{partial_path}_right/{fn}"))
        self.walk_left = []
        fns = os.listdir(f"{partial_path}_left/")
        fns.sort(key=lambda fn: int(fn[:len(fn) - 4]))
        for fn in fns:
            self.walk_left.append(arcade.load_texture_pair(
                f"{partial_path}_left/{fn}"))
        # Initial
        self.texture = self.stand_right[1]
        self.hit_box = self.texture.hit_box_points  # Sets it based on first one
        self.facing = "right"
        self.distance_travelled_with_texture = 0
        self.walk_curr_index = 0

    def pymunk_moved(self, physics_engine, dx, dy, dtheta):
        # Facing
        if dx < -constants.ZONE_NO_ANIMATION and self.facing == "right":
            self.facing = "left"
            self.walk_curr_index = 0
        elif dx > constants.ZONE_NO_ANIMATION and self.facing == "left":
            self.facing = "right"
            self.walk_curr_index = 0

        grounded = physics_engine.is_on_ground(self)
        self.distance_travelled_with_texture += dx

        if not grounded:
            if dy > ZONE_NO_ANIMATION or dy < -ZONE_NO_ANIMATION:
                if self.facing == "left":
                    self.texture = self.jump_left[0]
                elif self.facing == "right":
                    self.texture = self.jump_right[0]
            self.walk_curr_index = 0

        if abs(dx) <= ZONE_NO_ANIMATION:
            if self.facing == "left":
                self.texture = self.stand_left[0]
            elif self.facing == "right":
                self.texture = self.stand_right[0]
            self.walk_curr_index = 0
            return

        if abs(self.distance_travelled_with_texture) > DISTANCE_PER_FRAME:
            self.distance_travelled_with_texture = 0
            self.walk_curr_index += 1
            if self.walk_curr_index >= len(self.walk_right):
                self.walk_curr_index = 0
            if self.facing == "left":
                self.texture = self.walk_left[self.walk_curr_index][0]
            elif self.facing == "right":
                self.texture = self.walk_right[self.walk_curr_index][0]

    def move_enemy(self):
        # # Facing
        # if dx < -constants.ZONE_NO_ANIMATION and self.facing == "right":
        #     self.facing = "left"
        #     self.walk_curr_index = 0
        # elif dx > constants.ZONE_NO_ANIMATION and self.facing == "left":
        #     self.facing = "right"
        #     self.walk_curr_index = 0

        # grounded = physics_engine.is_on_ground(self)
        # self.distance_travelled_with_texture += dx

        # self.walk_curr_index = 0
        if self.walk_curr_index >= len(self.walk_right):
            self.walk_curr_index = 0
        if self.facing == "left":
            self.texture = self.walk_left[self.walk_curr_index][0]
        elif self.facing == "right":
            self.texture = self.walk_right[self.walk_curr_index][0]
