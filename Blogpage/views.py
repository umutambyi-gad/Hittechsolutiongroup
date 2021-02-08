from django.shortcuts import render, redirect
from django.views.generic import View
from .models import *
from Contactpage.models import *
from django.http import JsonResponse
from scripts.script import formatting_
from calendar import month_abbr
from Memberspage.views import ajax_operation


def blog(request):
    tags = Tags.objects.all()
    categories = Categories.objects.all()
    blogs = Blogs.objects.all()
    contacts = ContactForm.objects.all()

    address = ''
    number = ''
    email = ''
    for contact in contacts:
        address = contact.address
        number = contact.contact_number
        email = contact.email_address

    suffer = ''
    for i in blogs:
        suffer = month_abbr[i.blog_added_date.month]

    context = {
        'tags': tags,
        'categories': categories,
        'blogs': blogs,
        'suffer': suffer,
        'breadcrumb': BlogBreadcrumb.objects.first(),
        'address': address,
        'number': number,
        'email': email
    }
    return render(request, 'blog.html', context)
    if request.is_ajax():
        return ajax_operation(request)
    

def blog_single(request, blog_id, blog_title_slug):
    try:
        tags = Tags.objects.all()
        categories = Categories.objects.all()
        blog = Blogs.objects.get(pk=blog_id)
        blogs = Blogs.objects.all()

        contents = formatting_(blog.blog_content)

        contacts = ContactForm.objects.all()
        for contact in contacts:
            address = contact.address
            number = contact.contact_number
            email = contact.email_address

        context = {
           'tags': tags,
           'categories': categories,
           'blog': blog,
           'blogs': blogs,
           'contents': contents,
           'breadcrumb': BlogBreadcrumb.objects.first(),
           'address': address,
            'number': number,
            'email': email
        }
        if request.is_ajax():

            root_comment_id = request.POST.get('root_comment_id', None)
            message = request.POST.get('ajax_message', None)

            if root_comment_id is not None or message is not None:
                if len(root_comment_id.strip()) > 0:
                    root_comment_id = int(root_comment_id.strip())

                if message.startswith('@') and isinstance(root_comment_id, int):
                    reply_data = ReplyComments.objects.create(
                        user=request.user,
                        root_comment=RootComments.objects.get(pk=root_comment_id),
                        commentor_message=message)
                    reply_data.save()

                else:
                    root_data = RootComments.objects.create(
                        user=request.user,
                        blog=Blogs.objects.get(pk=blog_id),
                        commentor_message=message)
                    root_data.save()

            return ajax_operation(request)
            
        return render(request, 'blog-single.html', context)

    except Exception:
       return render(request, '404.html')
