from features import getFeatures
from flask import Flask, request, render_template
import numpy as np
import warnings
import pickle
from sklearn.preprocessing import normalize

warnings.filterwarnings('ignore')

file = open("pickle_model/phishing_model.pkl", "rb")
gbc = pickle.load(file)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        obj = getFeatures(url)
        x = np.array(obj.featuresArray()).reshape(1, 30)
        newArr = []
        for i in x:
            for y in i:
                newArr.append(y)
        print(x)
        print(type(x))
        print(normalize(x))
        predictions = gbc.predict_proba(x)[0, 1]
        y=['UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
       'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
       'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
       'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
       'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick',
       'UsingPopupWindow', 'IframeRedirection', 'AgeofDomain', 'DNSRecording',
       'WebsiteTraffic', 'PageRank', 'GoogleIndex', 'LinksPointingToPage',
       'StatsReport']
        featuresFull = [];
        predictions=1
        for i in range(0, len(y)):
            featuresFull.append([y[i], newArr[i]])
        return render_template('index.html', score=predictions, url=url, newArr=newArr, y=y, featuresFull=featuresFull)
    return render_template('index.html', score=42)


if __name__ == "__main__":
    app.run(debug=True)
