from django.db.models.base import Model as Model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.views.generic import View, TemplateView, ListView
from .models import Month, Challenge, Skill, Goal
from .forms import ChallengeForm, SkillForm, GoalForm

# Create your views here.

months_list_en = [
    ("jan", "January"),
    ("feb", "February"),
    ("mar", "March"),
    ("apr", "April"),
    ("may", "May"),
    ("jun", "June"),
    ("jul", "July"),
    ("aug", "August"),
    ("sep", "September"),
    ("oct", "October"),
    ("nov", "November"),
    ("dec", "December"),
]
months_list_fr = [
    "janvier",
    "février",
    "mars",
    "avril",
    "mai",
    "juin",
    "juillet",
    "août",
    "septembre",
    "octobre",
    "novembre",
    "décembre"
]

def get_month(month) -> str:
    for i in months_list_en:
        if i[1] == month.capitalize():
            month_str = i[0]
            break
        month_str = ""

    return month_str



# Raising a 404 page
def raise_404(request, message="The page your are looking for does not exist.", string="", string1="", string2="", string3=""):
    return render(request, "404.html", context={"message": message}, status=404)



# Rendering localhost:8000
class StartingView(TemplateView):
    template_name = "challenges/starting.html"



# Rendering localhost:8000/months
class MonthsView(TemplateView):
    template_name = "challenges/months.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        months_en = [i[1].lower() for i in months_list_en]
        context["months"] = months_en
        return context



# Rendering localhost:8000/months/<str:month>/
class MonthChallengesView(View):
    def get(self, request, month):
        try:
            month_str = get_month(month)
            month_object = get_object_or_404(Month, month=month_str)
            month_challenges = month_object.challenges.all()    #type:ignore

            return render(request, "challenges/challenges.html", {
                "month": month,
                "challenges": month_challenges
            })
        except:
            return raise_404(request, "That month does not exist.")




# Rendering localhost:8000/months/<str:month>/<slug:slug>/
class SingleChallengeView(View):
    def get(self, request, month, slug):
        try:
            if month not in [i[1].lower() for i in months_list_en]:
                return raise_404(request, "That month does not exist.")

            challenge = get_object_or_404(Challenge, slug=slug)
            return render(request, "challenges/single_challenge.html", {
                "name": challenge.name,
                "month": month.capitalize(),
                "date": challenge.date,
                "skills": challenge.skills.all(),
                "goals": challenge.goals.all(),
                "content": challenge.content
                })
        except:
            return raise_404(request, "That challenge does not exist.")



# Rendering localhost:8000/months/add-goal/
class AddGoalView(View):
    def get(self, request):
        goal_form = GoalForm()
        return render(request, "challenges/add_goal.html", {"goal_form": goal_form})


    def post(self, request):
        goal_form = GoalForm(request.POST)
        if goal_form.is_valid():
            goal_form.save()
            return HttpResponseRedirect(reverse("all_goals"))

        return render(request, "challenges/add_goal.html", {"goal_form": goal_form})



# Rendering localhost:8000/months/add-skill/
class AddSkillView(View):
    def get(self, request):
        skill_form = SkillForm()
        return render(request, "challenges/add_skill.html", {"skill_form": skill_form})


    def post(self, request):
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill_form.save()
            return HttpResponseRedirect(reverse("all_skills"))

        return render(request, "challenges/add_skill.html", {"skill_form": skill_form})



# Rendering localhost:8000/months/add-challenge/
class AddChallengeView(View):
    def get(self, request):
        challenge_form = ChallengeForm()
        print(challenge_form)
        return render(request, "challenges/add_challenge.html", {"challenge_form": challenge_form})


    def post(self, request):
        challenge_form = ChallengeForm(request.POST)
        if challenge_form.is_valid():
            challenge_form.save()
            return HttpResponseRedirect(reverse("all_challenges"))

        return render(request, "challenges/add_challenge.html", {"challenge_form": challenge_form})



# Rendering localhost:8000/challenges
class ChallengesView(ListView):
    model = Challenge
    template_name = "challenges/all_challenges.html"
    context_object_name = "challenges"
    ordering = ["-id", "-date", "name"]



# Rendering localhost:8000/skills/
class SkillsView(ListView):
    model = Skill
    template_name = "challenges/all_skills.html"
    context_object_name = "skills"
    ordering = ["id", "title"]



# Rendering localhost:8000/goals/
class GoalsView(ListView):
    model = Goal
    template_name = "challenges/all_goals.html"
    context_object_name = "goals"
    ordering = ["id", "label"]



class ContactView(View):
    def get(self, request):
        return render(request, "challenges/contact.html")


    def post(self, request):
        pass
