from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    
    fulltext = request.GET['fulltext']
    words = fulltext.split()

    wordDicitionary = {}

    for word in words:
        
        if word in wordDicitionary:
            wordDicitionary[word] += 1
        else:
            wordDicitionary[word] = 1

    sortedWordDicitionary = sorted(wordDicitionary.items(), key = operator.itemgetter(1), reverse  = True)  
    

    return render(request,'count.html',{"fulltext":fulltext,"count":len(words),"wordDicitionary": sortedWordDicitionary})

def about(request):
    return render(request,'about.html')
      