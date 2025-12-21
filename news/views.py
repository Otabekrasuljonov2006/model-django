from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def news(request):
    return render(request, "index.html")
def yangilik(request, id):
    if id>0 and id<=3:
        ls = [
            """
<div class="news" id="1"><h2>Birinchi yangilik</h2><p>Bu birinchi yangilik matni. Bugun muhim voqea sodir bo‘ldi.</p></div>
""",
            """
            <div class="news" id="2"><h2>Ikkinchi yangilik</h2><p>Bu ikkinchi yangilik. Texnologiya sohasida katta yangiliklar bor.</p></div>
            """,
            """
            <div class="news" id="3"><h2>Uchinchi yangilik</h2><p>Bu uchinchi yangilik. Sport olamidagi so‘nggi xabarlar.</p></div>
            """
        ]
        return HttpResponse(ls[id-1])
    else:
        return HttpResponse("Bunday yangilik hali mavjud emas")
    