// Scroll fade-in
const fadeElements = document.querySelectorAll('.fade-in');

const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if(entry.isIntersecting){
            entry.target.style.opacity = 1;
            entry.target.style.transform = 'translateY(0)';
            observer.unobserve(entry.target);
        }
    });
}, { threshold: 0.2 });

fadeElements.forEach(el => observer.observe(el));

// Tabs functionality
const tabs = document.querySelectorAll('.tab-btn');
const grids = document.querySelectorAll('.amenities-grid');

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        tabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        const target = tab.getAttribute('data-target');
        grids.forEach(grid => {
            if(grid.id === target){
                grid.classList.add('active');
            } else {
                grid.classList.remove('active');
            }
        });
    });
});
