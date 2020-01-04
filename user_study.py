# -*- coding: utf-8 -*-
import gym
import gym_maze
import keyboard
import numpy as np

if __name__ == '__main__':
    # for i in range(100):
    i = 3
    env = gym.make('maze-sample-5x5-v0', maze_file="maze2d_5x5-v3.npy")
    # env.maze_view.maze.save_maze(f'samples\\maze2d_5x5-v{i}.npy')

    arrows = dict(up=0, down=1, right=2, left=3)
    env.reset()
    env.render()
    # with open('gym-maze\\gym_maze\\envs\\maze_samples\\maze2d_5x5.npy', 'rb') as f:
    #     a = np.load(f)
    #     print(a)
    #     # 0101
    while True:
        key = keyboard.read_hotkey(suppress=False)
        print(key)
        if key == 'esc':
            break
        if key not in arrows.keys():
            continue
        # action = int(input('ENTER DIRECTION STEP (UP=1, DOWN=2, RIGHT=3, LEFT=4): ')) - 1
        ns, r, d, _ = env.step(arrows[key])
        env.render()
