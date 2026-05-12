"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
import numpy as np


def visualize(data_dict, outfile):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    if outfile:
        plt.savefig(outfile)
    else:
        fig.tight_layout()          # this command triggers the show
        plt.show()