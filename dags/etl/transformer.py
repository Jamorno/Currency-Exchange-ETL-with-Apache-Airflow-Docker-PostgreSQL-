import logging
import pandas as pd

class DataTransform:
    def transform_data(self, raw_data):
        try:
            updated = pd.to_datetime(raw_data.get("time_next_update_utc"))
            base = raw_data.get("base_code")
            rates = raw_data.get("rates", {})

            records = []
            for currency, value in rates.items():
                records.append({
                    "updated": updated,
                    "base_currency": base,
                    "target_currency": currency,
                    "exchange_rate": value
                })

            df = pd.DataFrame(records)
            logging.info(f"Transformed {len(df)} records.")
            return df

        except Exception as e:
            logging.error(f"DEBUG: Failed to transform data: {e}")
            return pd.DataFrame()