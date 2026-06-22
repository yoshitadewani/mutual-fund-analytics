import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        print("\n" + "="*60)
        print("FILE:", file)

        try:
            df = pd.read_csv(os.path.join(folder_path, file))

            print("Shape:", df.shape)

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print("Error reading file:", e)