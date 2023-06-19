<h1>Phishing detection</h1>
<img width="308" alt="image" src="https://github.com/scry-monsters/Phishing-Detection/assets/43356852/a486f801-7aea-472a-b7f1-c69d79ffe84e">
<img width="308" alt="image" src="https://github.com/scry-monsters/Phishing-Detection/assets/43356852/89cb5908-39a3-43b2-8ef8-7bd44965ccfd">
<h1>Developer Mode Page</h1>
<img width="310" alt="image" src="https://github.com/scry-monsters/Phishing-Detection/assets/43356852/2c24a659-3d91-48d4-92e2-59c84d67876b">
<img width="309" alt="image" src="https://github.com/scry-monsters/Phishing-Detection/assets/43356852/b685cf1b-2d12-4f30-b3bf-42200018dd76">
<h1>Overview</h1>
<p>Phishing is a cybercrime in which a target or targets are contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords. The information is then used to access important accounts and can result in identity theft and financial loss.</p>
<p>One of the most successful methods for preventing phishing attacks is Machine Learning. Most phishing attacks have same characteristics or features. With the help of supervised machine learning we can detect these patterns and prevent users falling victim to these types of attacks.</p>
</br>
To see the final project, click <a href="http://scrym.pythonanywhere.com/">here</a>
</br>
<h1>Tech Stack</h1>
<a href="https://www.python.org/" title="Python" rel="nofollow"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="100px" height="100px" style="max-width: 100%;"></a>
<a href="https://matplotlib.org/" rel="nofollow"><img src="https://camo.githubusercontent.com/e697b78d800b99e49d5220298ca5b72e74d31a7285bc0cc2615a9a104ab7e766/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f382f38342f4d6174706c6f746c69625f69636f6e2e737667" width="100" data-canonical-src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" style="max-width: 100%;"></a>
<a href="https://numpy.org/" title="NumPy" rel="nofollow"><img src="https://github.com/get-icon/geticon/raw/master/icons/numpy-icon.svg" alt="NumPy" width="100px" height="100px" style="max-width: 100%;"></a>
<a href="https://pandas.pydata.org/" title="pandas" rel="nofollow"><img src="https://github.com/get-icon/geticon/raw/master/icons/pandas-icon.svg" alt="pandas" width="100px" height="100px" style="max-width: 100%;"></a>
<a href="https://scikit-learn.org/" rel="nofollow"><img alt="https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/doc/logos/scikit-learn-logo.png" src="https://raw.githubusercontent.com/scikit-learn/scikit-learn/main/doc/logos/scikit-learn-logo.png" width="170px" style="max-width: 100%;"></a>
<a href="https://flask.palletsprojects.com/en/2.2.x/" title="flask" rel="nofollow"><img src="https://github.com/get-icon/geticon/raw/master/icons/flask.svg" alt="pandas" width="100px" height="100px" style="max-width: 100%;"></a>
</br>
</br>
<h1>Result</h1>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align:right">
      <th></th>
      <th>Model</th>
      <th>Accuracy</th>
      <th>F1 Score</th>
      <th>Recall</th>
      <th>Precision</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Gradient Boosting</td>
      <td>0.96895</td>
      <td>0.97261</td>
      <td>0.98228</td>
      <td>0.96314</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Random Forest</td>
      <td>0.96503</td>
      <td>0.96893</td>
      <td>0.97154</td>
      <td>0.96635</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SVC</td>
      <td>0.96262</td>
      <td>0.96699</td>
      <td>0.97530</td>
      <td>0.95882</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Decision Tree</td>
      <td>0.96171</td>
      <td>0.96600</td>
      <td>0.96885</td>
      <td>0.96316</td>
    </tr>
    <tr>
      <th>4</th>
      <td>KNN</td>
      <td>0.95418</td>
      <td>0.95929</td>
      <td>0.96187</td>
      <td>0.95673</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Logistic Regression</td>
      <td>0.92734</td>
      <td>0.93616</td>
      <td>0.94898</td>
      <td>0.92368</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Naive Bayes</td>
      <td>0.60567</td>
      <td>0.45950</td>
      <td>0.29860</td>
      <td>0.99642</td>
    </tr>
  </tbody>
</table>
<p>We can conclude that Gradient Boosting is the most effective algorithm for detecting phishing URLs in our dataset. </p>
</br>
<h1>Summary</h1>
<p>In conclusion, our supervised binary classification project involved exploring and analyzing a dataset of URLs to determine whether they were legitimate or phishing. We performed extensive exploratory data analysis to gain insights into the distribution and relationships of the features in the dataset. We also tested various classification algorithms, including Decision Trees, Random Forest, K-Nearest Neighbors, Naive Bayes, Logistic Regression, and Support Vector Machines, to find the most effective one.

After evaluating and comparing the performance of each algorithm using various metrics such as accuracy, precision, recall, and F1 score, we found that Gradient Boosting performed the best with an accuracy of over 95%. This algorithm provided the most accurate predictions and had the highest overall performance among the other algorithms.

Our project demonstrates the importance of performing exploratory data analysis and testing multiple classification algorithms to determine the best approach for solving a binary classification problem. The insights and knowledge gained from this project can be applied to similar classification problems in various domains, such as fraud detection, spam filtering, and malware detection.</p>
