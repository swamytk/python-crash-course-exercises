import plotly.express as px
from die import Die

# Create two dies
die_1 = Die()   # 6 faces
die_2 = Die(10) # 10 faces

# Roll and save
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the result
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results as histogram
title = 'Results of rolling D6 and D10 dies for 50,000 times'
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.write_html('dice_visual_d6d10.html')
fig.show()




