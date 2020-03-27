# Write a program that displays a plot of the functions
# f(x)=x, g(x)=x**2 and h(x)=x**3 in the range [0, 4]
# on the one set of axes.

# Import numpy to create arrays
# that can be easily manipulated.
import numpy as np
# import matplotlib.pyplot to create graphs.
import matplotlib.pyplot as plt
# create array of values that function
# will be applied to, with the resulting
# array plotted against the original array.
# Originally I went in steps of one here, but
# steps of 0.5 are probably better considering
# the small range of values.
values = np.arange(0, 4, 0.5)
# The plt.plot() method creates an Axes object
# (in English, a plotting of x and y values)
# for the current Figure object
# (in English, the space that the plot appears on - the plot-space),
# and if there is no Figure object, it will create one.
# Consider this from https://realpython.com/python-matplotlib-guide/

# "Almost all functions from pyplot, such as plt.plot(),
# are implicitly either referring to an existing current Figure
# and current Axes, or creating them anew if none exist.
# [...] with plt.plot() and other top-level pyplot functions
# [... t]here is only ever one Figure or Axes that you’re
# manipulating at a given time, and you don’t need
# to explicitly refer to it."

# This means that we do not need to explicitly assign
# the result of plot() to a variable, because the assignment
# occurs implicitly anyway. When plot() is called the second time,
# it will create another plot on the same plot-space
# because it will use the current (the same) Figure object.
# the 'label' argument will store the values for the legend
plt.plot(values, values, label = 'f(x)=x')
plt.plot(values, values**2, label = 'f(x)=x**2')
plt.plot(values, values**3, label = 'f(x)=x**3')
# title() creates a title
plt.title('Week 8 Assignment')
# legend() will include the 'labels' above in a legend,
# and the 'loc' keyword argument determines
# where the legend is positioned.
plt.legend(loc='upper left')
# Finally, show() will display this Figure object to the user.
plt.show()
plt.savefig("Week8-plots.jpg")
