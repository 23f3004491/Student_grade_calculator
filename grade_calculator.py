import pandas as pd 
import numpy as np 
df = pd.read_csv("students.csv")
print('Shape:', df.shape)
df.columns= [col.strip().lower() for col in df.columns]
subject= df.columns[1:]
df['total'] = df[subject].sum(axis=1)
df['average']= (df['total']/len(subject)).round(2)

def assign_grade(avg):
    if avg>=90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'F'
    
    
df['grade'] = df['average'].apply(assign_grade)

max_avg = df['average'].max()
toppers = df[df['average'] == max_avg]['name'].tolist()

failures = df[df['grade'] == 'F']['name'].tolist()

df.to_csv("results.csv", index=False)

print(f"Total students processed: {len(df)}")
print(f"Topper(s): {', '.join(toppers)} (Avg: {max_avg})")
print(f"Failures ({len(failures)}): {', '.join(failures)}")
print("\nFirst 5 results:")
print(df.head())