#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask


# In[2]:


app = Flask(__name__)


# In[3]:


from flask import request, render_template
import joblib


# In[4]:


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")
        model = joblib.load("predictdefault")
        
        pred = model.predict([[float(income), float(age), float(loan)]])
        s = f"The predicted default is {pred[0]}."
        
        return(render_template("index.html", result=s))
    else:
        return(render_template("index.html", result=""))


# In[5]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




