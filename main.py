from game.constants import SPRITE_SCALING_TILES
import arcade
from game import constants, entity


class Window(arcade.Window):
    def __init__(self):
        # Build window
        super().__init__(constants.WIDTH, constants.HEIGHT, constants.TITLE)
        # arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        self.background = arcade.load_texture(
            "assets/background_final.png")
        self.left_pressed = False
        self.right_pressed = False
        self.facing = "right"
        self.view_left = 0
        self.hits_left = 4
        self.score = 0
        self.immune_for = 3
        # initiailze player list
        self.player_list = arcade.SpriteList()
        self.player = entity.Entity("hazmat")
        grid_x = 1
        grid_y = 1
        self.player.center_x = constants.SPRITE_SIZE * \
            grid_x + constants.SPRITE_SIZE / 2
        self.player.center_y = constants.SPRITE_SIZE * \
            grid_y + constants.SPRITE_SIZE / 2
        self.player_list.append(self.player)

        map = arcade.tilemap.read_tmx("assets/map_real.tmx")
        self.platform_list = arcade.tilemap.process_layer(
            map, "Platform", constants.SPRITE_SCALING_TILES)

        # Spatial hashing speeds time to find collision
        self.item_list = arcade.SpriteList()
        for x in range(150, int(constants.LEVEL_WIDTH), int(constants.LEVEL_WIDTH / 20)):
            TP = arcade.Sprite(
                "assets/toilet_paper.png", constants.SPRITE_SCALING_TILES / 2)
            TP.center_x = x
            TP.center_y = 200
            self.item_list.append(TP)

        # ENEMY
        self.enemy_list = arcade.SpriteList()
        enemy1 = entity.Entity("fatman")
        enemy1.bottom = constants.SPRITE_SIZE
        enemy1.left = 6 * constants.SPRITE_SIZE
        enemy1.boundary_left = enemy1.left - 300
        enemy1.boundary_right = enemy1.left + 250
        enemy1.change_x = 10
        self.enemy_list.append(enemy1)

        # for x in range(40, int(constants.LEVEL_WIDTH), int(constants.LEVEL_WIDTH / 20)):
        #     enemy = entity.Entity("fatman")
        #     enemy.bottom = constants.SPRITE_SIZE
        #     enemy.left = x
        #     enemy.boundary_left = x - 300
        #     enemy.boundary_right = x + 400
        #     enemy.change_x = 2
        #     self.enemy_list.append(enemy)

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
        if self.immune_for > 0:
            self.immune_for -= dt
        else:
            self.immune_for = 0
        # DEALING WITH MOVEMENT
        self.enemy_list.update()
        for enemy in self.enemy_list:
            # If the enemy hit the left boundary, reverse
            if enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                enemy.facing = "right"
                enemy.walk_curr_index = 0
                enemy.change_x *= -1
                enemy.move_enemy()
            # If the enemy hit the right boundary, reverse
            elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                enemy.facing = "left"
                enemy.walk_curr_index = 0
                enemy.change_x *= -1
                enemy.move_enemy()
            else:
                enemy.num += 1
                if enemy.num % 10 == 0:
                    enemy.walk_curr_index += 1
                enemy.move_enemy()

        # TP
        TP_hit_list = arcade.check_for_collision_with_list(
            self.player, self.item_list)
        for TP in TP_hit_list:
            print("GOT ONE")
            TP.remove_from_sprite_lists()
            self.score += 1

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

        # DEALING WITH VIEWPORT
        changed_viewport = False
        left_boundary = self.view_left + constants.LEFT_VIEWPORT_MARGIN
        if self.player.center_x < left_boundary and self.view_left - (left_boundary - self.player.center_x) > 0:
            self.view_left -= left_boundary - self.player.center_x
            changed_viewport = True
        right_boundary = self.view_left + constants.WIDTH - constants.RIGHT_VIEWPORT_MARGIN
        if self.player.center_x > right_boundary and self.view_left + (self.player.center_x - right_boundary) + constants.WIDTH < constants.LEVEL_WIDTH:
            self.view_left += self.player.center_x - right_boundary
            changed_viewport = True
        if changed_viewport:
            self.view_left = int(self.view_left)
            # Scroll
            arcade.set_viewport(
                self.view_left, constants.WIDTH + self.view_left, 0, constants.HEIGHT)
        if len(arcade.check_for_collision_with_list(self.player, self.enemy_list)) > 0:
            # TODO: Collisions change suit
            if self.immune_for <= 0:
                print("COLLIDED")
                self.hits_left -= 1
                self.player.remove_from_sprite_lists()
                # player = entity.Entity("hazmat")
                # grid_x = 1
                # grid_y = 1
                # self.player.center_x = constants.SPRITE_SIZE * \
                #     grid_x + constants.SPRITE_SIZE / 2
                # self.player.center_y = constants.SPRITE_SIZE * \
                #     grid_y + constants.SPRITE_SIZE / 2
                # self.player_list.append(player)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            constants.LEVEL_WIDTH, constants.HEIGHT,  # 100 x 9 level
            self.background)
        self.platform_list.draw()
        self.enemy_list.draw()
        self.player_list.draw()
        self.item_list.draw()


def main():
    window = Window()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
