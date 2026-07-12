import pandas as pd
import plotly.express as px

csv_path = "kobe.csv"

df = pd.read_csv(
    csv_path,
    encoding="shift_jis",
    skiprows=[0, 1, 2, 4, 5],
    header=0,
)

df = df[["年月日", "平均気温(℃)"]]
df["年月日"] = pd.to_datetime(df["年月日"], format="%Y/%m/%d", errors="coerce")
df["平均気温(℃)"] = pd.to_numeric(df["平均気温(℃)"], errors="coerce")
df = df.dropna(subset=["年月日", "平均気温(℃)"])

fig = px.line(
    df,
    x="年月日",
    y="平均気温(℃)",
    title="神戸の平均気温の推移",
    labels={
        "年月日": "日付",
        "平均気温(℃)": "平均気温 (℃)",
    },
)

fig.update_traces(
    mode="lines+markers",
    hovertemplate="日付: %{x|%Y-%m-%d}<br>気温: %{y} ℃<extra></extra>",
)

fig.update_layout(
    xaxis=dict(showgrid=True),
    yaxis=dict(showgrid=True),
    font=dict(family="Hiragino Sans, Meiryo, sans-serif"),
)

output_html = "temperature.html"
fig.write_html(output_html, include_plotlyjs="cdn")
print(f"Saved interactive plot to {output_html}")
