import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "Hiragino Sans"
plt.rcParams["axes.unicode_minus"] = False

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

plt.figure(figsize=(12, 6))
plt.plot(df["年月日"], df["平均気温(℃)"], label="平均気温 (℃)", color="orange")
plt.xlabel("日付")
plt.ylabel("気温 (℃)")
plt.title("神戸の平均気温の推移")
plt.grid(True)
plt.legend()
plt.tight_layout()

output_png = "temperature.png"
plt.savefig(output_png, dpi=150)
print(f"Saved graph to {output_png}")
