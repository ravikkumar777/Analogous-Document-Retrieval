from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from django import forms

def home(request):
	return render(request,"home.html", {})

def documentTraining(request):
    if request.method == "POST":
        sname = request.POST['myvalue']
        
    import graphlab
    graphlab.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', 4)
    people = graphlab.SFrame('people_wiki.gl/')
    people['word_count'] = graphlab.text_analytics.count_words(people['text'])
    tfidf = graphlab.text_analytics.tf_idf(people['word_count'])

    if graphlab.version <= '1.6.1':
        tfidf = tfidf['docs']

    people['tfidf'] = tfidf
    knn_model = graphlab.nearest_neighbors.create(people,features=['tfidf'],label='name')
    
    # Table Creation
    pname = people[people['name'] == sname]
    d=knn_model.query(pname)
    e= d[0]
    f= d[1]
    g= d[2]
    h= d[3]
    i= d[4]
    rank=e['rank']
    name=e['reference_label']
    distance=e['distance']
    te = people[people['name'] == name ]
    tx = te['text']
        
    rank1=f['rank']
    name1=f['reference_label']
    distance1=f['distance']
    te1 = people[people['name'] == name1 ]
    tx1 = te1['text']
        
    rank2=g['rank']
    name2=g['reference_label']
    distance2=g['distance']
    te2 = people[people['name'] == name2 ]
    tx2 = te2['text']
        
    rank3=h['rank']
    name3=h['reference_label']
    distance3=h['distance']
    te3 = people[people['name'] == name3 ]
    tx3 = te3['text']
        
    rank4=i['rank']
    name4=i['reference_label']
    distance4=i['distance']
    te4 = people[people['name'] == name4 ]
    tx4 = te4['text']
        
        
    return render(request, 'index.html', {'d':distance, 'd1':distance1, 'd2':distance2, 'd3':distance3, 'd4':distance4 ,
                                            'r':rank,     'r1':rank1,     'r2':rank2,     'r3':rank3,     'r4':rank4 ,
                                            'n':name,     'n1':name1,     'n2':name2,     'n3':name3,     'n4':name4,  
                                             'tt':tx,    'tt1':tx1,      'tt2':tx2,      'tt3':tx3,      'tt4':tx4
                                           })

