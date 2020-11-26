import arcade
from game import constants, entity, sounds, WinView, PauseView, LoseView


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_viewport(0, self.window.w, 0, self.window.h)
        self.window.set_mouse_visible(False)

    def setup(self):
        self.background = arcade.load_texture(
            "assets/background_final.png")
        self.left_pressed = False
        self.right_pressed = False
        self.view_left = 0
        self.immune_for = 3
        # initiailze player list
        self.player_list = arcade.SpriteList()
        # name = "main_char"
        if self.window.hits_left == 4:
            self.player = entity.Entity("hazmat")
        elif self.window.hits_left == 3:
            self.player = entity.Entity("main_char_gas")
        elif self.window.hits_left == 2:
            self.player = entity.Entity("main_char_mask")
        else:
            self.player = entity.Entity("main_char")
        grid_x = 1
        grid_y = 1
        self.player.center_x = constants.SPRITE_SIZE * \
            grid_x + constants.SPRITE_SIZE / 2
        self.player.center_y = constants.SPRITE_SIZE * \
            grid_y + constants.SPRITE_SIZE / 2
        # self.player.center_x = constants.WIDTH * 6
        self.player_list.append(self.player)

        self.cashier = arcade.Sprite("assets/cashier/closed.png")
        self.cashier.center_y = self.player.center_y
        self.cashier.center_x = self.window.w * 6

        map = arcade.tilemap.read_tmx("assets/map_real.tmx")
        self.platform_list = arcade.tilemap.process_layer(
            map, "Platform", constants.SCALING_TILES)

        # Spatial hashing speeds time to find collision

        # ENEMY
        self.enemy_list = arcade.SpriteList()
        enemy1 = entity.Entity("employee")
        enemy1.bottom = constants.SPRITE_SIZE
        enemy1.left = 6 * constants.SPRITE_SIZE
        enemy1.boundary_left = enemy1.left - 300
        enemy1.boundary_right = enemy1.left + 250
        enemy1.change_x = 2
        self.enemy_list.append(enemy1)

        enemy2 = entity.Entity("karen")
        enemy2.bottom = constants.SPRITE_SIZE
        enemy2.left = 15 * constants.SPRITE_SIZE
        enemy2.boundary_left = enemy2.left - 50
        enemy2.boundary_right = enemy2.left + 256
        enemy2.change_x = 2
        self.enemy_list.append(enemy2)

        enemy3 = entity.Entity("fatman")
        enemy3.bottom = 4 * constants.SPRITE_SIZE
        enemy3.left = 12 * constants.SPRITE_SIZE
        enemy3.boundary_left = enemy3.left
        enemy3.boundary_right = enemy3.left + 512
        enemy3.change_x = 2
        self.enemy_list.append(enemy3)

        enemy4 = entity.Entity("karen")
        enemy4.bottom = 3 * constants.SPRITE_SIZE
        enemy4.left = 6 * constants.SPRITE_SIZE
        enemy4.boundary_left = enemy4.left - 256
        enemy4.boundary_right = enemy4.left + 128
        enemy4.change_x = 1
        self.enemy_list.append(enemy4)

        enemy5 = entity.Entity("employee")
        enemy5.bottom = 7 * constants.SPRITE_SIZE
        enemy5.left = 17 * constants.SPRITE_SIZE
        enemy5.boundary_left = enemy5.left - 50
        enemy5.boundary_right = enemy5.left + 256
        enemy5.change_x = 2
        self.enemy_list.append(enemy5)

        enemy6 = entity.Entity("fatman")
        enemy6.bottom = 7 * constants.SPRITE_SIZE
        enemy6.left = 29 * constants.SPRITE_SIZE
        enemy6.boundary_left = enemy6.left - 256
        enemy6.boundary_right = enemy6.left + 64
        enemy6.change_x = 3
        self.enemy_list.append(enemy6)

        enemy7 = entity.Entity("employee")
        enemy7.bottom = constants.SPRITE_SIZE
        enemy7.left = 32 * constants.SPRITE_SIZE
        enemy7.boundary_left = enemy7.left - 64
        enemy7.boundary_right = enemy7.left + 18 * constants.SPRITE_SIZE
        enemy7.change_x = 5
        self.enemy_list.append(enemy7)

        enemy8 = entity.Entity("fatman")
        enemy8.bottom = 7 * constants.SPRITE_SIZE
        enemy8.left = 48 * constants.SPRITE_SIZE
        enemy8.boundary_left = enemy8.left - 128
        enemy8.boundary_right = enemy8.left + 200
        enemy8.change_x = 7
        self.enemy_list.append(enemy8)

        enemy9 = entity.Entity("karen")
        enemy9.bottom = constants.SPRITE_SIZE
        enemy9.left = 48 * constants.SPRITE_SIZE
        enemy9.boundary_left = enemy9.left - 18 * constants.SPRITE_SIZE
        enemy9.boundary_right = enemy9.left + 64
        enemy9.change_x = 3
        self.enemy_list.append(enemy9)

        enemy10 = entity.Entity("karen")
        enemy10.bottom = constants.SPRITE_SIZE
        enemy10.left = 40 * constants.SPRITE_SIZE
        enemy10.boundary_left = enemy10.left - 9 * constants.SPRITE_SIZE
        enemy10.boundary_right = enemy10.left + 9 * constants.SPRITE_SIZE
        enemy10.change_x = 5
        self.enemy_list.append(enemy10)

        enemy11 = entity.Entity("fatman")
        enemy11.bottom = constants.SPRITE_SIZE
        enemy11.left = 48 * constants.SPRITE_SIZE
        enemy11.boundary_left = enemy11.left - 18 * constants.SPRITE_SIZE
        enemy11.boundary_right = enemy11.left + 64
        enemy11.change_x = 5
        self.enemy_list.append(enemy11)

        enemy12 = entity.Entity("employee")
        enemy12.bottom = constants.SPRITE_SIZE
        enemy12.left = 56 * constants.SPRITE_SIZE
        enemy12.boundary_left = enemy12.left - 144
        enemy12.boundary_right = enemy12.left + 300
        enemy12.change_x = 3
        self.enemy_list.append(enemy12)

        enemy13 = entity.Entity("fatman")
        enemy13.bottom = 7 * constants.SPRITE_SIZE
        enemy13.left = 64 * constants.SPRITE_SIZE
        enemy13.boundary_left = enemy13.left - 128
        enemy13.boundary_right = enemy13.left + 200
        enemy13.change_x = 3
        self.enemy_list.append(enemy13)

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

        self.physics_engine.add_sprite_list(self.window.item_list,
                                            friction=constants.DYNAMIC_ITEM_FRICTION,
                                            collision_type="item")

        self.physics_engine.add_sprite(self.cashier,
                                       friction=constants.DYNAMIC_ITEM_FRICTION,
                                       collision_type="floor")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True
        elif key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.is_on_ground(self.player):
                if self.window.fx_on:
                    sounds.jump.play()
                f = (0, constants.PLAYER_JUMP_IMPULSE)
                self.physics_engine.apply_impulse(self.player, f)
        elif key == arcade.key.ESCAPE:
            pause_view = PauseView.PauseView(self)
            self.window.show_view(pause_view)

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
        if self.window.score >= self.window.goal:
            self.cashier.texture = arcade.load_texture_pair(
                "assets/cashier/open.png")[0]
        self.cashier.update()
        if arcade.check_for_collision(self.player, self.cashier) and self.window.score >= self.window.goal:
            game_win = WinView.WinView()
            self.window.show_view(game_win)

        for enemy in self.enemy_list:
            # If the enemy hit the left boundary, reverse
            if enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                enemy.facing_left = 0
                enemy.walk_curr_index = 0
                enemy.change_x *= -1
                enemy.move_enemy()
            # If the enemy hit the right boundary, reverse
            elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                enemy.facing_left = 1
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
            self.player, self.window.item_list)
        for TP in TP_hit_list:
            TP.remove_from_sprite_lists()
            self.window.score += 1

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
        left_boundary = self.view_left + constants.VIEWPORT_MARGIN
        if self.player.center_x < left_boundary and self.view_left - (left_boundary - self.player.center_x) > 0:
            self.view_left -= left_boundary - self.player.center_x
            changed_viewport = True
        right_boundary = self.view_left + self.window.w - constants.VIEWPORT_MARGIN
        if self.player.center_x > right_boundary and self.view_left + (self.player.center_x - right_boundary) + self.window.w < constants.LEVEL_WIDTH:
            self.view_left += self.player.center_x - right_boundary
            changed_viewport = True
        if changed_viewport:
            self.view_left = int(self.view_left)
            # Scroll
            arcade.set_viewport(
                self.view_left, self.window.w + self.view_left, 0, self.window.h)
        if len(arcade.check_for_collision_with_list(self.player, self.enemy_list)) > 0:
            if self.immune_for <= 0:
                self.immune_for = 3
                if self.window.fx_on:
                    # sounds.sneeze.play()
                    sounds.grunt.play()
                self.window.hits_left -= 1
                if self.window.hits_left <= 0:
                    view = LoseView.LoseView()
                    self.window.show_view(view)
                else:
                    game_view = GameView()
                    game_view.setup()
                    self.window.show_view(game_view)
        if self.player.center_y < 0:
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(
            0, 0,
            constants.LEVEL_WIDTH, self.window.h,  # 100 x 9 level
            self.background)
        self.platform_list.draw()
        self.enemy_list.draw()
        self.cashier.draw()
        self.player_list.draw()
        self.window.item_list.draw()
        tp_amount = arcade.load_texture(
            "assets/amounts/toilet_paper_amount.png")
        scale = 1
        arcade.draw_scaled_texture_rectangle(
            max(120, self.view_left + 70), self.window.h - 35, tp_amount, scale, 0)
        score_text = f"{self.window.score}"
        arcade.draw_text(score_text, max(94, self.view_left + 44), self.window.h - 50,
                         arcade.csscolor.BLACK, 18)
        if self.window.score < self.window.goal and arcade.check_for_collision(self.player, self.cashier):
            arcade.draw_text("Come back with 15 items", self.view_left + self.window.w / 2, self.window.h - 50,
                             arcade.csscolor.CRIMSON, 24, anchor_x="center")
        elif self.window.score >= self.window.goal:
            arcade.draw_text("Find the cashier to checkout", self.view_left + self.window.w / 2, self.window.h - 50,
                             arcade.csscolor.CRIMSON, 24, anchor_x="center")
