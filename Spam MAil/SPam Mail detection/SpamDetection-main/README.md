# SpamDetection
Two models for spam detection - RNN and Random Forest

## DATASET: 
SOURCE: https://www.kaggle.com/uciml/sms-spam-collection-dataset
- the dataset contains 4825 legit and 747 spam messages, a total of 5572, making it a relatively unbalanced dataset (86.6% legit and just 13.4% spam)

## DATA PREPROCESSING
- no tipical data preprocessing was done on the data, aside from tokenization and padding as the amount of _junk_ present is presumably a valuable indicator of the spam status of a message

## RANDOM FOREST CLASSIFIER
- even though the general accuracy score for this classifier reached an excellent 94%, the recall of only 56% is a cause for concern - which is demonstrated by the failure to recognize that the very obvious test message was indeed spam

## RECURRENT NEURAL NETWORK
- due to the size of our dataset, the architecture of the RNN was kept as simple as possible to avoid overfitting, with just one LSTM unit. This proved to be more than enough to reach an excellent 98% accuracy after evaluation on the test set, while still maintaining good convergence of loss and accuracy
- unlike RandomForrest, the RNN managed to properly identify the test message as spam
