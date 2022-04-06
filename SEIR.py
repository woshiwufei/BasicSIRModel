import matplotlib.pyplot as plt


def diffusion(s, e, i, r, β, γ):
    ds = (s[-1] * i[-1] * β) / 1000
    di = (i[-1] * γ)
    de = e[-1] / hidden_time
    s.append(s[-1] - ds)
    e.append(e[-1] + ds - de)
    i.append(i[-1] + de - di)
    r.append(1000 - s[-1] - i[-1] - e[-1])


if __name__ == '__main__':
    suspect = [950]
    exposed = [1]
    hidden_time = 14
    infected = [48]
    recovery = [0]
    beta = 0.05
    gamma = 0.01
    days = 1000

    for day in range(days):
        diffusion(suspect, exposed, infected, recovery, beta, gamma)

    print('suspect: ', suspect, '\nexposed: ', exposed, '\ninfected: ', infected, '\nrecovery: ', recovery)

    plt.plot(suspect, color='blue', label='suspect')
    plt.plot(exposed, color='black', label='exposed')
    plt.plot(infected, color='red', label='infected')
    plt.plot(recovery, color='green', label='recovery')
    plt.legend()
    plt.savefig('./result_img/SEIR.png')
    plt.show()
