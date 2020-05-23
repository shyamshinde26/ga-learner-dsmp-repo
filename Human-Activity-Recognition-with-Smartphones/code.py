# --------------
import pandas as pd
from collections import Counter

# Load dataset
data=pd.read_csv(path)
print(data.isnull().sum())
print(data.describe())


# --------------
import seaborn as sns
from matplotlib import pyplot as plt
sns.set_style(style='darkgrid')

# Store the label values 
label=data.iloc[:,-1]
sns.countplot(label)
plt.xticks(rotation=90)

# plot the countplot



# --------------
# make the copy of dataset
data_copy=data.copy()



# Create an empty column 
data_copy['duration']=''


# Calculate the duration
duration_df = (data_copy.groupby([label[label.isin(['WALKING_UPSTAIRS', 'WALKING_DOWNSTAIRS'])], 'subject'])['duration'].count() * 1.28)
duration_df = pd.DataFrame(duration_df)

# Sort the values of duration
plot_data = duration_df.reset_index().sort_values('duration', ascending=False)
plot_data['Activity'] = plot_data['Activity'].map({'WALKING_UPSTAIRS':'Upstairs', 'WALKING_DOWNSTAIRS':'Downstairs'})


# Plot the durations for staircase use
plt.figure(figsize=(15,5))
sns.barplot(data=plot_data, x='subject', y='duration', hue='Activity')
plt.title('Participants Compared By Their Staircase Walking Duration')
plt.xlabel('Participants')
plt.ylabel('Total Duration [s]')
plt.show()




# --------------
#exclude the Activity column and the subject column
feature_cols = data.columns[: -2]   

#Calculate the correlation values
correlated_values = data[feature_cols].corr()
#stack the data and convert to a dataframe

correlated_values = (correlated_values.stack().to_frame().reset_index()
                    .rename(columns={'level_0': 'Feature_1', 'level_1': 'Feature_2', 0:'Correlation_score'}))


#create an abs_correlation column
correlated_values['abs_correlation'] = correlated_values.Correlation_score.abs()

#Picking most correlated features without having self correlated pairs
top_corr_fields = correlated_values.sort_values('Correlation_score', ascending = False).query('abs_correlation>0.8 ')
top_corr_fields = top_corr_fields[top_corr_fields['Feature_1'] != top_corr_fields['Feature_2']].reset_index(drop=True)



# --------------
# importing neccessary libraries
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_recall_fscore_support as error_metric
from sklearn.metrics import confusion_matrix, accuracy_score

# Encoding the target variable
le=LabelEncoder()
data['Activity']=le.fit_transform(data['Activity'])

# split the dataset into train and test
X=data.iloc[:,:-1]
y=data.iloc[:,-1:]

# Baseline model 
X_train, X_test, y_train,y_test=train_test_split(X, y, test_size=0.3)
classifier=SVC()
clf=classifier.fit(X_train, y_train)
y_pred=clf.predict(X_test)
precision, recall, f_score, support = error_metric(y_test, y_pred,average='weighted')
accuracy=accuracy_score(y_test, y_pred)
model1_score=accuracy
print('Precision:',precision)
print('Accuracy:',accuracy)
print('f1_score:',f_score)
print('recall:',recall)


# --------------
# importing libraries
from sklearn.feature_selection import SelectFromModel

from sklearn.svm import LinearSVC

# Feature selection using Linear SVC
lsvc = LinearSVC(C = 0.01, penalty="l1", dual=False, random_state=42).fit(X_train, y_train)
model_2 = SelectFromModel(lsvc, prefit=True)
new_train_features = model_2.transform(X_train)
new_test_features = model_2.transform(X_test)

print(new_train_features.shape,new_test_features.shape )

# model building on reduced set of features
classifier_2 = SVC()
clf_2 = classifier_2.fit(new_train_features, y_train)
y_pred_new = clf_2.predict(new_test_features)
model2_score =accuracy_score(y_test, y_pred_new)
precision, recall, f_score, _ = error_metric(y_test, y_pred_new, average='weighted')
print(model2_score)
print(precision, recall, f_score)


# --------------
# Importing Libraries
from sklearn.model_selection import GridSearchCV

# Set the hyperparmeters
selector=GridSearchCV(estimator=SVC(),scoring='accuracy',param_grid={'kernel': ['linear', 'rbf'],'C': [100, 20, 1, 0.1]})


# Usage of grid search to select the best hyperparmeters
selector.fit(new_train_features,y_train)
parameters=selector.best_params_
means = selector.cv_results_['mean_test_score']
stds = selector.cv_results_['std_test_score']
print(parameters)
print('means:',means)  
print("stds:",stds)
# Model building after Hyperparameter tuning
classifier_3=SVC(C=20, kernel='rbf')
clf_3=classifier_3.fit(new_train_features,y_train)
y_pred_final=clf_3.predict(new_test_features)
precision, recall, f_score, _ = error_metric(y_test, y_pred_new, average='weighted')
model3_score=accuracy_score(y_test, y_pred_final)
print('Precision:',precision)
print('Accuracy:',model3_score)
print('f1_score:',f_score)
print('recall:',recall)






