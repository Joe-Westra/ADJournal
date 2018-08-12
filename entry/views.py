from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import NightlyStatSerializer
from .models import NightlyStat
import re

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        with open("/home/ubuntu/stats/templates/entry/index.html") as f:
            CodeExampleRenderer.codeDuplicator(f)
            return render(request, 'entry/index2.html', context=None)

class StatsPageView(TemplateView):
    template_name = "stats.html"

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest API"""
    queryset = NightlyStat.objects.all()
    serializer_class = NightlyStatSerializer

    def preform_create(self, serializer):
        """Save the POST data when creating a new NightlyStat"""
        serializer.save()


class CodeExampleRenderer:
    starttag = '<code_example>'
    endtag = '</code_example>'
    codeexample = ""
    selection = False


    def selectLineCopier(line):
        if CodeExampleRenderer.starttag in line:
            CodeExampleRenderer.selection = True
            return line
        elif CodeExampleRenderer.selection == False:
            return line


        if CodeExampleRenderer.endtag in line:
            CodeExampleRenderer.selection = False
            formattedcode = '<p class="in-comp" id="formatted_code">' + CodeExampleRenderer.codeexample + "</p>"
            return str(line + formattedcode)

        code = str(line)
        code = re.sub('<','&lt;', code)
        code = re.sub('>','&gt;', code)
        CodeExampleRenderer.codeexample += code + "</br>"
        return line


    def codeDuplicator(rawhtml):

        file = rawhtml.readlines()
        outputfile = open("/home/ubuntu/stats/templates/entry/index2.html", "w")

        for line in file:
            outputfile.write(str(CodeExampleRenderer.selectLineCopier(line)))

        outputfile.close()
        CodeExampleRenderer.codeexample = ""
        """
        starttag = '<code_example>'
        endtag = '</code_example>'
        codeexcerpt = ""
        linecounter = 0
        codecounter = 0
        endline = 0

        for line in rawhtml.xreadlines():
            counter++
            if starttag in line:
                selection = True
                continue
            if endtag in line:
                selection = False

            if selection:
                code = line
                code = re.sub('<','&lt;', code)
                code = re.sub('>','&gt;', code)
                codeexcerpt += code

                originalcode = line
                start = line.find(starttag) + len(starttag)
                end = line.find(endtag, start)
                codexcerpt = line[start:end]
                codexcerpt = re.sub('<','&lt;',codexample)
                codexcerpt = re.sub('>','&gt;',code)
                formatttedcode = line[:start] + 


                code = line[start:end]



                code = re.sub('<','&lt;',codexample)
            code = re.sub('>','&gt;',code)
            output += rawhtml[:end]
            output +="<rightcode>" + code + "</rightcode>"
            start = rawhtml.find(starttag)
        return output + "hey there!"
        """
