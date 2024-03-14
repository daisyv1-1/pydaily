def main():
    card_number = '4829-1450-5013-0644'
    trcard =  str.maketrans({'-':'', ':':''})
    new_num = card_number.translate(trcard)
    if verification(new_num):
        print("valid credit card number")
    else:
        print("invalid credit card number")

def verification(card_valid):
    revcard = card_valid[::-1]
    def sumodd(nums):
        oddnum = nums[::2]
        sum_odd = 0
        for digit in oddnum:
            sum_odd += int(digit)
        return sum_odd
    def sumeven(nums):
        evennum = nums[1::2]
        sum_even = 0
        for digit in evennum:
            number = int(digit)*2
            if number >= 10:
                sum_even += (number//10) + (number % 10)
            else:
                sum_even += number
        return sum_even
    sum1 = sumodd(revcard)
    sum2 = sumeven(revcard)
    total = sum1 + sum2
    return 0==total%10

main()