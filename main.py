import arcade
from game import constants


class Window(arcade.Window):
    def __init__(self):
        # Build window
        super().__init__(constants.WIDTH, constants.HEIGHT, constants.TITLE)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.left_pressed = False
        self.right_pressed = False
        self.facing = "right"
        # initiailze player list
        self.player_list = arcade.SpriteList()
        self.player = arcade.Sprite("assets/fat_man_right.png",
                                    constants.SPRITE_SCALING_PLAYER)
        grid_x = 1
        grid_y = 1
        self.player.center_x = constants.SPRITE_SIZE * \
            grid_x + constants.SPRITE_SIZE / 2
        self.player.center_y = constants.SPRITE_SIZE * \
            grid_y + constants.SPRITE_SIZE / 2
        self.player_list.append(self.player)

        map = arcade.tilemap.read_tmx("assets/map2.tmx")
        self.platform_list = arcade.tilemap.process_layer(
            map, "Tile Layer 1", constants.SPRITE_SCALING_TILES)

        # Spatial hashing speeds time to find collision
        self.floor_list = arcade.SpriteList(use_spatial_hash=True)
        # make ground
        for x in range(0, 1250, constants.SPRITE_IMAGE_SIZE):
            floor = arcade.Sprite("assets/fat_man_left.png",
                                  constants.SPRITE_SCALING_TILES)
            floor.center_x = x
            floor.center_y = 32
            self.floor_list.append(floor)
        self.item_list = arcade.SpriteList(use_spatial_hash=True)

        # Create physics
        self.physics_engine = arcade.PymunkPhysicsEngine(
            damping=constants.DEFAULT_DAMPING, gravity=constants.GRAVITY)
        self.physics_engine.add_sprite(self.player,
                                       friction=constants.PLAYER_FRICTOIN,
                                       mass=constants.PLAYER_MASS,
                                       moment=arcade.PymunkPhysicsEngine.MOMENT_INF, collision_type="player",
                                       max_horizontal_velocity=constants.PLAYER_MAX_VX,
                                       max_vertical_velocity=constants.PLAYER_MAX_VY)

        self.physics_engine.add_sprite_list(self.platform_list,
                                            friction=constants.FLOOR_FRICTION,
                                            collision_type="floor",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        self.physics_engine.add_sprite_list(self.floor_list,
                                            friction=constants.FLOOR_FRICTION,
                                            collision_type="wall",
                                            body_type=arcade.PymunkPhysicsEngine.STATIC)

        self.physics_engine.add_sprite_list(self.item_list,
                                            friction=constants.DYNAMIC_ITEM_FRICTION,
                                            collision_type="item")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.is_on_ground(self.player):
                f = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(self.player, f)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

    def on_update(self, dt):
        grounded = self.physics_engine.is_on_ground(self.player)
        if self.left_pressed and not self.right_pressed:
            if grounded:
                # Might have vertical movement, but force APPLIED is zero
                f = (-constants.PLAYER_MOVE_FORCE_GROUND, 0)
            else:
                f = (-constants.PLAYER_MOVE_FORCE_AIR, 0)
            self.physics_engine.set_friction(self.player, 0)
            self.physics_engine.apply_force(self.player, f)

        elif self.right_pressed and not self.left_pressed:
            if grounded:
                # Might have vertical movement, but force APPLIED is zero
                f = (constants.PLAYER_MOVE_FORCE_GROUND, 0)
            else:
                f = (constants.PLAYER_MOVE_FORCE_AIR, 0)
            self.physics_engine.set_friction(self.player, 0)
            self.physics_engine.apply_force(self.player, f)
        else:
            # Stuck while holding both down
            self.physics_engine.set_friction(self.player, 1)

        self.physics_engine.step()

    def on_draw(self):
        arcade.start_render()
        self.floor_list.draw()
        self.platform_list.draw()
        self.item_list.draw()
        self.player_list.draw()


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
