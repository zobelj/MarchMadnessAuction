from teams import *
import sqlite3
import pandas
import matplotlib.pyplot as plt
import pandas
import seaborn as sns

import pandas as pd
import sqlite3
conn = sqlite3.connect('march_madness_pre.db')
c = conn.cursor()
df = pd.read_sql_query("SELECT * FROM march_madness_pre_team_pts", conn)
#change column names to get rid of the _pts part at the end of each one
for column in df.columns:
    df.rename(columns={column: column[:-4]}, inplace=True)
#order the columns of the df in order of mean
df = df.reindex(df.mean().sort_values(ascending=False).index, axis=1)
#create a violin plot of each of the columns in the dataframe using sns. do not show anything extreme values
#re-write above code but make the graph larger vertically
#re-write above code to add more spacing between each one
sns.violinplot(data=df, inner="quartile", scale = "count", cut = 0, orient = "h", bw=.2, width = 1)
#add more spacing between each one
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)
# add even more spacing between each one
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1, hspace = 0.5)
#make the graph larger vertically
#make font of x axis labels larger
plt.xticks(fontsize=20)
#make font of y axis labels larger

plt.gcf().set_size_inches(40, 40)
plt.savefig('march_madness_pre_team_pts.png')
plt.show()
