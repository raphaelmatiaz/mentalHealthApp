import logging
from django.http import JsonResponse
from mongo.models import Comments
from mongo.mongo import Mongo
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .forms import CommentForm  

mongo = Mongo()
logging.basicConfig(level=10)


def get_comments(request: Request, category_id: int):
    comments = mongo.get_comments(category_id=category_id)

    if not comments:
        return JsonResponse(
            data={"error": "Comments not found"}, status=HTTP_404_NOT_FOUND
        )

    serializer = Comments(root=comments)

    return JsonResponse(data={"comments": serializer.model_dump()}, status=HTTP_200_OK)

#Tentativa de fazer método POST

def post_comments(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            content = form.cleaned_data['content']
            author = form.cleaned_data['author']
            category = form.cleaned_data['category']

            mongo.collection.insert_one(comment_data)

            return JsonResponse({"message": "Comentário enviado com sucesso!"}, status=HTTP_200_OK)

        else:
            return JsonResponse({"error": "Dados inválidos."}, status=HTTP_400_BAD_REQUEST)

    else:
        form = CommentForm()  

    return render(request, 'comment_form.html', {'form': form})

def delete_comments(request, comment_id):
    result = mongo.collection.delete_one({"_id": comment_id})

    if result.deleted_count > 0:
        return JsonResponse({"message": "Comentário apagado com sucesso!"}, status=HTTP_200_OK)
    else:
        return JsonResponse({"error": "Comentário não encontrado!"}, status=HTTP_404_NOT_FOUND)

def comment_list(request):
    comments = Comment.objects.all()  
    return render(request, 'comments/comment_list.html', {'comments': comments})