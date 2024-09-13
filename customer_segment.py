import streamlit as st
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset 
# If your data is stored in a CSV file
df = pd.read_csv('altered_marketing_campaign1.csv')  # Make sure this file is in the same directory or provide the correct path

# Display the first few rows of the dataset
#st.subheader('Dataset Preview')
#st.write(df.head())
st.title('CUSTOMER PERSONALITY ANALYSIS')

select_val = st.selectbox('select',['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds'])

# Extracting the relevant columns for plotting
mnt_fruits = df['MntFruits']
spent = df['Income']  # Assuming 'spent' is the column name for Total Amount Spent


st.subheader(f'Total Amount Spent vs {select_val}')
fig, ax = plt.subplots()
sns.kdeplot(y=df[select_val],x=df['Spent'],hue=df['Cluster'],fill=False,ax=ax,palette='bright')
ax.set_title(f'Spent vs. {select_val}')
st.pyplot(fig)


# grouping
grp = df.groupby('Cluster')
for l,r in grp:
	st.write(l)
	st.write('*************************************************************')
	st.write(r)






