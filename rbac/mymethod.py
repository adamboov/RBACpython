from rbac.models import UserInfo, Role, Permission, RoleToUser, PerToRole

def get_roles_by_user_id(user_id):
    rolesinfo = []
    roles = RoleToUser.objects.filter(UserId=user_id)
    for i in roles:
        role = Role.objects.get(ID=i.RoleId)
        rolesinfo.append(role)
    return rolesinfo


def get_permission_by_role_id(role_id):
    perinfo = []
    permissions = PerToRole.objects.filter(RoleId=role_id)
    for i in permissions:
        per = Permission.objects.get(ID=i.PerId)
        perinfo.append(per)
    return perinfo


def set_per_to_role(role_id, per_id):
    PerToRole.objects.create(PerId=per_id, RoleId=role_id).save()

