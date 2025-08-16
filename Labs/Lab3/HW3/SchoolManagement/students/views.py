# from django.shortcuts import render, redirect
# from .data import context
# from django.http import HttpResponse

# def index(request):
#     return render(request, 'index.html')

# def home(request):
#     return render(request, 'home.html')

# def list_students(request):
#     return render(request, 'showstudents.html', {'students': context})

# def add_student(request):
#     if request.method == 'POST':
#         # هنا سنضيف منطق إضافة طالب جديد
#         new_student = {
#             "FirstName": request.POST.get('first_name'),
#             "LastName": request.POST.get('last_name'),
#             "Age": int(request.POST.get('age')),
#             "Gender": request.POST.get('gender'),
#             "Level": request.POST.get('level'),
#             "Status": request.POST.get('status')
#         }
#         context.append(new_student)
#         return redirect('show')
#     return render(request, 'addstudent.html')

# def edit_student(request, student_id):
#     student = context[int(student_id)]
#     if request.method == 'POST':
#         # هنا منطق التعديل
#         student['FirstName'] = request.POST.get('first_name')
#         student['LastName'] = request.POST.get('last_name')
#         student['Age'] = int(request.POST.get('age'))
#         student['Gender'] = request.POST.get('gender')
#         student['Level'] = request.POST.get('level')
#         student['Status'] = request.POST.get('status')
#         return redirect('show')
#     return render(request, 'editstudent.html', {'student': student, 'student_id': student_id})

# def delete_student(request, student_id):
#     if request.method == 'POST':
#         del context[int(student_id)]
#         return redirect('show')
#     return render(request, 'deletestudent.html', {'student': context[int(student_id)]})

from django.shortcuts import render, redirect
from .data import context
from datetime import datetime

def index(request):
    filter_context = {
        'fname': 'Doaa',  # قيمة لتجربة الفلاتر النصية
        'today': datetime.now(),  # لتجربة فلتر التاريخ
        'list': ['Apple', 'Banana', 'Cherry'],  # لتجربة فلتر join
        'float_num': 3.14159265359,  # لتجربة floatformat
        'long_text': 'هذا نص طويل جدًا يجب تقطيعه لعرض جزء منه فقط',  # لتجربة truncatechars
        'text': 'هذا النص يحتوي على عدة كلمات',  # لتجربة wordcount
        'dict_list': [{'name': 'أحمد'}, {'name': 'محمد'}, {'name': 'خالد'}],  # لتجربة dictsort
        'html_content': '<strong>نص HTML آمن</strong>',  # لتجربة فلتر safe
        'url_text': 'زيارة موقعنا https://example.com',  # لتجربة urlize
        'code_text': "Line 1\nLine 2\nLine 3"  # لتجربة linenumbers
    }
    return render(request, 'index.html', filter_context)

def home(request):
    return render(request, 'home.html')

def list_students(request):
    return render(request, 'showstudents.html', {'students': context})

# دوال الإضافة والتعديل والحذف
def add_student(request):
    if request.method == 'POST':
        new_student = {
            "FirstName": request.POST.get('first_name'),
            "LastName": request.POST.get('last_name'),
            "Age": int(request.POST.get('age')),
            "Gender": request.POST.get('gender'),
            "Level": request.POST.get('level'),
            "Status": request.POST.get('status')
        }
        context.append(new_student)
        return redirect('show')
    return render(request, 'addstudent.html')

def edit_student(request, student_id):
    student = context[int(student_id)]
    if request.method == 'POST':
        student['FirstName'] = request.POST.get('first_name')
        student['LastName'] = request.POST.get('last_name')
        student['Age'] = int(request.POST.get('age'))
        student['Gender'] = request.POST.get('gender')
        student['Level'] = request.POST.get('level')
        student['Status'] = request.POST.get('status')
        return redirect('show')
    return render(request, 'editstudent.html', {'student': student, 'student_id': student_id})

def delete_student(request, student_id):
    if request.method == 'POST':
        del context[int(student_id)]
        return redirect('show')
    return render(request, 'deletestudent.html', {'student': context[int(student_id)]})


from django.shortcuts import render
from difflib import SequenceMatcher
import re

def highlight_demo(request):
    word = request.GET.get('word', 'التعلم')
    min_similarity = float(request.GET.get('similarity', 0.7))
    color = request.GET.get('color', '#fffacd')
    
    highlight_args = f"{word},min_similarity={min_similarity},color={color}"
    
    text = request.GET.get('text', '')
    word_count = len(re.findall(r'\b[\u0600-\u06FF]+\b', text)) if text else 0
    
    # حساب الكلمات المظللة بنفس المنطق الدقيق المستخدم في الفلتر
    highlighted_count = 0
    if text and word:
        def is_similar(current_word):
            if abs(len(word) - len(current_word)) > 2:
                return False
            similarity = SequenceMatcher(None, word, current_word).ratio()
            return similarity >= min_similarity
        
        arabic_words = re.findall(r'\b[\u0600-\u06FF]+\b', text)
        highlighted_count = sum(1 for w in arabic_words if is_similar(w))
    
    return render(request, 'highlight_demo.html', {
        'highlight_args': highlight_args,
        'word_count': word_count,
        'highlighted_count': highlighted_count
    })