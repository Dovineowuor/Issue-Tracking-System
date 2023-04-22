from django.shortcuts import render
# Create your views here.
from django.shortcuts import render, redirect
from .models import Issue
from apps.Users.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Issue, Project, Role, UserRole

@login_required
def assign_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        assigned_to = User.objects.get(id=request.POST['assigned_to'])
        issue.assigned_to = assigned_to
        issue.save()
        return redirect('issue_detail', issue_id=issue.id)
    else:
        users = User.objects.all()
        return render(request, 'assign_issue.html', {'issue': issue, 'users': users})

@login_required
def resolve_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        issue.status = request.POST['status']
        issue.save()
        return redirect('issue_detail', issue_id=issue.id)
    else:
        return render(request, 'resolve_issue.html', {'issue': issue})

@login_required
def reassign_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    if request.method == 'POST':
        assigned_to = User.objects.get(id=request.POST['assigned_to'])
        issue.assigned_to = assigned_to
        issue.save()
        return redirect('issue_detail', issue_id=issue.id)
    else:
        users = User.objects.all()
        return render(request, 'reassign_issue.html', {'issue': issue, 'users': users})

@login_required
def manage_roles(request):
    roles = Role.objects.all()
    if request.method == 'POST':
        user_id = request.POST['user_id']
        role_id = request.POST['role_id']
        user_role = UserRole.objects.filter(user_id=user_id).first()
        if user_role:
            user_role.role_id = role_id
            user_role.save()
        else:
            UserRole.objects.create(user_id=user_id, role_id=role_id)
        return redirect('manage_roles')
    else:
        users = User.objects.all()
        return render(request, 'manage_roles.html', {'users': users, 'roles': roles})

@login_required
def assign_issue(request, issue_id):
    issue = Issue.objects.get(id=issue_id)
    users = User.objects.all()
    if request.method == 'POST':
        assigned_to_id = request.POST.get('assigned_to')
        assigned_to = User.objects.get(id=assigned_to_id)
        issue.assigned_to = assigned_to
        issue.save()
        return redirect('issue_detail', issue_id=issue.id)
    return render(request, 'assign_issue.html', {'issue': issue, 'users': users})
# /////////////
# from auth0.v3.authentication import GetToken
# from auth0.v3.management import Auth0

# def login(request):
#     # Redirect the user to the Auth0 login page
#     auth0 = Auth0(domain='your-auth0-domain', client_id='your-client-id', client_secret='your-client-secret')
#     authorize_url = auth0.authorize_url(redirect_uri='http://localhost:8000/callback', audience='your-audience')
#     return redirect(authorize_url)

# def callback(request):
#     # Handle the callback from Auth0 to authenticate the user
#     auth0 = Auth0(domain='your-auth0-domain', client_id='your-client-id', client_secret='your-client-secret')
#     code = request.GET.get('code')
#     token = GetToken(auth0).authorization_code(client_id='your-client-id', client_secret='your-client-secret', code=code, redirect_uri='http://localhost:8000/callback')
#     user_info = auth0.users.get(token['access_token'])
#     # Save the user info to the database or session
#     return redirect('home')