from mongoengine import *
from querysets import GuidingLandsQuery

class Lfg(Document):
    message_id = IntField(required=True)
    confirmed = ListField(IntField())
    tentative = ListField(IntField())
    time = StringField()
    lfg_type = StringField()
    channel_id = IntField()
    pin_msg_id = IntField()

class Player(Document):
    player_id = IntField(required=True)
    display_name = StringField()
    remarks = StringField()
    levels = DictField()
    available = BooleanField(default=False)

    meta = {'queryset_class': GuidingLandsQuery}

class Session(Document):
    message_id = IntField(required=True)
    session_id = StringField(required=True)
    #report_player = ListField(IntField())
    session_creator = IntField(required=True)
    description = StringField()
