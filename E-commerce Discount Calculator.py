BaseDiscount=0
LoyalityDiscount=0
CouponDiscount=0
CoupenCode='SALE500'

Price=float(input("Enter the total purchase amount LKR:"))
current_price=Price
if(Price>5000):
    BaseDiscount=Price*10/100
    current_price=current_price-BaseDiscount

LoyalStatus=input("Are you a loyality member (yes or no)")
if(LoyalStatus=="yes"):
    LoyalityDiscount=current_price*5/100
    current_price=current_price-LoyalityDiscount

User_input=input("Do you have a coupon code or press enter(or press Enter for none)")
if(User_input==CoupenCode and current_price>500):
    CouponDiscount=500
    current_price=current_price-CouponDiscount

print("Your final price after all discounts is LKR:",current_price)





