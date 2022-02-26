#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import render_template, request
import joblib

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")   
        purchases = float(purchases)
        suppcard = float(suppcard)
        print(purchases, suppcard)
        model1 = joblib.load("ccu_dt")
        pred1 = model1.predict([[purchases, suppcard]])
        s1 = "The Score of CC Upgrade based on Decision Tree is " + str(pred1[0])
        model2 = joblib.load("ccu_reg")
        pred2 = model2.predict([[purchases, suppcard]])
        s2 = "The Score of CC Upgrade based on Regression is " + str(pred2[0])
        model3 = joblib.load("ccu_nn")
        pred3 = model3.predict([[purchases, suppcard]])
        s3 = "The Score of CC Upgrade based on Neural Network is " + str(pred3[0])
        model4 = joblib.load("ccu_gb")
        pred4 = model4.predict([[purchases, suppcard]])
        s4 = "The Score of CC Upgrade based on Gradient Boosting is " + str(pred4[0])
        model5 = joblib.load("ccu_rf")
        pred5 = model5.predict([[purchases, suppcard]])
        s5 = "The Score of CC Upgrade based on Random Forest is " + str(pred5[0])
        return(render_template("index.html", result1 = s1, result2 = s2, result3 = s3, result4 = s4, result5 = s5))
    else:
        return(render_template("index.html", result1 = "2", result2 = "2", result3 = "2", result4 = "2", result5 = "2"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




