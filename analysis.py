"Create time series plots."
import pandas as pd
import seaborn as sns

sns.set_theme(
    style="whitegrid",
    palette="ch:s=.5,r=-.5",
    rc={"figure.figsize": (30, 10)},
)

DATE_COLUMN = "Datum (Anlage)"
TIMESTAMP_COLUMN = "Zeit (Anlage)"

df = pd.read_csv(
    "output.csv",
    sep=";",
    decimal=",",
    parse_dates=[DATE_COLUMN, TIMESTAMP_COLUMN],
)

df.sort_values(TIMESTAMP_COLUMN, inplace=True)
df.reset_index(drop=True, inplace=True)

for i, feature in enumerate(df.columns.values):
    if feature in [DATE_COLUMN, TIMESTAMP_COLUMN]:
        continue

    print(f"Plotting {feature=}, {i+1} of {len(df.columns.values)}")

    plot = sns.lineplot(x=df[DATE_COLUMN], y=df[feature])
    plot.set(title=feature)
    plot.set_xticklabels(
        plot.get_xticklabels(),
        rotation=45,
        horizontalalignment="right",
    )
    fig = plot.get_figure()
    fig.tight_layout()
    fig.savefig(f"plots/{feature}.png", format="png")
    fig.clear()

print("All plots created.")
