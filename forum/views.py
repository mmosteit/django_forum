from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from models import Threads, Posts
from django.core.urlresolvers import reverse


import datetime

import forum_fn

# Create your views here.

def delete_post(request):
    dead_post_id   = request.GET['post_id']
    thread_id      = request.GET['thread_id']
    post           = Posts.objects.get(post_id=dead_post_id)
    post.deleted   = True
    post.save()
    
    response = redirect('view_thread')
    response['Location'] += '?thread_id='+str(thread_id)
    return response

def delete_thread(request):
    title = 'delete'
    dead_thread = request.POST['thread_id']
    Posts.objects.filter(thread_id = dead_thread).delete()
    Threads.objects.filter(thread_id = dead_thread).delete()

    return HttpResponseRedirect(reverse('forum.views.index'))

def index(request):
    title = 'Mosteit forum'
    template = loader.get_template('forum/index.html')

    threads = Threads.objects.all() 
    context = RequestContext(request, {'title':title, 
                                       'threads':threads} )         

    return HttpResponse(template.render(context))

def new_post(request):


    new_username    = request.POST['username']
    new_post_text   = request.POST['post_text'] 
    new_date_posted = datetime.datetime.now()
    new_parent_id   = request.POST['parent_id']
    new_thread_id   = request.POST['thread_id']
   
   
    if new_username.strip() == "" or new_post_text.strip() == "":
        template = loader.get_template('forum/new_post_error.html')
        title    = "Error creating thread"
        context  = RequestContext(request,{"title":title,"thread_id":new_thread_id})
        return HttpResponse(template.render(context))  
   
    post = Posts(username = new_username, post_text = new_post_text, date_posted = new_date_posted, parent_id = new_parent_id, deleted = False, thread_id = new_thread_id)
    post.save()
    
    response = redirect('view_thread')
    response['Location'] += '?thread_id='+str(new_thread_id)
    return response

   

   
    
#def new_post_error(request)
    
def new_thread(request):
    page_title       = 'new_thread'
    new_post_text    = request.POST['post_text']
    new_username     = request.POST['username']
    new_thread_title = request.POST['title']
    new_date_posted  = datetime.datetime.now()

    if new_post_text.strip() == "" or new_username.strip() == "" or new_thread_title.strip() == "":
        return HttpResponseRedirect(reverse('new_thread_error'))
    
    # Create the thread 
    new_thread = Threads(thread_title = new_thread_title, username = new_username, date_posted = new_date_posted) 
    new_thread.save()    

    # Create the dummy post. This post is the parent of all the top level
    # posts in this thread.  Being a dummy post, it contains no text
    dummy_post = Posts(parent_id = 0, date_posted = new_date_posted, thread_id = new_thread.thread_id, deleted = False, username = new_username)
    dummy_post.save()
    
    # Set the new thread's first post to the dummy post
    new_thread.first_post_id = dummy_post.post_id
    new_thread.save()
    
    # Insert the actual first post into the table
    first_post = Posts(parent_id = dummy_post.thread_id, username = new_username, post_text = new_post_text, date_posted = new_date_posted, thread_id = new_thread.thread_id, deleted = False )
    first_post.save()
  
    return HttpResponseRedirect(reverse('index'))

def new_thread_error(request):

    template = loader.get_template('forum/new_thread_error.html')
    title    = "Error creating thread"
    context  = RequestContext(request,{"title":title})
    return HttpResponse(template.render(context))

def view_thread(request):
    query_thread_id = request.GET['thread_id']
    thread          = Threads.objects.get(thread_id = query_thread_id)
    tree            = forum_fn.post_tree(thread.first_post_id, None)
    title           = thread.thread_title
    template        = loader.get_template('forum/view_thread.html')
    context         = RequestContext(request, {'title':title,'thread_id':query_thread_id, 
                                       'post':tree} ) 

    return HttpResponse(template.render(context))
