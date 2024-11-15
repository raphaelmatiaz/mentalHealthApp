import logging
from django.http import JsonResponse
from mongo.models import CategoryComments
from mongo.mongo import Mongo
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from dashboard.forms import CommentForm  

mongo = Mongo()
logging.basicConfig(level=10)


def get_comments(request: Request, category_id: int):
    comments = mongo.db_get_comment(category_id=category_id)

    if not comments:
        return JsonResponse(
            data={"error": "Comments not found"}, status=HTTP_404_NOT_FOUND
        )

    serializer = CategoryComments(root=comments)

    return JsonResponse(data={"comments": serializer.model_dump()}, status=HTTP_200_OK)

def view_post_comment(request: Request, category_id):      
    
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():

            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            
            successfull = mongo.db_add_comment(
                author=author,
                category_id=category_id,
                content=content
            )
            
            if successfull:
                return JsonResponse(
                    data={"message": "Comment added successfully"},
                    status=HTTP_200_OK
                )
            else:
                return JsonResponse(
                    data={"error": "Failed to add comment"},
                    status=HTTP_500_INTERNAL_SERVER_ERROR
                )
            
            form = CommentForm()

            return render(request, 'dashboard/phrase_list.html', {'form': form})    
    else:
        form = CommentForm()
    
    return render(request, 'dashboard/create_phrase.html', {'form': form})    
