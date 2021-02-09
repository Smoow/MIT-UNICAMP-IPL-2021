interest_rate = 0.05
starting_value = 100

if interest_rate == 0:
    out = "NEVER"
else:
    # Para dobrar em tempo t, precisamos 2 <= (1 + r) ** t
    total = starting_value
    timesteps = 0

    while total < 2 * starting_value:
        total *= 1 + interest_rate
        timesteps += 1

    out = timesteps
