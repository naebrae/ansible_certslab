#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import ldap

def getLdapUsers(ldapURL="ldaps://localhost:636", ldapDN="cn=Directory Manager", ldapPWD=""):

    l = ldap.initialize(ldapURL)
    try:
        l.simple_bind_s(ldapDN, ldapPWD)

        baseDN = "dc=lab,dc=home"
        searchScope = ldap.SCOPE_SUBTREE
        searchFilter = "uid=janed"
        users = {}
        ldap_result_id = l.search(baseDN, searchScope, searchFilter)
        while 1:
            rType, rData = l.result(ldap_result_id, 0)
            if (rData == []):
                break
            else:
                if rType == ldap.RES_SEARCH_ENTRY:
                    cn = rData[0][0]
                    data = rData[0][1]

                    #Flatten, just for more easy access
                    for (k, v) in data.items():
                        if len(v) == 1:
                            data[k] = v[0]

                    uid = data["uid"]
                    users[cn] = data
        return users;
    except ldap.LDAPError as e:
        print(e)
    finally:
        l.unbind_s()
    return 0

def main():
    ldapUsers = getLdapUsers('ldaps://ldap.lab.home:1636', 'uid=johnd,ou=people,dc=lab,dc=home', 'Password1')
    print(ldapUsers)

if __name__ == "__main__":
    sys.exit(main())

