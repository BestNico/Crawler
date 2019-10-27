from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Date, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import pymysql

pymysql.install_as_MySQLdb()

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "root",
    "1234",
    "localhost:3306",
    "sqlalchemy",
)
ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
session = scoped_session(
  # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# 基本类
Base = declarative_base()


# 表要继承基本类
class User(Base):
    __tablename__ = 'users' # 表的名字

    # 定义各字段
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(200))
    age = Column('age', Integer)
    email = Column('email', String(100))

    def __str__(self):
        return self.id

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)
    gender = Column(Enum('F', 'M'), nullable=False)

    def __repr__(self):
        return "id:%s name:%s register_date:%s gender:%s" \
               %(self.id,self.name, self.register_date, self.gender)

class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    name = Column(String(32), nullable=False)
    score = Column(Integer, nullable=False)
    stu_id = Column(Integer, ForeignKey("student.id"))

    def __repr__(self):
        return "id:%s day:%s name:%s score:%s stu_id:%s" \
               %(self.id, self.day, self.name, self.score, self.stu_id)


# 创建表
Base.metadata.create_all(ENGINE)