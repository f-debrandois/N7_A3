def print_decision_boundaries(model, x, y):
    # make these smaller to increase the resolution
    dx, dy = 0.1, 0.1

    # generate 2 2d grids for the x & y bounds
    y_grid, x_grid = np.mgrid[slice(-4, 4 + dy, dy), slice(-4, 4 + dx, dx)]

    x_gen = np.concatenate((np.expand_dims(np.reshape(y_grid, (-1)),1),np.expand_dims(np.reshape(x_grid, (-1)),1)), axis=1)
    z_gen = model.forward(np.transpose(x_gen)).reshape(x_grid.shape)

    z_min, z_max = 0, 1

    c = plt.pcolor(x_grid, y_grid, z_gen, cmap='RdBu', vmin=z_min, vmax=z_max)
    plt.colorbar(c)
    plt.plot(x[y==0,0], x[y==0,1], 'r.')
    plt.plot(x[y==1,0], x[y==1,1], 'b.')
    plt.show()