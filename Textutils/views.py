# I have created this file - SBK.
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse('''<h1>Hello SBK Bhai</h1>
#      <h2> Check out below link of websites for your reference : </h2>
#      <a href="https://www.youtube.com/">YouTube SBK</a>
#      </br>
#      <a href="https://www.linkedin.com/home/?trk=nav_responsive_tab_home">LinkedIn SBK</a>
#      </br>
#      <a href="http://www.voot.com/?gclid=CNLCw_Xajs8CFQ8jaAod6GcCsg">Voot SBK</a>
#      </br>
#      <a href="https://www.hotstar.com/in">Hotstar SBK</a>
#      </br>
#      <a href="https://www.javatpoint.com/">    JavaTpiont sbk  </a>
#      ''')
#
# def about(request):
#     return HttpResponse("About SBK Life")

def index(request):
    # param = {'name':"SBK", 'place':"Mars"}
    return render(request, 'index.html')
    # return HttpResponse("Home </br> <a href='/'> Back </a>")

def analyze(request):
    # Get the text
    Rtext = request.POST.get('text','default')
    # Check checkbox value
    dtext = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    # print(dtext)
    # print(Rtext)
    # Check which checkbox is on
    if dtext == "on":
        # return HttpResponse("Remove punc </br> <a href='/'> Back </a>")
        # analyzed = Rtext
        punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in Rtext:
            if char not in punctuation:
                analyzed = analyzed + char
        param = {'purpose':'Remove punctuations', 'analysed_text': analyzed}
        # return render(request, 'analyze.html', param)
        Rtext = analyzed
    if(fullcaps == 'on'):
        analyzed = ""
        for char in Rtext:
            analyzed = analyzed + char.upper()
        param = {'purpose': 'Upper Case conversion', 'analysed_text': analyzed}
        # return render(request, 'analyze.html', param)
        Rtext = analyzed
    if(newlineremover == 'on'):
        analyzed = ""
        for char in Rtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        param = {'purpose': 'Remove new line', 'analysed_text': analyzed}
        # return render(request, 'analyze.html', param)
        Rtext = analyzed
    if(extraspaceremover == 'on'):
        analyzed = ""
        for char in Rtext:
            if char != "  ":
                analyzed = analyzed + char
        param = {'purpose': 'Remove Extra Spaces', 'analysed_text': analyzed}
        # return render(request, 'analyze.html', param)
        Rtext = analyzed
    if(charcount == 'on'):
        analyzed = ""
        count =0
        for char in Rtext:
            analyzed = analyzed + char
            count +=1
        param = {'purpose': 'Get total number of character entered', 'analysed_text': analyzed, 'tcount': count}

    if(dtext != "on" and fullcaps != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
         return HttpResponse("You have entered an invalid operation : %s"%(Rtext))

    return render(request, 'analyze.html', param)
    # else:
    #     return HttpResponse("Error")
# def removepunc(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("Remove punc </br> <a href='/'> Back </a>")
#
# def capfirst(request):
#     return HttpResponse("Capitalize first")