import random 
import string 

id_users = list(range(1, 101))
id_penerima = list(range(1, 101))

def generate_message() -> dict:
    random_user_id = random.choice(id_users)

    # Copy data array id_penerima
    copy_id_penerima = id_penerima.copy()

    # User can't send message to himself
    copy_id_penerima.remove(random_user_id)
    acak_id_penerima = random.choice(copy_id_penerima)

    # Generate a random message
    message = ''.join(random.choice(string.ascii_letters) for i in range(32))

    return {
        'user_id': random_user_id,
        'recipient_id': acak_id_penerima,
        'message': message
    }
    
if __name__ == '__main__':
        print(generate_message())