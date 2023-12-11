from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponse 
from translate import Translator 
from deep_translator import GoogleTranslator
from lingua import Language, LanguageDetectorBuilder

# Create your views here. 

def home(request): 
    if request.method == "POST": 
        text = request.POST["translate"] 
        language = request.POST["language"] 
		# translator= Translator(to_lang=language) 
		# translation = translator.translate(text)
        translation = GoogleTranslator(source='auto', target='ak').translate(text)
        languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
        detector = LanguageDetectorBuilder.from_languages(*languages)\
        .with_minimum_relative_distance(0.9)\
        .build()
        print(detector.detect_language_of("languages are awesome"))

        return HttpResponse(translation) 
    return render(request,"main/index.html")
