document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('achievementModal');
    const closeBtn = document.querySelector('.close-button');
    const achvCards = document.querySelectorAll('.achv-card');

    achvCards.forEach(card => {
        card.addEventListener('click', () => {
            // 1. Отримуємо тексти з картки
            const title = card.querySelector('h3').innerText;
            const desc = card.querySelector('.achv-desc').innerText;
            const xpText = card.querySelector('.xp-reward').innerText; 
            const iconHtml = card.querySelector('.achv-icon').innerHTML;
            const badgeText = card.querySelector('.achv-badge').innerText;
            
            // 2. Визначаємо рідкість картки, щоб задати правильний колір вікну
            let rarityClass = 'common';
            if (card.classList.contains('rare')) rarityClass = 'rare';
            else if (card.classList.contains('epic')) rarityClass = 'epic';
            else if (card.classList.contains('legendary')) rarityClass = 'legendary';

            // Чи заблоковано досягнення?
            const isLocked = card.querySelector('.achv-icon').classList.contains('dim');

            // 3. Заповнюємо тексти в модальному вікні
            document.getElementById('modalTitle').innerText = title;
            document.getElementById('modalDesc').innerText = desc;
            document.getElementById('modalXP').innerText = xpText;
            
            // 4. Оновлюємо іконку та її колір (передаємо клас рідкості)
            const modalIcon = document.getElementById('modalIcon');
            modalIcon.innerHTML = iconHtml;
            modalIcon.className = `modal-main-icon ${rarityClass}`; 
            // Якщо іконка була заблокована на картці, робимо її тьмяною і у вікні
            if(isLocked) modalIcon.style.opacity = "0.4";
            else modalIcon.style.opacity = "1";

            // 5. Оновлюємо бейдж (колір і текст)
            const modalBadge = document.getElementById('modalBadge');
            modalBadge.innerText = badgeText;
            modalBadge.className = `achv-badge ${rarityClass}`;

            // Якщо заблоковано, робимо XP сірим
            const modalXP = document.getElementById('modalXP');
            modalXP.className = isLocked ? 'xp-reward dim' : 'xp-reward';

            // 6. Показуємо вікно
            modal.style.display = "block";
        });
    });

    // Закриття вікна
    closeBtn.onclick = () => modal.style.display = "none";
    window.onclick = (event) => {
        if (event.target == modal) modal.style.display = "none";
    }
});