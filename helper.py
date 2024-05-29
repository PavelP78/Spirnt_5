import random

def generate_random_order():
	first_name = random.choice(['Naruto', 'Sasuke', 'Sakura'])
	last_name = random.choice(['Uchiha', 'Hatake', 'Haruno'])
	address = f"Konoha, {random.randint(100, 200)} apt."
	metro_station = random.randint(1, 9)
	phone = f"+7 {''.join(random.choices('0123456789', k=10))}"
	rent_time = random.randint(1, 10)
	delivery_date = f"{random.choice(['2024', '2025'])}-{random.choice(['01', '06'])}-{random.choice(['01', '06'])}"
	comment = f"{random.choice([first_name, last_name])}, come back to Konoha"
	
	return {"firstName": first_name, "lastName": last_name, "address": address, "metroStation": metro_station,
			"phone": phone, "rentTime": rent_time, "deliveryDate": delivery_date, "comment": comment}
