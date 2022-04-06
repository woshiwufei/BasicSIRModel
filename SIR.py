import matplotlib.pyplot as plt


def diffusion(s, i, r, β, γ):
    ds = (s[-1] * i[-1] * β) / 1000
    di = (i[-1] * γ)
    s.append(s[-1] - ds)
    i.append(i[-1] + ds - di)
    r.append(1000 - s[-1] - i[-1])


if __name__ == '__main__':
    suspect = [950]
    infected = [50]
    recovery = [0]
    beta = 0.05
    gamma = 0.01
    days = 1000

    for day in range(days):
        diffusion(suspect, infected, recovery, beta, gamma)
    print('suspect: ', suspect, '\ninfected: ', infected, '\nrecovery: ', recovery)

    plt.plot(suspect, color='blue', label='suspect')
    plt.plot(infected, color='red', label='infected')
    plt.plot(recovery, color='green', label='recovery')
    plt.legend()
    plt.savefig('./result_img/SIR.png')
    plt.show()
