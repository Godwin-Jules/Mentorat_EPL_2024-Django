from django import forms
from .models import Challenge, Skill, Goal

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        exclude = ["slug", "date"]
        widgets = {
            "name": forms.TextInput(attrs = {
                "class": "challenge_control",
                "placeholder": "Make 21 days of coding"
            }),
            "month": forms.SelectMultiple(attrs = {"class": "challenge_control"}),
            "skills": forms.SelectMultiple(attrs = {"class": "challenge_control"}),
            "goals": forms.SelectMultiple(attrs = {"class": "challenge_control"}),
            "content": forms.Textarea(attrs = {
                "class": "challenge_control",
                "placeholder": "Give a description to your challenge right here !",
                "rows": 15,
                "cols": 75
            })
        }
        labels = {
            "name": "Your Challenge Name",
            "month": "Month(s)",
            "skills": "Skills to be improved",
            "goals": "Goals to be achieved",
            "content": "Your Challenge Description"
        }
        help_texts = {
            "name": "Give a name to your Challenge",
            "month": "Select at least one month",
            "skills": "Select at least one skill to be improved",
            "goals": "Select at least one goal to be achieved",
            "content": "Add a Description to your challenge"
        }
        error_messages = {
            "name": {
                "required": "Please give a name to your challenge",
                "invalid": "Please give a valid name",
                "max_length": "The name is too long",
                "unique": "This Challenge already exists"
            },
            "month": {
                "required": "Please select at least one month"
            },
            "skills": {
                "required": "Please select at least one skill"
            },
            "goals": {
                "required": "Please select at least one goal"
            },
            "content": {
                "required": "Please add a description to your challenge",
                "max_length": "The description is too long"
            }
        }



class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ["slug"]
        widgets = {
            "title": forms.TextInput(attrs = {
                "class": "skill_control",
                "placeholder": "Python"
            }),
            "description": forms.Textarea(attrs = {
                "class": "skill_control",
                "placeholder": "Python is a high-level, interpreted programming language"
            })
        }
        labels = {
            "title": "Your Skill Title",
            "description": "Your Skill Description"
        }
        help_texts = {
            "title": "Add a title to your skill",
            "description": "Add a description to your skill"
        }
        error_messages = {
            "title": {
                "required": "Please give a title to your skill",
                "invalid": "Please give a valid title",
                "max_length": "The title is too long",
                "unique": "This skill already exists"
            },
            "description": {
                "required": "Please add a description to your skill",
                "max_length": "The description is too long"
            }
        }



class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"
        widgets = {
            "label": forms.TextInput(attrs = {
                "class": "goal_control",
                "placeholder": "Learn Python"
            })
        }
        labels = {
            "label": "Your Goal"
        }
        help_texts = {
            "label": "Add a goal to be achieved"
        }
        error_messages = {
            "label": {
                "required": "Please give a goal to be achieved",
                "invalid": "Please give a valid goal",
                "max_length": "This goal is too long",
            }
        }