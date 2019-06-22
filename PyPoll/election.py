import pandas as pd
import numpy as np
import statistics

csv_path = "/Users/lcambero/Desktop/JyNote/PyPoll/election_data.csv"
elections_df = pd.read_csv(csv_path)
elections_df.head()

votes_df = elections_df['Voter ID'].count()
votes_df

candidate_df = pd.Index(elections_df["Candidate"])
candidate_df.value_counts()

df1 = pd.DataFrame(candidate_df,columns=['Candidate'])
df1.head()

df1 = pd.DataFrame(candidate_df.value_counts())
df1.head()

df1_percentage = df1['Candidate']/df1['Candidate'].sum()*100
df1_percentage.head()

df2 = pd.DataFrame(df1_percentage.head())
df2.head()


print("\nElection Results\n----------------------------------")
print(f"Total Votes: {votes_df}")
print("----------------------------------")
print(candidate_df.value_counts())
print("----------------------------------")
print("Percentage")
print(df1_percentage.head())

file = open("elections.txt","w+")

file.write("\nElection Results\n----------------------------------")
file.write(f"Total Votes: {votes_df}")
file.write("----------------------------------")
file.write(f"candidate_df.value_counts()")
file.write("----------------------------------")
file.write("Percentage")
file.write(f"df1_percentage.head()")

file.close()
