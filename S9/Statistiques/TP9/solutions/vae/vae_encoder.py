# Input layer
inputs = kl.Input(shape=(input_dim,), name='encoder_input')

# Dense layer from input layer
x = kl.Dense(intermediate_dim, activation='relu')(inputs)

# Two dense layer that takes input from the same layer x
z_mean = kl.Dense(latent_dim, name='z_mean')(x)
z_log_var = kl.Dense(latent_dim, name='z_log_var')(x)