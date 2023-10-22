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
        document.documentElement.style.setProperty('--current_user_color_2', colorHex + '2b');
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
    globalNav = document.getElementById('inopNav')
    if(menu.classList.contains('hideElement')){
        menu.classList.remove('hideElement')
        menu.classList.add('openingLateral')
        globalNav.classList.remove('hideElement')
        globalNav.classList.remove('justFadeHide')
        globalNav.classList.add('justFadeShow')
    }else{
        //item.classList.add('hideElement')
        menu.classList.remove('opening')
        menu.classList.add('closingLateral')
        globalNav.classList.remove('justFadeShow')
        globalNav.classList.add('justFadeHide')
        setTimeout(() => {
            menu.classList.remove('closingLateral')
            menu.classList.add('hideElement')
            globalNav.classList.add('hideElement')
            globalNav.classList.remove('justFadeShow')
            
        }, 300);
        
    }

}

function openPopDialog(title, descr, action, type='normal'){
    titleObject = document.getElementById('globalTitlePopDialogArea')
    descrObject = document.getElementById('globalDescrPopDialogArea')
    btAct = document.getElementById('globalGoBtPopDialogArea')

    titleObject.innerHTML = title
    descrObject.innerHTML = descr
    
    btAct.onclick = function() {
        eval(action)
    }

    globalObfs = document.getElementById('globalObfsPopDialog')
    popDial = document.getElementById('globalPopDialogArea')

    globalObfs.classList.remove('hideElement')
    globalObfs.classList.add('justFadeShow')
    popDial.classList.add('opening')
}

function closePopDialog(){
    globalObfs = document.getElementById('globalObfsPopDialog')
    popDial = document.getElementById('globalPopDialogArea')

    globalObfs.classList.remove('justFadeShow')
    globalObfs.classList.add('justFadeHide')
    popDial.classList.add('closing')

    setTimeout(() => {
        globalObfs.classList.add('hideElement')
        popDial.classList.remove('closing')
        globalObfs.classList.remove('justFadeHide')
    }, 300);
}
