class Titanic:
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np
    #import sklearn as learn

    train = pd.read_csv('train.csv')
    test = pd.read_csv('test.csv')

    PassengerID = train['PassengerId']

    f, ax = plt.subplots(3, 4, figsize=(15, 15))
    sns.countplot('Pclass', data=train, ax=ax[0, 0])
    sns.countplot('Sex', data=train, ax=ax[0, 1])
    sns.boxplot(x='Pclass', y='Age', data=train, ax=ax[0, 2])
    sns.countplot('SibSp', hue='Survived', data=train, ax=ax[0, 3], palette='husl')
    sns.distplot(train['Fare'].dropna(), ax=ax[2, 0], kde=False, color='b')
    sns.countplot('Embarked', data=train, ax=ax[2, 2])

    sns.countplot('Pclass', hue='Survived', data=train, ax=ax[1, 0], palette='husl')
    sns.countplot('Sex', hue='Survived', data=train, ax=ax[1, 1], palette='husl')
    sns.distplot(train[train['Survived'] == 0]['Age'].dropna(), ax=ax[1, 2], kde=False, color='r', bins=5)
    sns.distplot(train[train['Survived'] == 1]['Age'].dropna(), ax=ax[1, 2], kde=False, color='g', bins=5)
    sns.countplot('Parch', hue='Survived', data=train, ax=ax[1, 3], palette='husl')
    sns.swarmplot(x='Pclass', y='Fare', hue='Survived', data=train, palette='husl', ax=ax[2, 1])
    sns.countplot('Embarked', hue='Survived', data=train, ax=ax[2, 3], palette='husl')

    ax[0, 0].set_title('Total Passengers by Class')
    ax[0, 1].set_title('Total Passengers by Gender')
    ax[0, 2].set_title('Age Box Plot By Class')
    ax[0, 3].set_title('Survival Rate by SibSp')
    ax[1, 0].set_title('Survival Rate by Class')
    ax[1, 1].set_title('Survival Rate by Gender')
    ax[1, 2].set_title('Survival Rate by Age')
    ax[1, 3].set_title('Survival Rate by Parch')
    ax[2, 0].set_title('Fare Distribution')
    ax[2, 1].set_title('Survival Rate by Fare and Pclass')
    ax[2, 2].set_title('Total Passengers by Embarked')
    ax[2, 3].set_title('Survival Rate by Embarked')

    plt.show()


