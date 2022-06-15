class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        sm = int(loginTime[:2]) * 60 + int(loginTime[-2:])
        em = int(logoutTime[:2]) * 60 + int(logoutTime[-2:])
        print(sm, em)
        
        if sm > em:
            em += 24 * 60
            
        q, r = divmod(sm, 15)
        start, end = q + int(r > 0), em // 15
        return max(0, end - start)

# self-help answer
#         login_h, login_m  = loginTime.split(':')
#         logout_h, logout_m  = logoutTime.split(':')
#         login_h, login_m = int(login_h), int(login_m)
#         logout_h, logout_m = int(logout_h), int(logout_m)
        
#         if login_h == logout_h:
#             if login_m < logout_m and logout_m - login_m < 15:
#                 return 0
        
#         if login_m not in [0,15,30,45]:
#             if login_m < 15:
#                 login_m = 15
#             elif login_m < 30:
#                 login_m = 30
#             elif login_m < 45:
#                 login_m = 45
#             elif login_m > 45:
#                 login_m = 0
#                 login_h += 1
#                 if login_h > 23:
#                     login_h = login_h - 24

#         if logout_m not in [0,15,30,45]:
#             if logout_m < 15:
#                 logout_m = 0
#             elif logout_m < 30:
#                 logout_m = 15
#             elif logout_m < 45:
#                 logout_m = 30
#             elif logout_m > 45:
#                 logout_m = 45

#         print(login_h, login_m)
#         print(logout_h, logout_m)
#         if login_h < logout_h:
#             if logout_m > login_m:
#                 hm = logout_h - login_h
#                 return hm * 4 + (logout_m - login_m) // 15
#             else:
#                 hm = logout_h - login_h - 1
#                 return hm * 4 + (60 + logout_m - login_m) // 15
#         elif login_h > logout_h:
#             if logout_m > login_m:
#                 hm = 24 + logout_h - login_h
#                 return hm * 4 + (logout_m - login_m) // 15
#             else:
#                 hm = 24 + logout_h - login_h - 1
#                 return hm * 4 + (60 + logout_m - login_m) // 15
#         elif login_h == logout_h:
#             if logout_m > login_m:
#                 return (logout_m - login_m) // 15
#             elif logout_m == login_m:
#                 return 0
#             else:
#                 hm = 24 - 1
#                 return hm * 4 + (60 + logout_m - login_m) // 15