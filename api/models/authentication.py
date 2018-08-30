import jwt
import time
import datetime

class Decod():


    def encode_token(self, user_id):
        """
        
        Decodes the auth token

        :param auth_token:

        :return:

        """
        token = jwt.encode({'user': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1)}, "kalyango").decode()
        return token
    def decode_token(self, token):

        """
        
        Decodes the auth token

        :param auth_token:

        :return:

        """

        try:

            decoded_value = jwt.decode(token, "kalyango")

            return decoded_value['user']
            # return "yes"

        except jwt.ExpiredSignatureError:

            return 'Token expired. You have to log in again.'

        except jwt.InvalidTokenError:

            return 'Invalid Token. You have to log in again.'