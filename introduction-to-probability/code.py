# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df = pd.read_csv(path)
p_a = len(df[df['fico']>700])/len(df)
p_b = len(df[df['purpose'] == 'debt_consolidation'])/len(df)
df1 = df[df['purpose'] == 'debt_consolidation']
p_a_b = (p_a + p_b) / p_b
result = (p_a_b == p_a)
print(result)
# code ends here


# --------------
# code starts here
# print(len(df))
# print(len(df[df['paid.back.loan']== 'Yes']))
prob_lp=len(df[df['paid.back.loan']== 'Yes'])/len(df)
print(prob_lp)
prob_cs=len(df[df['credit.policy']== 'Yes'])/len(df)
print(prob_cs)
new_df=df[df['paid.back.loan'] == 'Yes']
prob_pd_cs=len(new_df[new_df['credit.policy'] == 'Yes'])/len(new_df)
print(prob_pd_cs)
bayes=prob_pd_cs*prob_lp / prob_cs
print(bayes)
# code ends here
# print(df[df['paid.back.loan'] == 'Yes'].shape[0] )
# prob_lp = df[df['paid.back.loan'] == 'Yes'].shape[0] / df.shape[0]
# prob_cs = df[df['credit.policy'] == 'Yes'].shape[0] / df.shape[0]
# new_df = df[df['paid.back.loan'] == 'Yes']
# prob_pd_cs = new_df[new_df['credit.policy'] == 'Yes'].shape[0] / new_df.shape[0]
# print(prob_pd_cs)
# bayes = (prob_pd_cs * prob_lp)/ prob_cs
# print(bayes)


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar',width=0.3)
plt.show()
df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar',width=0.3)
plt.show()
# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
inst_mean=df['installment'].mean()
df['installment'].plot(kind='hist')
plt.show()
df['log.annual.inc'].plot(kind='hist')
plt.show()
# code ends here


