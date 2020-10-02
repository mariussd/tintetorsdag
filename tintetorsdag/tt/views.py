from tintetorsdag.tt.models import User, Tint
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from tintetorsdag.tt.serializers import (
    UserSerializer,
    SetTintSerializer,
    TintSerializer,
)
from tintetorsdag.tt.permissions import IsOwnerOrReadOnly
from tintetorsdag.tt.utils import is_thursday
from datetime import date
from rest_framework.decorators import action


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    @action(detail=False, methods=["post"], serializer_class=SetTintSerializer)
    def tint(self, request):
        if not is_thursday():
            return Response(
                {"error": "Det er ikke torsdag :("}, status=status.HTTP_400_BAD_REQUEST
            )
        serializer = SetTintSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        should_be_tinting = serializer.validated_data["is_tinting"]
        if should_be_tinting == request.user.is_tinting:
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        today = date.today()
        if should_be_tinting:
            tint = Tint.objects.create(created=today, user=request.user)
            return Response(TintSerializer(tint).data, status=status.HTTP_200_OK)
        else:
            request.user.tints().get(created=today).delete()
            return Response({}, status=status.HTTP_200_OK)
