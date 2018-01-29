from ple.games.flappybird import FlappyBird
from ple import PLE
from humanagent import HumanAgent

game = FlappyBird()
p = PLE(game, fps=30, display_screen=True)
agent = HumanAgent(allowed_actions=p.getActionSet())

p.init()
reward = 0.0

nb_frames = 100
for i in range(nb_frames):
    if p.game_over():
        p.reset_game()
    observation = p.getScreenRGB()
    action = agent.pickAction(reward, observation)
    reward = p.act(action)
