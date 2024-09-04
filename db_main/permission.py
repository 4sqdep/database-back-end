from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsNotStaffUserPermission(BasePermission):
    """
    Faqat is_staff=False bo'lgan foydalanuvchilarga Project modelga post qilishga ruxsat beradi.
    """

    def has_permission(self, request, view):
        # Agar POST so'rovi bo'lsa, ruxsatni tekshiradi
        if request.method == 'POST':
            if request.user.is_staff:
                # Foydalanuvchiga maxsus xabar yuboradi
                raise PermissionDenied(
                    detail="Siz POST so'rovi yubora olmaysiz, chunki sizda ruxsat mavjudemas.")
            # Boshqa metodlarga ruxsat beriladi
        return True