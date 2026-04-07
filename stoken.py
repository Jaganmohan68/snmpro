from itsdangerous import URLSafeTimedSerializer
salt="jagan123"
secret_key="snmprj"

'''For encryption'''
def endata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt=salt)
'''For Decryption'''
def dndata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt=salt,max_age=60)