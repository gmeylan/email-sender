from ldap3 import Server, Connection, ALL, ObjectDef, Reader
import os


def connect_to_ldap():
    server = Server(os.getenv('LDAP_SERVER_HOST'), get_info=ALL)
    return Connection(server, auto_bind=True)


def create_user(user):
    conn = connect_to_ldap()

    result = conn.add('cn=b.young,ou=ldap3-tutorial,dc=demo1,dc=freeipa,dc=org', "inetOrgPerson",
        {'givenName': user.get_complete_name(), 'departmentNumber': user.department_number,
         'telephoneNumber': user.telephone_number, 'mail': user.email, 'password': user.password})
    return result


