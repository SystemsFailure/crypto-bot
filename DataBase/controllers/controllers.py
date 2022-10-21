from datetime import datetime
import sqlalchemy.exc
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
import logging
from DataBase.connect_to_db import Connect
from DataBase.models.models import User
conn = Connect()
engine, Base = conn.get_settings()

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(filename='logs_controllers.log', level=logging.DEBUG)
log = logging.getLogger('controller-logger')


class UserController:
    def __init__(self):
        self.session = Session(bind=engine)
        self.name = 'name'
        self.email = 'email'
        self.password = 'password'

    def get_user(self, user_id) -> object:
        # user = self.session.query(User).filter(and_(User.id == user_id, User.username == 'Elena'))
        user = self.session.query(User).get(user_id)
        return user

    def get_all_users(self):
        return self.session.query(User).all()

    def get_limit_users(self, limit, offset: int = 0, mode: bool = True) -> object:
        start_time = datetime.now()
        log.info(f' started function : {self.get_limit_users.__name__}, date : '
                 f'{datetime.now()} '
                 f'{datetime.now()}')
        if mode is True:
            try:
                log.info('function work on the if mode is True')
                count = self.session.query(User).count()
                user_of_limit = self.session.query(User).offset(offset=offset).limit(limit=limit)
                log.info(f' ending function : {self.get_limit_users.__name__}, date : '
                         f'{datetime.now()} '
                         f'{datetime.now()}, time completing of script : {datetime.now() - start_time} .s')
                return user_of_limit, count
            except sqlalchemy.exc.DataError as exc:
                log.error(f'{exc} or data is null')
        else:
            try:
                log.info('function work on the if mode is False')
                count = self.session.query(User).count()
                user_of_limit = self.get_all_users()
                lim = user_of_limit[offset:limit]
                log.info(f' ending function : {self.get_limit_users.__name__}, date : '
                         f'{datetime.now()} '
                         f'{datetime.now()}, time completing of script : {datetime.now() - start_time} .s')
                return lim, count
            except sqlalchemy.exc.DataError as exc:
                log.error(f'{exc} or data is null')

    def create_user(self, name, email, password):
        start_time = datetime.now()
        log.info(f' started function : {self.create_user.__name__}, date : '
                 f'{datetime.now()} '
                 f'{datetime.now()}')
        try:
            user = User(
                username=name,
                email=email,
                password=password
            )
            self.session.add(user)
            self.session.commit()
            log.info(f' ending function : {self.create_user.__name__}, date : '
                     f'{datetime.now()} '
                     f'{datetime.now()}, time completing of script : {datetime.now() - start_time} .s')
            return user
        except Exception as ex:
            log.error(f'{ex} not answer {self.create_user.__name__}  : date - {datetime.now()}')
            return False

    def update_user_field(self, id_, **kwargs):
        user = self.get_user(id_)
        arr = ['name', 'email', 'password']
        for field, value in kwargs.items():
            if field not in arr:
                print(f'some field: {field} not found! Exchange field')
                break
            match field:
                case self.name:
                    user.username = value
                    self.session.add(user)
                    self.session.commit()
                case self.email:
                    user.email = value
                    self.session.add(user)
                    self.session.commit()
                case self.password:
                    user.password = value
                    self.session.add(user)
                    self.session.commit()

    def get_by_id(self, u_id) -> int:
        user = self.session.query(User).get(u_id)
        return user.user_id
