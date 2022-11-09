document.addEventListener('DOMContentLoaded', () => {
    menuItems = Array.from(document.getElementsByClassName('menu-item'));
    contentBtns = Array.from(document.getElementsByClassName('content-button'));
    contentBtns.forEach(btn => {
        btn.addEventListener('click', (event) => {
            for (let item of menuItems) {
                if(item.dataset.type == event.target.dataset.type) {
                    item.classList.remove('fade-out')
                    item.classList.add('fade-in')
                    item.classList.remove('hide')
                }
                else {
                    item.classList.remove('fade-in')
                    item.classList.add('fade-out')
                    item.classList.add('fade')
                    item.classList.add('hide')
                }
            }
        })
    });
})