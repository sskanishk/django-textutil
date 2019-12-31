# star
# views it is a python program
# views return HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("hello wotld")

# orignial
def analyse(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    #Check which checkbox is on
    if(djtext == ""):
        return render(request, 'error.html')
    elif(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover != "on" and charcount != "on"):
        return render(request, 'error.html')
    else:
        if removepunc == "on":
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
            # return render(request, 'analyze.html', params)
            djtext = analyzed
        
        if(fullcaps == "on"):
            analyzed = ""
            for char in djtext:
                analyzed = analyzed + char.upper()
            params = {'purpose':'Changed to UPPERCASE', 'analyzed_text': analyzed}
            # return render(request, 'analyze.html', params)
            djtext = analyzed

        if (newlineremover == "on"):
            analyzed = ""
            for char in djtext:
                if char != "\n" and char!="\r":
                    analyzed = analyzed + char
                else:
                    print("no")
            print("pre", analyzed)
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
            print(params)
            # Analyze the text
            # return render(request, 'analyze.html', params)
            djtext = analyzed
        
        if(extraspaceremover == "on"):
            analyzed = ""
            for index, char in enumerate(djtext):
                if djtext[index] == " " and djtext[index+1] == " ":
                    pass
                else:
                    analyzed = analyzed + char
            params = {'purpose':'Removed ExtraSpace', 'analyzed_text': analyzed}
            # return render(request, 'analyze.html', params)
            djtext = analyzed
        
        if(charcount == "on"):
            count = 0
            for i in djtext:
                if i != " ":
                    count += 1
            # params = {'purpose':'Number of Character', 'analyzed_text': analyzed}
            params = {'purpose':'Number of Character', 'analyzed_text': count}
            # return render(request, 'analyze.html', params)
            # djtext = analyzed
        
        return render(request, 'analyze.html', params)


        



def dictx(request):
    params = {'name':'kanish', 'place':'Bali'}
    return render(request, 'dictx.html', params)

def about(request):
    a = '''<h2>about page</h2>
            <a href="http://127.0.0.1:8000/about">About</a><br>
            <a href="http://127.0.0.1:8000/notes">Notes</a>'''
    return HttpResponse(a)


# pipelines
# def removepunc(request):
#     # get the text 
#     print(request.GET.get('text', 'default'))
#     # analyse the text
#     return HttpResponse("removepunc")
# def capfirst(request):
#     return HttpResponse("capfirst")
# def newlineremove(request):
#     return HttpResponse("newlineremove")
# def spaceremove(request):
#     return HttpResponse("spaceremove")
# def charcount(request):
#     return HttpResponse("charcount")



def link(request):
    s = '''<h2>Navigation Bar<br></h2>
            <a href="https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django with Harry Bhai</a><br> 
            <a href="https://www.facebook.com/">Facebook</a><br>
            <a href="https://www.flipkart.com/">Flipkart</a><br>
            <a href="https://www.hindustantimes.com">News</a><br>
            <a href="https://www.google.com/">Google</a>'''
    return HttpResponse(s)


def notes(request):
    file = open("notes.txt",'r+')
    return HttpResponse(file.read())


