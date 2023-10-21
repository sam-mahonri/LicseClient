function showElement(id){
    element = document.getElementById(id)
    element.classList.add('fadeIn')
    element.classList.remove('hideElement')
}

function verifyColor(self){
    var corDeFundo = window.getComputedStyle(self, null).getPropertyValue('background-color');
    document.documentElement.style.setProperty('--current_user_color', corDeFundo);
    document.documentElement.style.setProperty('--current_user_color_2', rgbToHex(corDeFundo) + '41');
    document.getElementById('colorInput').value = rgbToHex(corDeFundo)
}

function rgbToHex(rgb) {
    var partes = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    delete partes[0];
    for (var i = 1; i <= 3; ++i) {
        partes[i] = parseInt(partes[i]).toString(16);
        if (partes[i].length == 1) partes[i] = '0' + partes[i];
    }
    return '#' + partes.join('');
}

function callColor(colorHex){
    if (colorHex.length == 7){
        document.documentElement.style.setProperty('--current_user_color', colorHex);
        document.documentElement.style.setProperty('--current_user_color_2', colorHex + '41');
    }
    
}

function updateInput(colorHex){
    document.getElementById('colorInput').value = colorHex
}

function verifyConfPasswords(element1, element2){
    element1 = document.getElementById(element1)
    element2 = document.getElementById(element2)
    if(element1.value != element2.value){
        element2.classList.add('invalidInput')
    }else{
        element2.classList.remove('invalidInput')
    }
}

function openPop(itemId, self){
    item = document.getElementById(itemId)
    hoverAll = document.getElementById('hoverAll')
    if(item.classList.contains('hideElement')){
        item.classList.remove('hideElement')
        item.classList.add('opening')
        hoverAll.classList.remove('hideElement')
    }else{
        //item.classList.add('hideElement')
        item.classList.remove('opening')
        item.classList.add('closing')
        setTimeout(() => {
            item.classList.remove('closing')
            item.classList.add('hideElement')
        }, 300);
        hoverAll.classList.add('hideElement')
    }
}

function notifArea(nature, message){
    var notifArea = document.getElementById('notifArea')
    var notifError = document.getElementById('notifAreaErrorMessage')
    var notifSuccess = document.getElementById('notifAreaSuccessMessage')

    notifArea.classList.remove('hideElement')
    notifSuccess.classList.add('hideElement')
    notifError.classList.add('hideElement')
    notifArea.classList.add('opening')

    setTimeout(() => {
        notifArea.classList.add('hideElement')
        notifSuccess.classList.add('hideElement')
        notifError.classList.add('hideElement')
        notifArea.classList.remove('closing')
    }, 5000);

    setTimeout(() => {
        notifArea.classList.remove('opening')
        notifArea.classList.add('closing')
    }, 4700);

    if (nature == "ERROR"){
        notifError.classList.remove('hideElement')
        notifSuccess.classList.add('hideElement')
        notifError.innerHTML = message
    }else if (nature == "SUCCESS"){
        notifSuccess.classList.remove('hideElement')
        notifError.classList.add('hideElement')
        notifSuccess.innerHTML = message
    }
}

function openMenu(menuId){
    menu = document.getElementById(menuId)
    if(menu.classList.contains('hideElement')){
        menu.classList.remove('hideElement')
        menu.classList.add('openingLateral')
    }else{
        //item.classList.add('hideElement')
        menu.classList.remove('opening')
        menu.classList.add('closingLateral')
        setTimeout(() => {
            menu.classList.remove('closingLateral')
            menu.classList.add('hideElement')
        }, 300);
    }

}