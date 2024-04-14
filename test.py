# month 입력
while True:
    try:
        month = int(input("Month : "))
        if month > 12: 
            raise NotImplementedError
        break
    except NotImplementedError:
        print("12월까지만 입력해주세용")
    except ValueError:
        print("숫자를 입력해주세용")

# day 입력
# 몇 월인지 확인
thir_o_d = [1, 3, 5, 7, 8, 10, 12]   # thirty_one_days
thir_d = [4, 6, 9, 11]      #thirty_days

for i in thir_o_d:
    if month == i:
        while True:
            try:
                day = int(input("Day : "))
                if day > 31:
                    raise NotImplementedError
                break
            except NotImplementedError:
                print("31일까지만 입력해주세용")
            except ValueError:
                print("숫자를 입력해주세용")
        break

for i in thir_d:
    if month == i:
        while True:
            try:
                day = int(input("Day : "))
                if day > 30:
                    raise NotImplementedError
                break
            except NotImplementedError:
                print("30일까지만 입력해주세용")
            except ValueError:
                print("숫자를 입력해주세용")
        break



if __name__ == "__main__":
    print("{}월 {}일".format(month, day))