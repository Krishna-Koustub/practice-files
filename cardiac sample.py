
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# reading the data

data = pd.read_csv('drive/My Drive/Projects/Heart-UCI/heart.csv')

# getting the shape
data.shape

"""**Data Description**
age: The person's age in years
sex: The person's sex (1 = male, 0 = female)
cp: The chest pain experienced (Value 1: typical angina, Value 2: atypical angina, Value 3: non-anginal pain, Value 4: asymptomatic)
trestbps: The person's resting blood pressure (mm Hg on admission to the hospital)
chol: The person's cholesterol measurement in mg/dl
fbs: The person's fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)
restecg: Resting electrocardiographic measurement (0 = normal, 1 = having ST-T wave abnormality, 2 = showing probable or definite left ventricular hypertrophy by Estes' criteria)
thalach: The person's maximum heart rate achieved
exang: Exercise induced angina (1 = yes; 0 = no)
oldpeak: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot. See more here)
slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
ca: The number of major vessels (0-3)
thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)
target: Heart disease (0 = no, 1 = yes)
"""

# reading the head of the data

data.head()

# describing the data

data.describe()

# getting the info of the data

data.info()

# making a pairplot

plt.rcParams['figure.figsize'] = (15, 15)
sns.pairplot(data)

# making a heat map

plt.rcParams['figure.figsize'] = (15, 15)
sns.heatmap(data)

# checking the distribution of age amonng the patients

plt.rcParams['figure.figsize'] = (10, 7)
sns.distplot(data['age'])
plt.title('Distribution of Age')

# checking the values present in sex attribute

data['sex'].value_counts()

# plotting a donut chart for visualizing each of the recruitment channel's share

size = [207, 96]
colors = ['lightblue', 'lightgreen']
labels = "Male", "Female"
explode = [0, 0.01]

my_circle = plt.Circle((0, 0), 0.7, color = 'white')

plt.rcParams['figure.figsize'] = (9, 9)
plt.pie(size, colors = colors, labels = labels, shadow = True, explode = explode, autopct = '%.2f%%')
plt.title('Distribution of Gender', fontsize = 20)
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.legend()
plt.show()

# plotting the target attribute

sns.countplot(data['target'], palette = 'pastel')

# tresbps vs target

sns.boxplot(data['target'], data['trestbps'])
plt.title('Relation of tresbps with target', fontsize = 20)

# cholestrol vs target

sns.violinplot(data['target'], data['chol'], palette = 'colorblind')
plt.title('Relation of Cholestrol with Target', fontsize = 20)

# Resting electrocardiographic measurement vs target

dat = pd.crosstab(data['target'], data['restecg'])
dat.div(dat.sum(1).astype(float), axis = 0).plot(kind = 'bar', stacked = True, figsize = (10, 7), colors = ['pink', 'purple', 'black'])
plt.title('Relation of ECG measurement with Target', fontsize = 20)

# checking the relation bet. thalach and target
# thalach: The person's maximum heart rate achieved

plt.rcParams['figure.figsize'] = (10, 7)
sns.lmplot('target', 'thalach', data = data)
plt.title('Relation between Max Heart rate and target', fontsize = 20)

# exang: Exercise induced angina (1 = yes; 0 = no)

sns.regplot('target', 'exang', data = data)
plt.title('Relation between Max Heart rate and target', fontsize = 20)

# oldpeak: ST depression induced by exercise relative to rest ('ST' relates to positions on the ECG plot. See more here)kkk. . .

plt.rcParams['figure.figsize'] = (10, 7)
sns.heatmap(data[['target', 'oldpeak']])
plt.title('Relation between Max Heart rate and target', fontsize = 20)

# slope: the slope of the peak exercise ST segment (Value 1: upsloping, Value 2: flat, Value 3: downsloping)
# checking the relation between slope and target


sns.boxenplot(data['target'], data['slope'], palette = 'Set1')
plt.title('Relation between Peak Exercise and Target', fontsize = 20)

#ca: The number of major vessels (0-3)

sns.stripplot(data['target'], data['ca'])
plt.title('Relation between no. of major vessels and target', fontsize = 20)

# relation between age and target

sns.swarmplot(data['target'], data['age'], palette = 'dark')
plt.title('Relation of Age and target', fontsize = 20)

# relation between sex and target

sns.boxenplot(data['target'], data['sex'], palette = 'Set3')
plt.title('Relation of Sex and target', fontsize = 20)

# checking the relation between
#thal: A blood disorder called thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)

sns.swarmplot(data['target'], data['thal'], palette = 'Set2')
plt.title('Relation between Target and Blood disorder-Thalessemia', fontsize = 20)

# target vs chol and hue = thalach

plt.scatter(x = data['target'], y = data['chol'], s = data['thalach']*100)
plt.title('Relation of target with cholestrol and thalessemia', fontsize = 20)

# multi-variate analysis

sns.boxplot(x = data['target'], y = data['trestbps'], hue = data['sex'], palette = 'Set2')
plt.title('Checking relation of tresbps with genders to target', fontsize = 20)

# let's change the names of the  columns for better understanding

data.columns = ['age', 'sex', 'chest_pain_type', 'resting_blood_pressure', 'cholesterol', 'fasting_blood_sugar', 'rest_ecg', 'max_heart_rate_achieved',
       'exercise_induced_angina', 'st_depression', 'st_slope', 'num_major_vessels', 'thalassemia', 'target']

data.columns

data['sex'][data['sex'] == 0] = 'female'
data['sex'][data['sex'] == 1] = 'male'

data['chest_pain_type'][data['chest_pain_type'] == 1] = 'typical angina'
data['chest_pain_type'][data['chest_pain_type'] == 2] = 'atypical angina'
data['chest_pain_type'][data['chest_pain_type'] == 3] = 'non-anginal pain'
data['chest_pain_type'][data['chest_pain_type'] == 4] = 'asymptomatic'

data['fasting_blood_sugar'][data['fasting_blood_sugar'] == 0] = 'lower than 120mg/ml'
data['fasting_blood_sugar'][data['fasting_blood_sugar'] == 1] = 'greater than 120mg/ml'

data['rest_ecg'][data['rest_ecg'] == 0] = 'normal'
data['rest_ecg'][data['rest_ecg'] == 1] = 'ST-T wave abnormality'
data['rest_ecg'][data['rest_ecg'] == 2] = 'left ventricular hypertrophy'

data['exercise_induced_angina'][data['exercise_induced_angina'] == 0] = 'no'
data['exercise_induced_angina'][data['exercise_induced_angina'] == 1] = 'yes'

data['st_slope'][data['st_slope'] == 1] = 'upsloping'
data['st_slope'][data['st_slope'] == 2] = 'flat'
data['st_slope'][data['st_slope'] == 3] = 'downsloping'

data['thalassemia'][data['thalassemia'] == 1] = 'normal'
data['thalassemia'][data['thalassemia'] == 2] = 'fixed defect'
data['thalassemia'][data['thalassemia'] == 3] = 'reversable defect'

data['sex'] = data['sex'].astype('object')
data['chest_pain_type'] = data['chest_pain_type'].astype('object')
data['fasting_blood_sugar'] = data['fasting_blood_sugar'].astype('object')
data['rest_ecg'] = data['rest_ecg'].astype('object')
data['exercise_induced_angina'] = data['exercise_induced_angina'].astype('object')
data['st_slope'] = data['st_slope'].astype('object')
data['thalassemia'] = data['thalassemia'].astype('object')

# taking the labels out from the data

y = data['target']

data = data.drop('target', axis = 1)

print("Shape of y:", y.shape)

# one hot encoding of the data
# drop_first = True, means dropping the first categories from each of the attribues
# for ex gender having gender_male and gender-female would be male having values 1 and 0


data = pd.get_dummies(data, drop_first=True)

# checking the dataset after encoding

data.head()

# splitting the dependent and independent variables from the data

x = data

# checking the shapes of x and y
print("Shape of x:", x.shape)
print("Shape of y:", y.shape)

y.value_counts()

# splitting the sets into training and test sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

# getting the shapes
print("Shape of x_train :", x_train.shape)
print("Shape of x_test :", x_test.shape)
print("Shape of y_train :", y_train.shape)
print("Shape of y_test :", y_test.shape)

"""Diagnostic tests are often sold, marketed, cited and used with sensitivity and specificity as the headline metrics. Sensitivity and specificity are defined as,
Sensitivity = TruePositives/TruePositives+FalseNegatives
Specificity = FalseNegatives/FalseNegatives+TruePositives
"""

# MODELLING
# Random Forest Classifier

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

model = RandomForestClassifier(n_estimators = 50, max_depth = 5)
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
y_pred_quant = model.predict_proba(x_test)[:, 1]
y_pred = model.predict(x_test)

# evaluating the model
print("Training Accuracy :", model.score(x_train, y_train))
print("Testing Accuracy :", model.score(x_test, y_test))

# cofusion matrix
cm = confusion_matrix(y_test, y_pred)
plt.rcParams['figure.figsize'] = (5, 5)
sns.heatmap(cm, annot = True, annot_kws = {'size':15})

# classification report
cr = classification_report(y_test, y_pred)
print(cr)

y_pred_quant

from sklearn.tree import export_graphviz

estimator = model.estimators_[1]
feature_names = [i for i in x_train.columns]

y_train_str = y_train.astype('str')
y_train_str[y_train_str == '0'] = 'no disease'
y_train_str[y_train_str == '1'] = 'disease'
y_train_str = y_train_str.values


export_graphviz(estimator, out_file='tree.dot',
                feature_names = feature_names,
                class_names = y_train_str,
                rounded = True, proportion = True,
                label='root',
                precision = 2, filled = True)

from subprocess import call
call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=50'])

from IPython.display import Image
Image(filename = 'tree.png')

"""**Specificity and Sensitivity**"""

total=sum(sum(cm))

sensitivity = cm[0,0]/(cm[0,0]+cm[1,0])
print('Sensitivity : ', sensitivity )

specificity = cm[1,1]/(cm[1,1]+cm[0,1])
print('Specificity : ', specificity)

from sklearn.metrics import roc_curve

fpr, tpr, thresholds = roc_curve(y_test, y_pred_quant)

fig, ax = plt.subplots()
ax.plot(fpr, tpr)
ax.plot([0, 1], [0, 1], transform=ax.transAxes, ls="-", c=".3")
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

plt.title('ROC curve for diabetes classifier')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

# let's check the auc score

from sklearn.metrics import auc
auc = auc(fpr, tpr)
print("AUC Score :", auc)

"""**Explanation**"""




# importing ML Explanability Libraries


#for permutation importance
import eli5
from eli5.sklearn import PermutationImportance

#for SHAP values
import shap
from pdpbox import pdp, info_plots #for partial plots

# let's check the importance of each attributes

perm = PermutationImportance(model, random_state = 0).fit(x_test, y_test)
eli5.show_weights(perm, feature_names = x_test.columns.tolist())

"""**Partial Dependence Plot for Top 5 Features**"""

# plotting the partial dependence plot for num_major_vessels

base_features = data.columns.values.tolist()

feat_name = 'num_major_vessels'
pdp_dist = pdp.pdp_isolate(model=model, dataset=x_test, model_features = base_features, feature = feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# let's plot the partial dependence plot for thalassemia_fixed defect

base_features = data.columns.values.tolist()

feat_name = 'thalassemia_fixed defect'
pdp_dist = pdp.pdp_isolate(model = model, dataset = x_test, model_features = base_features, feature = feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# let's plot the partial dependence plot for thalassemia_reversable defect

base_features = data.columns.values.tolist()

feat_name = 'thalassemia_reversable defect'
pdp_dist = pdp.pdp_isolate(model = model, dataset = x_test, model_features = base_features, feature = feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# plotting a partial dependence graph for chest_pain_type_atypical angina

base_features = data.columns.values.tolist()

feat_name = 'chest_pain_type_atypical angina'
pdp_dist = pdp.pdp_isolate(model = model, dataset = x_test, model_features = base_features, feature = feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# plotting a partial dependence graph for st_depression


base_features = data.columns.values.tolist()

feat_name = 'st_depression'
pdp_dist = pdp.pdp_isolate(model = model, dataset = x_test, model_features = base_features, feature = feat_name)

pdp.pdp_plot(pdp_dist, feat_name)
plt.show()

# interactive partial dependence plots for st_depression

inter1 = pdp.pdp_interact(model=model, dataset=x_test, model_features=base_features, features=['st_slope_upsloping', 'st_depression'],
                          num_grid_points=[10, 10], percentile_ranges=[None, None],)

fig, axis = pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=['st_slope_upsloping', 'st_depression'], x_quantile = True, plot_pdp = True)
plt.show()

inter1  =  pdp.pdp_interact(model=model, dataset=x_test, model_features=base_features, features=['st_slope_flat', 'st_depression'])

pdp.pdp_interact_plot(pdp_interact_out=inter1, feature_names=['st_slope_flat', 'st_depression'], plot_type='contour', x_quantile = True,
                      plot_pdp = True)
plt.show()

# let's see the shap values

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(x_test)

shap.summary_plot(shap_values[1], x_test, plot_type="bar")

shap.summary_plot(shap_values[1], x_test)

# let's create a function to check the patient's conditions

def patient_analysis(model, patient):
  explainer = shap.TreeExplainer(model)
  shap_values = explainer.shap_values(patient)
  shap.initjs()
  return shap.force_plot(explainer.expected_value[1], shap_values[1], patient)

"""**Report for the First Patient**"""

# let's do some real time prediction for patients

patients = x_test.iloc[1,:].astype(float)
patient_analysis(model, patients)

"""**Report for the Second Patient**"""

patients = x_test.iloc[:, 2].astype(float)
patient_analysis(model, patients)

"""**Report for the Third Patient**"""

patients = x_test.iloc[:,3].astype(float)
patient_analysis(model, patients)

# dependence plot

shap.dependence_plot('num_major_vessels', shap_values[1], x_test, interaction_index = "st_depression")

"""**Force Plot**"""

shap_values = explainer.shap_values(x_train.iloc[:50])
shap.initjs()
shap.force_plot(explainer.expected_value[1], shap_values[1], x_test.iloc[:50])
