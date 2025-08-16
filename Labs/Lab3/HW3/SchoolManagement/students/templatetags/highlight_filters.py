from django import template
from difflib import SequenceMatcher
import re
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='highlight_similar')
def highlight_similar(text, args):
    """
    يقوم بتظليل الكلمات المشابهة للكلمة المحددة بدقة أعلى
    صيغة الاستخدام: {{ text|highlight_similar:"الكلمة,min_similarity=0.7,color=yellow" }}
    """
    try:
        word, params = args.split(',', 1)
        params = dict(p.split('=') for p in params.split(','))
    except:
        word = args
        params = {}
    
    min_similarity = float(params.get('min_similarity', 0.7))
    color = params.get('color', '#fffacd')
    
    # تحسين دقة المقارنة
    def is_similar(current_word):
        # تجاهل التشابه إذا كانت الكلمات مختلفة تماماً في الطول
        if abs(len(word) - len(current_word)) > 2:
            return False
            
        similarity = SequenceMatcher(None, word, current_word).ratio()
        return similarity >= min_similarity
    
    def replace_match(match):
        current_word = match.group()
        if is_similar(current_word):
            return f'<span style="background-color: {color}">{current_word}</span>'
        return current_word
    
    # تحسين نمط البحث عن الكلمات
    highlighted_text = re.sub(r'\b([\u0600-\u06FF]{2,})\b', replace_match, str(text))
    return mark_safe(highlighted_text)