c = 0
for celsius in range(21):
    f = 1.8 * c + 32
    print(f"\033[92mCelsius: \033[1m{c} | \033[0m\033[94mFahrenheit: \033[1m{f:.1f} \033[0m\n")
    c += 1