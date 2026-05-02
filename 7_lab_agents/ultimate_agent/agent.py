from google.adk.agents.llm_agent import Agent
from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.loop_agent import LoopAgent

# --- ІНСТРУМЕНТ ДЛЯ ЦИКЛУ ---
def exit_loop() -> dict:
    """Викликай цю функцію, коли звіт повністю готовий і схвалений."""
    return {"status": "finished", "message": "Звіт затверджено!"}

# --- 1. ЕТАП: ПАРАЛЕЛЬНИЙ ЗБІР ДАНИХ (Parallel) ---
tech_researcher = Agent(
    model='gemini-2.5-flash',
    name='tech_researcher',
    instruction="Ти технічний дослідник. Знайди 2-3 головні технологічні інновації за темою, яку дасть користувач."
)
market_researcher = Agent(
    model='gemini-2.5-flash',
    name='market_researcher',
    instruction="Ти бізнес-аналітик. Опиши фінансові перспективи та вплив на ринок за темою, яку дасть користувач."
)
parallel_gatherer = ParallelAgent(
    name='parallel_gatherer',
    description="Паралельно збирає технічні та бізнес-дані.",
    sub_agents=[tech_researcher, market_researcher]
)

# --- 2. ЕТАП: ОБРОБКА ДАНИХ (Agent) ---
data_processor = Agent(
    model='gemini-2.5-flash',
    name='data_processor',
    instruction="Ти аналітик. Прочитай сирі дані від дослідників і склади з них структурований чорновик звіту (Вступ, Технології, Ринок, Висновок)."
)

# --- 3. ЕТАП: ПОКРАЩЕННЯ ЗВІТУ (Loop) ---
writer = Agent(
    model='gemini-2.5-flash',
    name='writer',
    instruction="Ти професійний копірайтер. Перепиши чорновик звіту, щоб він звучав солідно. Якщо директор дає правки - виправ текст."
)
director = Agent(
    model='gemini-2.5-flash',
    name='director',
    instruction="Ти суворий директор. Прочитай звіт копірайтера. Якщо він короткий або сухий - напиши, що додати. Якщо звіт розгорнутий і красивий - ОБОВ'ЯЗКОВО виклич інструмент 'exit_loop', щоб зупинити роботу.",
    tools=[exit_loop]
)
loop_optimizer = LoopAgent(
    name='loop_optimizer',
    description="Цикл: копірайтер пише, директор перевіряє.",
    sub_agents=[writer, director],
    max_iterations=2 # Ставимо 2, щоб зекономити твій денний ліміт запитів!
)

# --- 4. ФІНАЛЬНА ЗБІРКА: ПОСЛІДОВНИЙ КОНВЕЄР (Sequential) ---
root_agent = SequentialAgent(
    name='ultimate_workflow',
    description="Збір даних (Parallel) -> Обробка -> Покращення (Loop).",
    sub_agents=[parallel_gatherer, data_processor, loop_optimizer]
)