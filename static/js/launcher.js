const getCard = (app_name) => {
    const cards = document.querySelectorAll('#app-cards .apppanel');
    for (const card of cards) {
        if (card.id != app_name) continue;
        return card;
    }
    return undefined;
}

var current_app = undefined;
var interval = 60;

const selectapp = (app_name) => {
    const card = getCard(app_name);
    if (!card) return;        
    card.classList.add("appcard-slidein");

    setTimeout(() => {
        current_app = app_name;
        document.addEventListener('click', closeapp);  
    }, interval);
}

const closeapp = (e) => {
    const card = getCard(current_app);
    if (!card) return;
    if (e.target.closest('.apppanel')) return;
    card.classList.remove("appcard-slidein");

    setTimeout(() => {
        document.removeEventListener('click', closeapp); 
        current_app = undefined;
    }, interval);
}



