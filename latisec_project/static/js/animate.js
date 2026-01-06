document.addEventListener('DOMContentLoaded', () => {
    const counters = document.querySelectorAll('.counter');
    if (!counters.length) return;

    const speed = 200;

    const animateCounter = (counter) => {
        const target = parseFloat(counter.dataset.target);
        let current = 0;
        const increment = target / speed;

        const update = () => {
            current += increment;
            if (current < target) {
                counter.textContent = Math.ceil(current * 10) / 10;
                requestAnimationFrame(update);
            } else {
                counter.textContent = target + (target % 1 !== 0 ? '%' : '');
            }
        };

        update();
    };

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.querySelectorAll('.counter').forEach(counter => {
                    if (!counter.classList.contains('animated')) {
                        counter.classList.add('animated');
                        animateCounter(counter);
                    }
                });
            }
        });
    }, { threshold: 0.5 });

    const statsSection = document.querySelector('.stats-section');
    if (statsSection) observer.observe(statsSection);
});
