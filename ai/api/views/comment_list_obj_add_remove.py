from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
from ai.models import CommentPool
from comment.models import CommentModel
from comment.api.serializers import CommentSerializer


class PoolCommentAddRemove(APIView):
    def get(self, request, pool_id, comment_id):
        pool: CommentPool = self.get_pool(pool_id)
        comment: CommentModel = self.get_comment_from_pool(pool, comment_id)
        if comment:
            comment: CommentSerializer = CommentSerializer(comment)
            return Response(comment.data, status.HTTP_200_OK)
        else:
            raise exceptions.NotFound("Comment not found")

    def post(self, request, pool_id, comment_id):
        pool: CommentPool = self.get_pool(pool_id)
        comment: CommentModel = self.get_comment_from_pool(pool, comment_id)
        if not comment:
            comment: CommentModel = self.get_comment(comment_id)
            if comment:
                pool.comments.add(comment)
                pool.save()
                return Response({"message": "Yorum başarıyla eklendi."}, status=status.HTTP_200_OK)
            else:
                raise exceptions.NotFound("Comment not found")

        else:
            return Response({"message": "Yorum zaten eklenmişti."}, status=status.HTTP_208_ALREADY_REPORTED)

    def delete(self, request, pool_id, comment_id):
        pool: CommentPool = self.get_pool(pool_id)
        comment: CommentModel = self.get_comment_from_pool(pool, comment_id)
        if comment:
            pool.comments.remove(comment)
            pool.save()
            return Response({"message": "Yorum başarıyla çıkarıldı."}, status=status.HTTP_200_OK)
        else:
            raise exceptions.NotFound("Comment not found")

    @staticmethod
    def get_pool(pool_id: str):
        return CommentPool.objects.filter(id=pool_id).first()

    @staticmethod
    def get_comment_from_pool(pool: CommentPool, comment_id: str):
        return pool.comments.filter(id=comment_id).first()

    @staticmethod
    def get_comment(comment_id: str):
        return CommentModel.objects.filter(id=comment_id).first()

