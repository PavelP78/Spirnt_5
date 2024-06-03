from faker import Faker
import datetime

fake = Faker('ru_RU')


def generate_order(color):
	first_name = fake.first_name()
	last_name = fake.last_name()
	address = fake.building_number() + ' ' + fake.street_name() + ', ' + fake.city()
	metro_station = fake.random_int(min=1, max=10)
	phone = fake.phone_number()
	rent_time = fake.random_int(min=1, max=10)
	delivery_date = (datetime.date.today() + datetime.timedelta(days=fake.random_int(min=1, max=365))).strftime('%Y-%m-%d')
	comment = fake.sentence(nb_words=3)
	color = color
	return {
		"firstName": first_name,
		"lastName": last_name,
		"address": address,
		"metroStation": metro_station,
		"phone": phone,
		"rentTime": rent_time,
		"deliveryDate": delivery_date,
		"comment": comment,
		"color": color
	}


def generate_courier_login():
	login = fake.first_name()
	return {
		"login": login
	}


def generate_courier_password():
	password = fake.password()
	return {
		"password": password
	}


def generate_courier_first_name():
	firstName = fake.first_name()
	return	{
		"firstName": firstName
	}
	
	