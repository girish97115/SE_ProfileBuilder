from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import (
    ListView
)

from users.forms import AppointmentCreationForm, AppointmentRejectionForm
from users.models import User
from .models import FacultyProfile, Appointment, StudentProfile


class FacultyProfileListView(ListView):
    model = FacultyProfile
    template_name = 'profiles/home.html'
    context_object_name = 'profiles'
    paginate_by = 4


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'profiles/appointmentlistview.html'
    context_object_name = 'appointments'
    paginate_by = 4

    def get_queryset(self):
        student_profile = StudentProfile.objects.filter(user=self.request.user.id).first()
        appointments = Appointment.objects.filter(student=student_profile.id).all()
        object_list = []
        for appointment in appointments:
            object_list.append(appointment)

        return object_list


class FacultySearchList(ListView):
    model = FacultyProfile
    template_name = 'profiles/search_listview.html'
    context_object_name = 'profiles'
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            users_list = User.objects.filter(username__icontains=query)
            object_list = FacultyProfile.objects.none()
            for users in users_list:
                object_list = object_list.union(FacultyProfile.objects.filter(user=users))

        else:
            object_list = FacultyProfile.objects.all()

        for post in object_list:
            if post.bookmark.filter(id=self.request.user.id).exists():
                post.is_favourite = True
            else:
                post.is_favourite = False
        return object_list


def bookmark_profile(request, pk):
    profile = get_object_or_404(FacultyProfile, id=pk)
    if profile.bookmark.filter(id=request.user.id).exists():
        profile.bookmark.remove(request.user)
    else:
        profile.bookmark.add(request.user)
    return HttpResponseRedirect(reverse('home'))


def make_appointment(request, pk):
    faculty = get_object_or_404(FacultyProfile, id=pk)
    student = request.user.studentprofile
    if request.method == "POST":
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.faculty = faculty
            appointment.student = student
            appointment.save()
            messages.success(request, f'Appointment request Sent')
            return HttpResponseRedirect(reverse('home'))

    else:
        form = AppointmentCreationForm()

    return render(request, 'profiles/appointment.html', {'faculty': faculty, 'student': student, 'form': form})


def faculty_info(request, pk):
    profile = get_object_or_404(FacultyProfile, id=pk)
    profiles = FacultyProfile.objects.all()
    object_list = []
    for pro in profiles:
        object_list.append(pro)
    return render(request, 'profiles/facultyinfo.html', {'profile': profile, 'profilesrelated': object_list[1:4]})


class RequestsListView(ListView, LoginRequiredMixin):
    model = Appointment
    template_name = 'users/requests.html'
    context_object_name = 'requests'
    paginate_by = 3

    def get_queryset(self):
        faculty_profile = FacultyProfile.objects.filter(user=self.request.user.id).first()
        appointments = Appointment.objects.filter(faculty=faculty_profile.id).all()
        object_list = []
        for appointment in appointments:
            object_list.append(appointment)

        return object_list


class StatusRequestsListView(ListView):
    model = Appointment
    template_name = 'profiles/appointment_status.html'
    context_object_name = 'appointments'
    paginate_by = 3

    # def get_queryset(self):
    #     student_profile = StudentProfile.objects.filter(user=self.request.user.id).first()
    #     appointments = Appointment.objects.filter(student=student_profile.id).all()
    #     object_list = []
    #     for appointment in appointments:
    #         object_list.append(appointment)
    #
    #     return object_list


def accept_appointment(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    appointment.accepted = 1
    appointment.save()
    messages.success(request, f'Appointment Accepted')
    return HttpResponseRedirect(reverse('home'))


def reject_appointment(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)

    if request.method == "POST":
        form = AppointmentRejectionForm(request.POST)
        if form.is_valid():
            reason = form.cleaned_data['Reason']
            appointment.accepted = 0
            appointment.reason_reject = reason
            appointment.save()
            messages.success(request, f'Appointment Rejected')
            return HttpResponseRedirect(reverse('home'))

    else:
        form = AppointmentRejectionForm()

    return render(request, 'users/reject_appointment.html', {'form': form})


class BookmarksListView(ListView, LoginRequiredMixin):
    model = FacultyProfile
    template_name = 'users/bookmarks.html'
    context_object_name = 'profiles'
    paginate_by = 3

    def get_queryset(self):
        profiles = FacultyProfile.objects.all()
        object_list = []
        for profile in profiles:
            if profile.bookmark.filter(id=self.request.user.id).exists():
                object_list.append(profile)

        return object_list
