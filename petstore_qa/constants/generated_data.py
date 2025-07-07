from faker import Faker

from petstore_qa.constants.dataclasses import UserModel

fake = Faker()


user_data = UserModel(
        id=fake.random_int(min=1, max=1000),
        username=fake.user_name(),
        firstName=fake.first_name(),
        lastName=fake.last_name(),
        email=fake.email(),
        password=fake.password(length=12),
        phone=fake.phone_number(),
        userStatus=fake.random_int(min=0, max=1)
    )
