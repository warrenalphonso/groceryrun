GRAVITY = (0, -2000)
MASS = 1.0
PLAYER_MASS = 2.0

DEFAULT_DAMPING = 1.0  # Damping - Amount of speed lost per second
PLAYER_DAMPING = 1
PLAYER_FRICTOIN = 1
FLOOR_FRICTION = 1
WALL_FRICTION = 0.7
DYNAMIC_ITEM_FRICTION = 0.6
PLAYER_MAX_VX = 450
PLAYER_MAX_VY = 1400

# Player forces
PLAYER_MOVE_FORCE_GROUND = 5000
PLAYER_MOVE_FORCE_AIR = PLAYER_MOVE_FORCE_GROUND   # Less horizontal force
PLAYER_JUMP_IMPULSE = 1900
PLAYER_PUNCH_FORCE = 600

DISTANCE_PER_FRAME = 2
ZONE_NO_ANIMATION = 0.1

# Blocks are 64 x 64 pixels
BLOCK_SIZE = 64
# Scale tiles and entity
SCALING_ENTITY = 1.4
SCALING_TILES = 1
# Scaled sprite size for tiles
SPRITE_SIZE = int(BLOCK_SIZE * SCALING_TILES)
# Custom level's width in blocks - this shouldn't be a constant
LEVEL_WIDTH = SPRITE_SIZE * 100
# Distance from left, right, top, bottom for us to start scrolling viewport.
VIEWPORT_MARGIN = 300
