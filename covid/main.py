import pandas as pd
import plotly.express as px

df1 = pd.read_csv("covid.csv")
figure1 = px.scatter(df1,x="date",y="cases",color="country",title="cases of covid ")
figure1.show()