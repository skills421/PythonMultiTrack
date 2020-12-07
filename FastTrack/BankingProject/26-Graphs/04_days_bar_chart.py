from matplotlib import pyplot as plt
from calendar import monthrange
from calendar import month_name

fig, ax = plt.subplots()
#
# data
#

month_nos = [x for x in range(1, 13)]
days_in_month = [monthrange(2020, x)[1] for x in month_nos]
month_names = [month_name[x][:3] for x in month_nos]

#
# plot
#

bar_plot = plt.bar(month_nos, days_in_month, tick_label=month_names)

#
# labels
#

def label_bars_inside_level():
    for idx, rect in enumerate(bar_plot):
        height = rect.get_height()
        x = rect.get_x()
        width = rect.get_width()
        ax.text(x+width/2.0, 25, days_in_month[idx], ha='center', va='bottom',
                bbox=dict(facecolor='white', alpha=0.5))


label_bars_inside_level()

plt.title('Days in the month')
plt.ylabel('days in month')
plt.xlabel('month')

plt.show()