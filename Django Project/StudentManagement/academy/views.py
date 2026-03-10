from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm

def index(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    enrollments = Enrollment.objects.all()
    context = {
        'student_count': students.count(),
        'course_count': courses.count(),
        'enrollment_count': enrollments.count(),
        'enrollments': enrollments.order_by('-enrollment_date')[:5]
    }
    return render(request, 'academy/index.html', context)

def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student registered successfully!')
            return redirect('register_student')
    else:
        form = StudentForm()
    return render(request, 'academy/register_student.html', {'form': form})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course added successfully!')
            return redirect('add_course')
    else:
        form = CourseForm()
    return render(request, 'academy/add_course.html', {'form': form})

def enroll_student(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()
            
            # Send Email
            student = enrollment.student
            course = enrollment.course
            context = {
                'student_name': f"{student.first_name} {student.last_name}",
                'course_name': course.name,
                'course_fee': course.fee,
            }
            html_message = render_to_string('academy/email_template.html', context)
            
            try:
                send_mail(
                    subject=f"Enrollment Acknowledgement - {course.name}",
                    message=f"Dear {student.first_name}, you have successfully enrolled in {course.name}.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[student.email],
                    html_message=html_message,
                    fail_silently=False,
                )
                messages.success(request, f'Student enrolled and acknowledgement email sent to {student.email}!')
            except Exception as e:
                messages.warning(request, f"Student enrolled but failed to send email: {str(e)}")
            
            return redirect('enroll_student')
    else:
        form = EnrollmentForm()
    return render(request, 'academy/enroll_student.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'academy/student_list.html', {'students': students})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student updated successfully!')
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'academy/register_student.html', {'form': form, 'is_update': True})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, 'Student deleted successfully!')
        return redirect('student_list')
    return render(request, 'academy/confirm_delete.html', {'object': student, 'type': 'Student', 'cancel_url': 'student_list'})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'academy/course_list.html', {'courses': courses})

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'academy/add_course.html', {'form': form, 'is_update': True})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, 'Course deleted successfully!')
        return redirect('course_list')
    return render(request, 'academy/confirm_delete.html', {'object': course, 'type': 'Course', 'cancel_url': 'course_list'})
