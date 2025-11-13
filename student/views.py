from django.shortcuts import render,redirect,get_object_or_404
from student.models import Profile
from student.forms import Registration
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

# READ
def Student_list(request):
    students=Profile.objects.all()
    return render(request,'student/student_list.html',{'students':students})
# CREATE

def add_student(request):
    if request.method=='POST':
             form=Registration(request.POST)
             if form.is_valid():
                form.save()
                return redirect('student_list')
    else:
        form=Registration()
    return render(request,'student/add_student.html',{'form':form})

# UPDATE

def edit_student(request,id):
    student=get_object_or_404(Profile,id=id)
    if request.method=='POST':
        
        form=Registration(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form=Registration(instance=student)
    return render(request,'student/edit_student.html',{'form':form})

# DELETE

def delete_student(request,id):
    student=get_object_or_404(Profile,id=id)
    if request.method=='POST':
       student.delete()
       return redirect('student_list')
    return render(request,'student/delete_student.html',{'student':student})