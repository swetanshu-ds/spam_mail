import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Importing the dataset into a pandas dataframe
df = pd.read_table('SMSSpamCollection', sep = '\t', header = None, names = ['labels','sms_message']
               
# Converting the labels to binary variables for ease of computation
df['label'] = df.label.map({'ham':0, 'spam':1})

# Splitting the dataset into a training and testing set by using the train_test_split method in sklearn                   
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'], df['label'])
                   
# Instantiating the CountVectorizer method
count_vector = CountVectorizer()

# Fitting the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)

# Transforming testing data and return the matrix
testing_data = count_vector.transform(X_test)                   

# Importing the MultinomialNB classifier and fitting the training data into the classifier using fit()
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)                   

# Making some prediction on our test data using predict()
predictions = naive_bayes.predict(testing_data)
                   
# Computing the accuracy, precision, recall and F1 scores 
# of your model using your test data 'y_test' and the 'predictions' variable
print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))
print('Recall score: ', recall_score(y_test, predictions))
print('F1 score: ', f1_score(y_test, predictions))                  
