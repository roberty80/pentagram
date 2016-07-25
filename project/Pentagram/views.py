from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from Pentagram.models import Photo
from Pentagram.models import Comment
from Pentagram.serializers import PhotoSerializer, UserSerializer, CommentSerializer
from rest_framework.permissions import AllowAny


@api_view(['GET', 'POST'])
def photos(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many = True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    if request.method == "POST":
        photos = PhotoSerializer(data=request.data)
        if photos.is_valid():
            photos.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=photos.errors)


@api_view(['POST'])
@permission_classes((AllowAny,))
def users(request):
    if request.method == "POST":
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data = user_serializer.errors)


@api_view(['GET', 'POST'])
def comments(request, id_photo):
    if request.method== 'GET':
        comments= Comment.objects.filter(photo_id=id_photo)
        serializer= CommentSerializer(comments, many=True)
        return Response(status=status.HTTP_200_OK, data= serializer.data)
    if request.method == 'POST':
        comment_serializer= CommentSerializer(data=request.data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response (status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=comment_serializer.errors)

@api_view(['PUT'])
def like(request,id_photo):
    if request.method == 'PUT':
        photo= Photo.objects.get(pk=id_photo)
        photo.counter_like +=1
        photo.save()
        return Response (status= status.HTTP_202_ACCEPTED)
'''def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post_id = post.pk
    liked = False
    if request.session.get('has_liked_' + str(post_id), liked):
        liked = True
        print("liked {}_{}".format(liked, post_id))
    context = {'post': post, 'liked': liked}
    return render(request, 'blog/post_detail.html', context)
def like_count_blog(request):
    liked = False
    if request.method == 'GET':
        post_id = request.GET['post_id']
        post = Post.objects.get(id=int(post_id))
        if request.session.get('has_liked_'+post_id, liked):
            print("unlike")
            if post.likes > 0:
                likes = post.likes - 1
                try:
                    del request.session['has_liked_'+post_id]
                except KeyError:
                    print("keyerror")
        else:
            print("like")
            request.session['has_liked_'+post_id] = True
            likes = post.likes + 1
    post.likes = likes
    post.save()
    return HttpResponse(likes, liked)'''














