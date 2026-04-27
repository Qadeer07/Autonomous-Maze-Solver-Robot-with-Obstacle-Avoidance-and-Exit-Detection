# Autonomous Maze Solver Robot with Obstacle Avoidance and Exit Detection

This project is an autonomous maze-solving robot developed using Python in the Webots simulation environment. The robot is designed to navigate through a maze without human control by using proximity sensors for obstacle detection and wall-following navigation.

##Project Overview

The robot uses a right-hand wall-following algorithm to move through the maze while avoiding collisions. It continuously reads sensor data and makes real-time decisions to adjust movement. An exit detection mechanism is also implemented to identify when the robot has successfully exited the maze.

## Features

- Autonomous maze navigation  
- Obstacle avoidance using proximity sensors  
- Right-hand wall-following algorithm  
- Real-time sensor-based decision making  
- Exit detection system  
- Smooth motor speed control  

## Technologies Used

- Python  
- Webots Simulator  
- e-puck Robot Model  
- Webots Controller API  

## Project Structure

```text
obstacle_avoidance_robot/
├── controllers/
│   └── obstacle_controller/
│       └── obstacle_controller.py
├── worlds/
│   └── obstacle_world.wbt
```

## How It Works

1. The robot reads data from proximity sensors.  
2. Sensor values are grouped into front, left, and right directions.  
3. The robot checks for obstacles and walls.  
4. It follows the right wall to navigate the maze.  
5. If the front is blocked, it rotates to avoid collision.  
6. If open space is detected for a continuous period, the robot identifies the maze exit.  

## Results

The robot successfully navigates through the maze, avoids obstacles, follows walls, and detects the maze exit in simulation.

## Author

Muhammad Qadeer
