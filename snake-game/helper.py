from matplotlib import get_backend
import matplotlib.pyplot as plt
from IPython import display
from numpy import block

plt.ion()

def plot(scores, mean_scores, model_name=None):
    print(get_backend())
    plt.clf()
    plt.title('Training ' + model_name + '...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.show(block=False)
    plt.pause(1)
