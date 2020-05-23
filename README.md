# Analogous-Document-Retrieval

### Similar Articles can be retrieved using ML Techniques, Such as word-count, TF - IDF, k'NN model. Brute force nearest neighbors model training, Pairwise querying.

[Project Reference](https://github.com/KrishnaManohar1997/Similar-Document-retrieval-using-Clustering)

## Installations

[Install Anaconda Navigator & GraphLab Create](https://turi.com/download/install-graphlab-create-command-line.html)

[Install django](https://docs.djangoproject.com/en/3.0/howto/windows/)

**django files structure**

![django files structure](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/django%20files%20path%20structure.png)

**Code Logic (views.py)**
```
import graphlab
graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
people = graphlab.SFrame('people_wiki.gl/')
people['word_count'] = graphlab.text_analytics.count_words(people['text'])
tfidf = graphlab.text_analytics.tf_idf(people['word_count'])

if graphlab.version <= '1.6.1':
   tfidf = tfidf['docs']

people['tfidf'] = tfidf
knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name')

pname = people[people['name'] == sname]
knn_model.query(pname)
```

### In Anaconda Navigator > Environments > (gl-env) Open Terminal
![Anaconda Terminal](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/Anaconda%20Navigator.png)

### Run django Server 
```
python manage.py runserver
```
![django server](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/django%20runserver.png)

### Sending Input
![Input](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/home.png)

## Output
![output1](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/result%201.png)
![output2](https://github.com/ravikkumar777/Analogous-Document-Retrieval/blob/master/screenshots/result2.png)
