import pandas as pd
import time
from loguru import logger

REQUIRED_COLUMNS = ["date", "country", "spend", "ctr", "roas", "campaign", "message"]

COLUMN_MAP = {
    "campaign_name": "campaign",
    "creative_message": "message",
}


class DataAgent:
    def load_data(self, path, retries=3, delay=1):
        logger.bind(agent="data", step="load_start", path=path).info("Loading data")

        last_error = None

        for attempt in range(1, retries + 1):
            try:
                df = pd.read_csv(path)
                if df.empty:
                    raise ValueError("Dataset is empty")

                # Normalize column names
                df = df.rename(columns=COLUMN_MAP)

                # Schema check
                missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
                if missing_cols:
                    raise KeyError(f"Missing required columns: {missing_cols}")

                # Numeric validation
                for col in ["spend", "ctr", "roas"]:
                    df[col] = pd.to_numeric(df[col], errors="raise")

                logger.bind(agent="data", step="load_success", rows=len(df)).info("Data loaded")
                return df

            except Exception as e:
                last_error = e
                logger.bind(agent="data", step="load_retry", attempt=attempt, error=str(e)).warning(
                    "Load failed — retrying"
                )
                time.sleep(delay)

        logger.bind(agent="data", step="load_failed").error("Failed after retries")
        raise last_error

    def summarize(self, df):
        return {
            "date_range": [df["date"].min(), df["date"].max()],
            "total_spend": float(df["spend"].sum()),
            "avg_ctr": float(df["ctr"].mean()),
            "avg_roas": float(df["roas"].mean()),
            "top_countries": df["country"].value_counts().head(3).to_dict(),
        }

 
    def compute_deltas(self, df):
     
        logger.info("Computing baseline vs current performance")

      
        mid = len(df) // 2
        baseline = df.iloc[:mid]
        current = df.iloc[mid:]

        def avg_metrics(d):
            return {
                "ctr": d["ctr"].mean(),
                "roas": d["roas"].mean(),
                "spend": d["spend"].mean(),
            }

        base = avg_metrics(baseline)
        curr = avg_metrics(current)

   
        deltas = {
            "ctr_delta_pct": ((curr["ctr"] - base["ctr"]) / base["ctr"]) * 100 if base["ctr"] != 0 else 0,
            "roas_delta_pct": ((curr["roas"] - base["roas"]) / base["roas"]) * 100 if base["roas"] != 0 else 0,
            "spend_delta_pct": ((curr["spend"] - base["spend"]) / base["spend"]) * 100 if base["spend"] != 0 else 0,
        }
        seg = (
            df.groupby("country")["ctr"]
            .mean()
            .sort_values()
            .to_dict()
        )

        return {
            "baseline": base,
            "current": curr,
            "deltas": deltas,
            "segment_ctr": seg
        }
