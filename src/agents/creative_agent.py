class CreativeAgent:
 

    def generate_creatives(self, df):
        low_ctr_ads = df[df["ctr"] < 0.015].head(5)

        results = []

        for _, row in low_ctr_ads.iterrows():
            results.append({
                "campaign": row["campaign_name"],
                "old_message": row["creative_message"],
                "new_creatives": [
                    f"Try highlighting benefits: {row['creative_message']}",
                    "Add urgency-based CTA: 'Limited Time Offer!'",
                    "Use more emotional storytelling in copy"
                ]
            })

        return results
