from smartphone import Smartphone

catalog = [
    Smartphone('Apple', 'Iphone 14 Pro', '+79012345678'),
    Smartphone('Xiaomy', 'Redmi 9', '+79018765432'),
    Smartphone('Huawei', ' Realme 7 5g', '+79123456789'),
    Smartphone('Samsung', 'Galaxy A25', '+79876543210'),
    Smartphone('OnePlus', 'Nord N30', '+79098765432')
]

for s in catalog:
    print(f"{s.brandphone} - {s.modelphone}. {s.subnumber}")
