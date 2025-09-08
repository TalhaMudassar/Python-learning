def idle_chaiwala():
    pass

print(idle_chaiwala())

def sold_cup():
    return 120
total = sold_cup()

print(total)

def chai_status(cup_left):
    if cup_left == 0:
        return "sorry chai is over! "
    return "chai is ready to serve"


print(chai_status(0))
print(chai_status(5))

print("----------------------------------")
def chai_report():
    return 100,20,5

sale,reproduce,_ =chai_report()
print("sale are ",sale)
print("reproduce are ",reproduce)