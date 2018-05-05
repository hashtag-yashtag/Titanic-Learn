<div><div class="markdown-converter__text--rendered"><h3>Start here if...</h3>
<p>You're new to data science and machine learning, or looking for a simple intro to the Kaggle prediction competitions.</p>
<h3>Competition Description</h3>
<p>The sinking of the RMS Titanic is one of the most infamous shipwrecks in history.&nbsp; On April 15, 1912, during her maiden voyage, the Titanic sank after colliding with an iceberg, killing 1502 out of 2224 passengers and crew. This sensational tragedy shocked the international community and led to better safety regulations for ships.</p>
<p>One of the reasons that the shipwreck led to such loss of life was that there were not enough lifeboats for the passengers and crew. Although there was some element of luck involved in surviving the sinking, some groups of people were more likely to survive than others, such as women, children, and the upper-class.</p>
<p>In this challenge, we ask you to complete the analysis of what sorts of people were likely to survive. In particular, we ask you to apply the tools of machine learning to predict which passengers survived the tragedy.</p>
<h3>Practice Skills</h3>
<ul>
<li>Binary classification</li>
<li>Python and R basics</li>
</ul>

<div class="markdown-converter__text--rendered competition-data__content"><h3>Overview</h3>
<p>The data has been split into two groups:</p>
<ul>
<li>training set (train.csv)</li>
<li>test set (test.csv)</li>
</ul>
<p><b> The training set </b>should be used to build your machine learning models. For the training set, we provide the outcome (also known as the “ground truth”) for each passenger. Your model will be based on “features” like passengers’ gender and class. You can also use <a href="https://triangleinequality.wordpress.com/2013/09/08/basic-feature-engineering-with-the-titanic-data/" target="_blank" rel="nofollow"> feature engineering </a>to create new features.</p>
<p><b>The test set </b>should be used to see how well your model performs on unseen data. For the test set, we do not provide the ground truth for each passenger. It is your job to predict these outcomes. For each passenger in the test set, use the model you trained to predict whether or not they survived the sinking of the Titanic.</p>
<p>We also include <b>gender_submission.csv</b>, a set of predictions that assume all and only female passengers survive, as an example of what a submission file should look like.</p>
<h3>Data Dictionary</h3>
<table>
<tbody>
<tr><th><b>Variable</b></th><th><b>Definition</b></th><th><b>Key</b></th></tr>
<tr>
<td>survival</td>
<td>Survival</td>
<td>0 = No, 1 = Yes</td>
</tr>
<tr>
<td>pclass</td>
<td>Ticket class</td>
<td>1 = 1st, 2 = 2nd, 3 = 3rd</td>
</tr>
<tr>
<td>sex</td>
<td>Sex</td>
<td></td>
</tr>
<tr>
<td>Age</td>
<td>Age in years</td>
<td></td>
</tr>
<tr>
<td>sibsp</td>
<td># of siblings / spouses aboard the Titanic</td>
<td></td>
</tr>
<tr>
<td>parch</td>
<td># of parents / children aboard the Titanic</td>
<td></td>
</tr>
<tr>
<td>ticket</td>
<td>Ticket number</td>
<td></td>
</tr>
<tr>
<td>fare</td>
<td>Passenger fare</td>
<td></td>
</tr>
<tr>
<td>cabin</td>
<td>Cabin number</td>
<td></td>
</tr>
<tr>
<td>embarked</td>
<td>Port of Embarkation</td>
<td>C = Cherbourg, Q = Queenstown, S = Southampton</td>
</tr>
</tbody>
</table>
<h3>Variable Notes</h3>
<p><b>pclass</b>: A proxy for socio-economic status (SES)<br> 1st = Upper<br> 2nd = Middle<br> 3rd = Lower<br><br> <b>age</b>: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5<br><br> <b>sibsp</b>: The dataset defines family relations in this way...<br> Sibling = brother, sister, stepbrother, stepsister<br> Spouse = husband, wife (mistresses and fiancés were ignored)<br><br> <b>parch</b>: The dataset defines family relations in this way...<br> Parent = mother, father<br> Child = daughter, son, stepdaughter, stepson<br> Some children travelled only with a nanny, therefore parch=0 for them.</p></div>

<h3>Visualizing the Data:</h3>
<img src="https://www.kaggleusercontent.com/kf/3490804/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..iik7VOlmINAvK7IDEl7wJA.NslqLnInDkBH4pZe0AhQhox_Ze5VXLoIMnyYtxClkuVMWGmaMhKJ92X9ARL5hbPBK1EXA2-6v-WF4krhHggIg4rmJAwR_6Kw9hCu_XxE-Be5DhjxfVZw0UZDJsXyW8pUGEIXdXKLGdA66iPybiR73Q.6DFQW3yoRUrtoMdnbhBGJA/__results___files/__results___9_1.png">
