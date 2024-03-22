### Author: KaruppuSwamy Thangaraj ###
### Date: 10-Mar-2024              ###

''' Plot of cubic numbers '''
import matplotlib.pyplot as plt

# Data X and its cube values in lists
x_val = range(1,5001)
y_val = [x**3 for x in x_val]

# Get empty plots
fig, ax = plt.subplots()

# Set attributes of plot
plt.style.use('seaborn')

# Option-1: Generating a subplot without colormap
#ax.scatter(x_val, y_val)

# Option-2: Generating a subplot with colormap
# Reference: https://saturncloud.io/blog/matplotlib-plot-lines-with-colors-through-colormap-a-guide/
col_map = plt.get_cmap('ocean')
normalized = plt.Normalize(min(y_val), max(y_val))
line_colors = col_map(normalized(y_val))
ax.scatter(x_val, y_val, color=line_colors)

# Set attributes of subplot
ax.set_title("Cube series")
ax.set_xlabel("X value")
ax.set_ylabel("Cube of X")
ax.axis([0,5001, 0, 5001**3])

# This is tricky - without below formatting, 
#   the y lable will be in scientifc notation
ax.ticklabel_format(style='plain', useLocale=False)

# Save the figure as image file
plt.savefig('cube_series.png')

# Display plot
plt.show()



