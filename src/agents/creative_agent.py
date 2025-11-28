class CreativeAgent:
    def generate_creatives(self, df):
        low_ctr_ads = df[df["ctr"] < 0.015].head(5)
        results = []
        for _, row in low_ctr_ads.iterrows():
            campaign_name = row.get("campaign_name", row.get("campaign", "Unknown Campaign"))
            old_msg = row.get("creative_message", row.get("message", ""))

            results.append({
                "campaign": campaign_name,
                "old_message": old_msg,
                "new_creatives": [
                    f"Try highlighting benefits: {old_msg}",
                    "Add urgency-based CTA: 'Limited Time Offer!'",
                    "Use more emotional storytelling in copy"
                ]
            })
        return results
