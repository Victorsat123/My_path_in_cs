from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, CheckConstraint, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func

# Базовий клас
class Base(DeclarativeBase):
    pass

# 1. Таблиця Category
class Category(Base):
    __tablename__ = 'categories'
    
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    color_hex = Column(String(10), nullable=False)
    
    # Зв'язок 1:N (Одна категорія має багато цілей)
    goals = relationship("Goal", back_populates="category")

# 2. Таблиця User
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    total_xp = Column(Integer, default=0)
    
    # На діаграмі є level_id (FK), але немає самої таблиці Level. 
    # Поки залишаємо просто як числове поле.
    level_id = Column(Integer) 
    
    __table_args__ = (
        CheckConstraint('total_xp >= 0', name='check_total_xp_positive'),
    )
    
    # Зв'язок 1:N (Один юзер має багато цілей)
    goals = relationship("Goal", back_populates="user")

# 3. Таблиця Goal
class Goal(Base):
    __tablename__ = 'goals'
    
    goal_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    title = Column(String(100), nullable=False)
    deadline = Column(Date)
    status = Column(String(50))
    
    # Зворотні зв'язки
    user = relationship("User", back_populates="goals")
    category = relationship("Category", back_populates="goals")
    # Зв'язок 1:N до завдань
    tasks = relationship("Task", back_populates="goal")

# 4. Таблиця Task
class Task(Base):
    __tablename__ = 'tasks'
    
    task_id = Column(Integer, primary_key=True, autoincrement=True)
    goal_id = Column(Integer, ForeignKey('goals.goal_id'))
    task_name = Column(String(100), nullable=False)
    xp_reward = Column(Integer, nullable=False)
    priority = Column(Integer, default=1)
    
    __table_args__ = (
        CheckConstraint('xp_reward > 0', name='check_xp_reward_positive'),
        CheckConstraint('priority BETWEEN 1 AND 5', name='check_priority_range'),
    )
    
    goal = relationship("Goal", back_populates="tasks")
    
    # Зв'язок 1:1 до ProgressLog (uselist=False означає, що це один об'єкт, а не список)
    progress_log = relationship("ProgressLog", back_populates="task", uselist=False)

# 5. Таблиця ProgressLog
class ProgressLog(Base):
    __tablename__ = 'progress_logs'
    
    log_id = Column(Integer, primary_key=True, autoincrement=True)
    # unique=True робить зв'язок строго 1:1 на рівні бази даних
    task_id = Column(Integer, ForeignKey('tasks.task_id'), unique=True) 
    entry_date = Column(DateTime, default=func.now(), nullable=False)
    notes = Column(Text)
    success_rate = Column(Integer)
    
    __table_args__ = (
        CheckConstraint('success_rate BETWEEN 0 AND 100', name='check_success_rate_range'),
    )
    
    task = relationship("Task", back_populates="progress_log")


# ==========================================
# ЗАПУСК СТВОРЕННЯ БАЗИ
# ==========================================
if __name__ == "__main__":
    # ЗАМІНІТЬ 'your_password' НА ВАШ РЕАЛЬНИЙ ПАРОЛЬ ВІД MYSQL
    DATABASE_URL = "mysql+pymysql://root:victor123321@localhost:3306/progress_hub"
    
    engine = create_engine(DATABASE_URL, echo=True)
    
    # Ця команда бере всі класи вище і створює для них таблиці в MySQL
    Base.metadata.create_all(bind=engine)
    print("Таблиці успішно створені!")