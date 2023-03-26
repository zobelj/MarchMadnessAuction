import matplotlib.pyplot as plt
from numpy import var
import seaborn as sns

from lib.database import run_query

def violin_plot(school_version = False, i=0, is_pre=False):
    # build query
    tourney_table = 'tourney_results_pre' if is_pre else 'tourney_results'
    schools_table = 'schools_pts_pre' if is_pre else 'schools_pts'

    if not school_version:
        query = f"SELECT Devan_pts, Jeremy_pts, Josh_pts, Justin_pts, Brant_pts, Nick_pts, Joe_pts FROM {tourney_table}"
        outfile = f"violin_figs/violin_school_{'pre' if is_pre else f'{i}'}.png"
    else: 
        query = f"SELECT * from {schools_table}"
        outfile = f"violin_figs/violin_tourney_{'pre' if is_pre else f'{i}'}.png" 

    # execute query
    df = run_query(query, fetch="sql")

    # change column names to get rid of the _pts part at the end of each one
    for column in df.columns:
        df.rename(columns={column: column[:-4]}, inplace=True)
    #order the columns of the df in order of mean
    df = df.reindex(df.mean().sort_values(ascending=False).index, axis=1)
    sns.violinplot(data=df, inner="quartile", scale = "count", cut = 0, orient = "h", bw=.2, width = 1)
    plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1, hspace = 0.5)
    plt.xticks(fontsize=20)
    plt.savefig(outfile)
    plt.show()


def density_plot(points_lists, headliner, i, is_pre=False):
    tourney_table = 'tourney_results_pre' if is_pre else 'tourney_results'

    # get the win percentage for each player from the database
    win_pcts = run_query(f'''SELECT (ROUND(100 * AVG(Devan_win), 2) || '%') as Devan_win_pct,
                        (ROUND(100 * AVG(Jeremy_win), 2) || '%') as Jeremy_win_pct,
                        (ROUND(100 * AVG(Josh_win), 2) || '%') as Josh_win_pct,
                        (ROUND(100 * AVG(Brant_win), 2) || '%') as Brant_win_pct,
                        (ROUND(100 * AVG(Nick_win), 2) || '%') as Nick_win_pct,
                        (ROUND(100 * AVG(Joe_win), 2) || '%') as Joe_win_pct
                    FROM {tourney_table}''', fetch="one")

    # convert win_pcts to a dictionary
    win_pcts = dict(zip(["Devan", "Jeremy", "Josh", "Justin", "Brant", "Nick", "Joe"], win_pcts))

    # plot density function for owners with non-zero variance
    legend_list = []
    THICKNESS = 2.5

    Devan = points_lists['Devan']
    Jeremy = points_lists['Jeremy']
    Josh = points_lists['Josh']
    #Justin = points_lists['Justin']
    Brant = points_lists['Brant']
    Nick = points_lists['Nick']
    Joe = points_lists['Joe']

    if(var(Devan)):
        sns.kdeplot(Devan, linewidth=THICKNESS, color="tab:blue")
        legend_list.append(f"Devan:  {win_pcts['Devan']}")

    if(var(Jeremy)):
        sns.kdeplot(Jeremy, linewidth=THICKNESS, color="tab:orange")
        legend_list.append(f"Jeremy:  {win_pcts['Jeremy']}")

    if(var(Josh)):
        sns.kdeplot(Josh, linewidth=THICKNESS, color="tab:green")
        legend_list.append(f"Josh:  {win_pcts['Josh']}")

    # if(var(Justin)):
    #     sns.kdeplot(Justin, linewidth=THICKNESS, color="tab:red")
    #     legend_list.append(f"Justin:  {win_pcts['Justin']}")

    if(var(Brant)):
        sns.kdeplot(Brant, linewidth=THICKNESS, color="tab:purple")
        legend_list.append(f"Brant:  {win_pcts['Brant']}")

    if(var(Nick)):
        sns.kdeplot(Nick, linewidth=THICKNESS, color="tab:brown")
        legend_list.append(f"Nick:  {win_pcts['Nick']}")

    if(var(Joe)):
        sns.kdeplot(Joe, linewidth=THICKNESS, color="tab:pink")
        legend_list.append(f"Joe:  {win_pcts['Joe']}")

    # configure and display plot
    plt.title(headliner)
    plt.xlabel("Points")
    plt.ylabel("")
    plt.yticks([])
    plt.legend(legend_list)
    plt.savefig(f"mm_figs/mm_{i}.png", dpi=300)
    plt.show()


