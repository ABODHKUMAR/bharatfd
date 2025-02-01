from django.db import models
from ckeditor.fields import RichTextField
from django.core.cache import cache
from googletrans import Translator

# Initialize the Translator instance
translator = Translator()

class FAQ(models.Model):
    
    # Original Question and Answer in English
    question = models.TextField()
    answer = RichTextField()

    # Hindi
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    
    # Bengali
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    # Spanish
    question_es = models.TextField(blank=True, null=True)  
    answer_es = RichTextField(blank=True, null=True)
    
    # French
    question_fr = models.TextField(blank=True, null=True)  
    answer_fr = RichTextField(blank=True, null=True)
    
    # German
    question_de = models.TextField(blank=True, null=True) 
    answer_de = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically translate only if the fields are not already filled
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src="en", dest="hi").text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src="en", dest="hi").text

        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src="en", dest="bn").text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src="en", dest="bn").text

        if not self.question_es:
            self.question_es = translator.translate(self.question, src="en", dest="es").text
        if not self.answer_es:
            self.answer_es = translator.translate(self.answer, src="en", dest="es").text

        if not self.question_fr:
            self.question_fr = translator.translate(self.question, src="en", dest="fr").text
        if not self.answer_fr:
            self.answer_fr = translator.translate(self.answer, src="en", dest="fr").text

        if not self.question_de:
            self.question_de = translator.translate(self.question, src="en", dest="de").text
        if not self.answer_de:
            self.answer_de = translator.translate(self.answer, src="en", dest="de").text

        super().save(*args, **kwargs)

    def get_translation(self, lang):
        """
        This method retrieves the translated question for a specific language.
        If the translation is not cached, it will fetch the translation, store it in the cache, and return it.
        """
        # Cache the translations for one hour (3600 seconds)
        cache_key = f"faq_{self.id}_{lang}_question"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data  # Return cached translation if available
        
        # Get the translation from the model fields or fallback to the original question
        translation = getattr(self, f"question_{lang}", self.question)
        
        # Store the translation in cache
        cache.set(cache_key, translation, timeout=3600)  # Cache for 1 hour
        
        return translation

    def get_translation_answer(self, lang):
        """
        This method retrieves the translated answer for a specific language.
        If the translation is not cached, it will fetch the translation, store it in the cache, and return it.
        """
        cache_key = f"faq_{self.id}_{lang}_answer"
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data
        
        # Get the translation from the model fields or fallback to the original answer
        translation = getattr(self, f"answer_{lang}", self.answer)
        
        # Store the translation in cache
        cache.set(cache_key, translation, timeout=3600)
        
        return translation

    def __str__(self):
        return self.question
