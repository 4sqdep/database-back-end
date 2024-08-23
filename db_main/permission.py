from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import APIException


class CustomPermissionDenied(APIException):
    status_code = 403
    default_detail = "Sizda bu amalni bajarish uchun ruxsat yo‘q."
    default_code = 'ruxsat berilmadi'

    def __init__(self, detail=None, code=None):
        if detail:
            self.detail = detail
        if code:
            self.code = code

class IsNotStaffUserPermission(BasePermission):
    """
    Faqat is_staff=False bo'lgan foydalanuvchilarga Project modelga post qilishga ruxsat beradi.
    """

    def has_permission(self, request, view):
        # Agar POST so'rovi bo'lsa, ruxsatni tekshiradi
        if request.method == 'POST':
            if request.user.is_staff:
                # Foydalanuvchiga maxsus xabar yuboradi
                raise CustomPermissionDenied(
                    detail="Siz POST so'rovi yubora olmaysiz, chunki sizda ruxsat mavjudemas.")
            return True
            # Boshqa metodlarga ruxsat beriladi
        return True