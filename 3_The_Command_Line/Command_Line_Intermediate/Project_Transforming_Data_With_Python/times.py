from aux import load_data, extract_hour

df = load_data()

# find most common hours (in UTC)
df['hour'] = df['submission_time'].apply(extract_hour)
hrs = df['hour'].value_counts()
print(hrs[:3])

