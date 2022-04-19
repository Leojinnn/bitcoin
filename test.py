import pyupbit


access = "Kh8RhXq6K97pMMs1buQtqBuYmujzBxhRpmKwf0OT"          # 본인 값으로 변경
secret = "Tp5C1ihnyxl2cUGbzGAGSFYd4seg2F8YSZhF3uK9"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회