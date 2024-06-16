from django.shortcuts import render
from elasticsearch_dsl.query import MultiMatch
from .documents import BlogDocument

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Blog

from .kafka_producer import produce_message
from rest_framework import status


# def index(request):
#     q = request.GET.get("q")
#     context = {}
#     if q:
#         query = MultiMatch(query=q, fields=["blog_title", "blog_text"], fuzziness="AUTO")
#         s = BlogDocument.search().query(query)[0:5]
#         context["blog"] = s
#     return render(request, "index.html", context)

# @api_view()
# def index_home(request):
#     return Response({
#         'status': 200,
#         'message': 'Yes'
#     })

# @api_view(['GET'])
# def search_blogs(request):
#     q = request.GET.get("q", "")
#     if q:
#         query = MultiMatch(query=q, fields=["blog_title", "blog_text"], fuzziness="AUTO")
#         s = BlogDocument.search().query(query)[0:5]
#         results = s.to_queryset()  # Convert search results to queryset (or handle as needed)
#         blogs = [{
#             'blog_title': blog.blog_title,
#             'user_id': blog.user_id,
#             'blog_text': blog.blog_text
#         } for blog in results]
#         return Response(blogs)
#     return Response({'message': 'No query provided'}, status=400)


# View for rendering the search page and handling search queries
def index(request):
    q = request.GET.get("q")
    context = {}
    if q:
        query = MultiMatch(query=q, fields=["blog_title", "blog_text"], fuzziness="AUTO")
        s = BlogDocument.search().query(query)[0:5]
        results = s.execute()  # Execute the search
        context["blogs"] = results
    return render(request, "index.html", context)

# API view for searching blogs via GET request (if needed separately)
@api_view(['GET'])
def search_blogs(request):
    q = request.GET.get("q", "")
    if q:
        query = MultiMatch(query=q, fields=["blog_title", "blog_text"], fuzziness="AUTO")
        s = BlogDocument.search().query(query)[0:5]
        results = s.execute()  # Execute the search
        blogs = [{
            'blog_title': blog.blog_title,
            'user_id': blog.user_id,
            'blog_text': blog.blog_text
        } for blog in results]
        return Response(blogs)
    return Response({'message': 'No query provided'}, status=400)


# @api_view(['POST'])
# def create_blog(request):
#     data = request.data
#     user_id = data.get('user_id')
#     blog_title = data.get('blog_title')
#     blog_text = data.get('blog_text')

#     # Debugging prints
#     print(f"Received data: user_id={user_id}, blog_title={blog_title}, blog_text={blog_text}")

#     if not user_id or not blog_title or not blog_text:
#         print("Missing required fields")
#         return Response({'message': 'Missing required fields'}, status=400)

#     try:
#         # Directly create the blog without checking for User existence
#         blog = Blog.objects.create(user_id=user_id, blog_title=blog_title, blog_text=blog_text)
#         print(f"Blog created: {blog}")
#         return Response({
#             'blog_title': blog.blog_title,
#             'user_id': blog.user_id,
#             'blog_text': blog.blog_text
#         }, status=201)
#     except Exception as e:
#         print(f"Exception occurred: {e}")
#         return Response({'message': str(e)}, status=500)



@api_view(['POST'])
def create_blog(request):
    data = request.data
    user_id = data.get('user_id')
    blog_title = data.get('blog_title')
    blog_text = data.get('blog_text')

    # Ensure required fields are present
    if not user_id or not blog_title or not blog_text:
        return Response({'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Produce message to Kafka
        message = {
            'user_id': user_id,
            'blog_title': blog_title,
            'blog_text': blog_text
        }
        produce_message('blog', message)

        return Response({'message': 'Blog post submitted successfully'}, status=status.HTTP_202_ACCEPTED)

    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
