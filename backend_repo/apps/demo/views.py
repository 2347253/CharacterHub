from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Post
from .serializers import PostSerializer
from random import sample  # Import sample for random selection

class PostPagination(PageNumberPagination):
    page_size = 10  # Number of posts per page
    page_size_query_param = 'page_size'

class PostListView(APIView):
    def get(self, request):
        # Fetch all posts and order them by timestamp (latest first)
        posts = Post.objects.all().order_by('-timestamp')

        # Apply pagination
        paginator = PostPagination()
        paginated_posts = paginator.paginate_queryset(posts, request)

        # Serialized posts with a limit of 3 comments
        serialized_posts = PostSerializer(
            paginated_posts, 
            many=True, 
            context={'show_comments': 3}  # Limit to 3 comments
        )

        # Follow-up Logic:
        # Instead of sorting comments by timestamp, you can fetch 3 random comments associated with each post.
        """
        for post in paginated_posts:
            comments = post.comments.all()  # Fetch all comments for the post
            # Randomly select up to 3 comments
            if comments.count() > 3:
                random_comments = sample(list(comments), 3)
            else:
                random_comments = comments
            # Add the random comments to the serialized post data
            serialized_post = PostSerializer(post).data
            serialized_post['comments'] = [
                {
                    "text": comment.text,
                    "timestamp": comment.timestamp,
                    "author": comment.user.username,
                }
                for comment in random_comments
            ]
            serialized_posts.data.append(serialized_post)
        """

        return paginator.get_paginated_response(serialized_posts.data)
