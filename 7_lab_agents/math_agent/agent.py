from google.adk.agents.llm_agent import Agent
import math

def calculate_rectangle_area(width: float, height: float) -> float:
    """
    Обчислює площу прямокутника.
    
    Args:
        width: ширина прямокутника
        height: висота прямокутника
    
    Returns:
        float: площа прямокутника
    """
    return width * height

def calculate_circle_area(radius: float) -> float:
    """
    Обчислює площу кола.
    
    Args:
        radius: радіус кола
    
    Returns:
        float: площа кола
    """
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """
    Обчислює об'єм куба.
    
    Args:
        side: довжина ребра куба
    
    Returns:
        float: об'єм куба
    """
    return side ** 3

def calculate_cylinder_volume(radius: float, height: float) -> float:
    """
    Обчислює об'єм циліндра.
    
    Args:
        radius: радіус основи циліндра
        height: висота циліндра
    
    Returns:
        float: об'єм циліндра
    """
    return math.pi * (radius ** 2) * height

# Створюємо математичного агента з повним набором інструментів
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='math_agent',
    description="Виконує математичні обчислення площ та об'ємів геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент, який допомагає з геометричними розрахунками.
    У тебе є інструменти для обчислення:
    1. Площі прямокутника (calculate_rectangle_area)
    2. Площі кола (calculate_circle_area)
    3. Об'єму куба (calculate_cube_volume)
    4. Об'єму циліндра (calculate_cylinder_volume)

    Використовуй ці інструменти, коли користувач просить виконати відповідні розрахунки.
    Завжди відповідай українською мовою, чітко вказуй, який інструмент було використано, 
    та пояснюй хід обчислень (наприклад, згадуй формулу).
    """,
    tools=[
        calculate_rectangle_area, 
        calculate_circle_area, 
        calculate_cube_volume, 
        calculate_cylinder_volume
    ],
)