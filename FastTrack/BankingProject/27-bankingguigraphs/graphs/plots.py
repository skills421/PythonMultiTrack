from matplotlib import pyplot as plt

def plot_pie_chart(credits:float, debits:float):
    fig = plt.figure()

    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    types = ['Credits', 'Debits']
    amounts = [credits, -debits]

    ax.pie(amounts, labels=types, autopct='%1.2f%%')

    return fig;

