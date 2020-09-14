from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Board, Favorite, Article, Comment
from .serializers import BoardSerializer

# Create your views here.
class Boards(APIView):
  def get(self, request):
    boards = Board.objects.all()
    serializer = BoardSerializer(boards, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = BoardSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetail(APIView):
  def get(self, request, board_pk):
    board = Board.objects.get(pk=board_pk)
    serializer = BoardSerializer(board)
    return Response(serializer.data)

  def put(self, request, board_pk):
    board = Board.objects.get(pk=board_pk)
    serializer = BoardSerializer(board, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, board_pk):
      board = Board.objects.get(pk=board_pk)
      board.delete()
      return Response(status=200)