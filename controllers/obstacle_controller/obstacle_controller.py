from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# ======================
# SENSORS
# ======================
ps = []
ps_names = ['ps0','ps1','ps2','ps3','ps4','ps5','ps6','ps7']

for name in ps_names:
    sensor = robot.getDevice(name)
    sensor.enable(timestep)
    ps.append(sensor)

# ======================
# MOTORS
# ======================
left_motor = robot.getDevice("left wheel motor")
right_motor = robot.getDevice("right wheel motor")

left_motor.setPosition(float('inf'))
right_motor.setPosition(float('inf'))

# ======================
# SPEED
# ======================
BASE_SPEED = 3.0
TURN_SPEED = 3.2

# ======================
# THRESHOLDS
# ======================
FRONT_BLOCK = 90
SIDE_BLOCK = 80

# ======================
# STATE
# ======================
mode = "MAZE"
exit_counter = 0

# ======================
# MAIN LOOP
# ======================
while robot.step(timestep) != -1:

    ps_values = [ps[i].getValue() for i in range(8)]

    front = max(ps_values[0], ps_values[7])
    right = max(ps_values[1], ps_values[2])
    left  = max(ps_values[5], ps_values[6])

    print("F:", front, "R:", right, "L:", left, "| C:", exit_counter)

    # ======================
    # EXIT DETECTION
    # ======================
    right_wall = right > SIDE_BLOCK
    front_clear = front < FRONT_BLOCK

    if not right_wall and front_clear:
        exit_counter += 1
    else:
        exit_counter = 0

    if exit_counter > 1400:
        print("MAZE SOLVED!")
        mode = "OPEN"

    # ======================
    # OPEN MODE
    # ======================
    if mode == "OPEN":
        left_motor.setVelocity(BASE_SPEED)
        right_motor.setVelocity(BASE_SPEED)

        for _ in range(30):
            robot.step(timestep)

        left_motor.setVelocity(0)
        right_motor.setVelocity(0)
        break

    # ======================
    # BEHAVIOUR
    # ======================

    if front > FRONT_BLOCK:
        left_motor.setVelocity(-TURN_SPEED)
        right_motor.setVelocity(TURN_SPEED)
        continue

    if right > SIDE_BLOCK and left > SIDE_BLOCK:
        left_motor.setVelocity(BASE_SPEED)
        right_motor.setVelocity(BASE_SPEED * 0.7)
        continue

    if right > SIDE_BLOCK:
        left_motor.setVelocity(BASE_SPEED * 0.5)
        right_motor.setVelocity(BASE_SPEED)
        continue

    if left > SIDE_BLOCK:
        left_motor.setVelocity(BASE_SPEED)
        right_motor.setVelocity(BASE_SPEED * 0.5)
        continue

    left_motor.setVelocity(BASE_SPEED)
    right_motor.setVelocity(BASE_SPEED)