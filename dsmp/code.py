# --------------
import pandas as pd
import numpy as np
bank=pd.read_csv(path)

categorical_var=bank.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print('numerical_var')


# --------------
# code starts here
banks=bank.drop('Loan_ID', axis=1)
print(banks.isnull().sum())
bank_mode=banks.mode()
banks['Gender'].fillna(bank_mode['Gender'][0],inplace=True)
banks['Married'].fillna(bank_mode['Married'][0],inplace=True)
banks['Dependents'].fillna(bank_mode['Dependents'][0],inplace=True)
banks['Education'].fillna(bank_mode['Education'][0],inplace=True)
banks['Self_Employed'].fillna(bank_mode['Self_Employed'][0],inplace=True)
banks['ApplicantIncome'].fillna(bank_mode['ApplicantIncome'][0],inplace=True)
banks['CoapplicantIncome'].fillna(bank_mode['CoapplicantIncome'][0],inplace=True)
banks['LoanAmount'].fillna(bank_mode['LoanAmount'][0],inplace=True)
banks['Loan_Amount_Term'].fillna(bank_mode['Loan_Amount_Term'][0],inplace=True)
banks['Credit_History'].fillna(bank_mode['Credit_History'][0],inplace=True)
banks['Property_Area'].fillna(bank_mode['Property_Area'][0],inplace=True)
banks['Loan_Status'].fillna(bank_mode['Loan_Status'][0],inplace=True)
print(banks)
#code ends here


# --------------
# Code starts here
avg_loan_amount=pd.pivot_table(banks,values='LoanAmount',index=['Gender','Married','Self_Employed'],aggfunc=np.mean)



# code ends here



# --------------
# code starts here
loan_approved_se=len(banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')])
loan_approved_nse=len(banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')])
print(loan_approved_se)
print(loan_approved_nse)
percentage_se=(loan_approved_se/614)*100
percentage_nse=(loan_approved_nse/614)*100
print(percentage_se)
print(percentage_nse)
# code ends here


# --------------
# code starts here
loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=sum(loan_term>=25)
print(big_loan_term)





# code ends here


# --------------
# code starts here
loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['Loan_Status','ApplicantIncome', 'Credit_History']
mean_values=loan_groupby.mean()



# code ends here


