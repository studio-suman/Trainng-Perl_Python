import ldap3
server = ldap3.Server('ldap://blr-ec-dc07.wipro.com', port =636, use_ssl = True)
connection = ldap3.Connection(server, 'uid=hsass,cn=USERS,dc=wipro,dc=com', 'ganga@345', auto_bind=True)
connection.bind()