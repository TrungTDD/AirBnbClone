import random


def seed_obj(model, random_list, numbers) -> tuple:
    if numbers > len(random_list):
        return (
            "ERROR",
            f"The number is out of random ${model.str}. It should smaller than {len(random_list)}",
        )
    else:
        if numbers < -1:
            return ("ERROR", f"The number of object should be larger than 0")

        elif numbers == -1:
            # seed all obj
            create_obj = []
            for a in random_list:
                create_obj.append(model(title=a))
            try:
                model.objects.bulk_create(create_obj)
                return ("SUCCESS", f"Create {len(create_obj)} successfully")

            except Exception as e:
                return ("ERROR", e)
        else:

            obj_idxs = []
            create_obj = []
            for _ in range(numbers):
                obj_idx = random.randint(0, len(random_list) - 1)

                while obj_idx in obj_idxs:
                    obj_idx = random.randint(0, len(random_list) - 1)
                obj_idxs.append(obj_idx)

                create_obj.append(model(title=random_list[obj_idx]))
            try:
                model.objects.bulk_create(create_obj)
                return ("SUCCESS", f"Create {len(create_obj)} successfully")
                
            except Exception as e:
                return ("ERROR", e)