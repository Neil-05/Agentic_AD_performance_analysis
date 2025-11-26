import pandas as pd

class DataAgent:
  

    def load_data(self, path: str):
        df = pd.read_csv(path)
        return df

    def summarize(self, df):
        summary = {
            "date_range": [df["date"].min(), df["date"].max()],
            "total_spend": float(df["spend"].sum()),
            "avg_ctr": float(df["ctr"].mean()),
            "avg_roas": float(df["roas"].mean()),
            "top_countries": df["country"].value_counts().head(5).to_dict()
        }
        return summary
