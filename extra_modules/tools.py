import numpy as np
import matplotlib.pyplot as plt


def display_rows_as_images(X, example_width=None, subplots_rows_cols=None, fig_multipliers=(1, 1), reshape_order='C'):
    """
    Displays 2D data stored in X in a nice grid.
    """
    # Compute rows, cols
    if X.ndim == 2:
        m, n = X.shape
    elif X.ndim == 1:
        n = X.size
        m = 1
        X = X[None]  # Promote to a 2 dimensional array
    else:
        raise IndexError('Input X should be 1 or 2 dimensional.')

    example_width = example_width or int(np.round(np.sqrt(n)))
    example_height = n / example_width

    # Compute number of items to display
    if subplots_rows_cols is None:
        subplots_rows = int(np.floor(np.sqrt(m)))
        subplots_cols = int(np.ceil(m / subplots_rows))
    else:
        subplots_rows, subplots_cols = subplots_rows_cols
    # creating subplots
    figsize = (subplots_cols * fig_multipliers[0], subplots_rows * fig_multipliers[1])
    fig, ax_array = plt.subplots(subplots_rows, subplots_cols, figsize=figsize)
    fig.subplots_adjust(wspace=0.025, hspace=0.025)

    ax_array = [ax_array] if m == 1 else ax_array.ravel()

    for i, ax in enumerate(ax_array):
        # Display Image
        h = ax.imshow(X[i].reshape(example_width, example_width, order=reshape_order),
                      cmap='Greys', extent=[0, 1, 0, 1])
        ax.axis('off')
    return  fig, ax_array


