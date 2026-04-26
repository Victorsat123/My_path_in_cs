// Вибираємо основні елементи
const track = document.querySelector('.slider-track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.next');
const prevButton = document.querySelector('.prev');

let currentIndex = 0;

// Функція для оновлення позиції стрічки
function updateSlidePosition() {
    // Отримуємо актуальну ширину слайда (важливо для адаптивності)
    const slideWidth = slides[0].getBoundingClientRect().width;
    // Зсуваємо стрічку за допомогою CSS Transform
    track.style.transform = `translateX(-${currentIndex * slideWidth}px)`;
}

// Кнопка "Вперед"
nextButton.addEventListener('click', () => {
    // Переходимо до наступного слайда. Якщо це останній — повертаємось на початок
    currentIndex = (currentIndex + 1) % slides.length;
    updateSlidePosition();
});

// Кнопка "Назад"
prevButton.addEventListener('click', () => {
    // Переходимо назад. Якщо це перший — йдемо в кінець
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
    updateSlidePosition();
});

// Оновлюємо позицію при зміні розміру вікна
window.addEventListener('resize', updateSlidePosition);