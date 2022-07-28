# NUS-summer-workshop: Opinion Spam Detection
**Nowadays, people are using product reviews to aid them in purchase decisions. Some  companies have intentionally fabricated fake reviews to either boost the rating/sentiment of their  products or to damage the rating/sentiment of their competitor’s products. Build a system/propose  an approach to detect opinion spam.**

#### step 1 Extract Feature Vector

To classify the reviews, we extract the feature vector for each piece of review. As shown below，the vector contain 4 dimensions: Computational linguistic and psychology、Similarity、Keywords frequency、Reviewer behavior.

<img src="E:\NUS暑研\Project\presentation\fig1.png" style="zoom:80%;" />

In order to further explore the impact of different features on the classification results, We tried combinations of different features and got the following results. The feature vector combining the 5 features obtained the highest classification accuracy.

<img src="E:\NUS暑研\Project\presentation\fig2.jpg" style="zoom:67%;" />

#### step 2 Decide a Suitable Classifier

After we extract the feature vector, we use AutoGluon(AutoML for Text, Image, and Tabular Data) to help us find a suitable classifier. There are 1600 reviews in the data set. we selected 1200 as the training set, and the remaining 400 as the test set. We tried 9 common classification models, and the performance of the models is shown in the figure below.

<img src="E:\NUS暑研\Project\presentation\fig3.png" style="zoom: 50%;" />

#### step 3 Apply our model to amazon

We collected reviews for 4 categories of products:(TV and video, Sports and outdoors, Medical supplies, Makeup) from Amazon.com. For each category, we scraped about 1000 reviews from 10 different products. After that, we apply our model to analyze reviews for each category and calculate the proportion of spam reviews to all reviews. The results are shown below.

<img src="E:\NUS暑研\Project\presentation\fig4.png" style="zoom:48%;" />





