kwh_used = 1000


if kwh_used <= 500:
    out = (0.45 * kwh_used) * 1.2
elif kwh_used <= 1500:
    out = ((0.45 * 500) + ((kwh_used - 500) * 0.74)) * 1.2
elif kwh_used <= 2500:
    out = ((0.45 * 500) + ((kwh_used - 500) * 0.74) + (kwh_used - 1500) * 1.25) * 1.2
else:
    out = ((0.45 * 500) + ((kwh_used - 500) * 0.74) + ((kwh_used - 1500) * 1.25) + ((kwh_used - 2500)) * 2) * 1.2

print(out)
