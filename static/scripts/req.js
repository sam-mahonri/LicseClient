var currentBtChat = ''
var curChat = ''
var allChats

function sendVerEmail(){
    fetch('/services/sendvemail', {
        method: 'GET'
    })
        .then(response => response.text())
        .then(data => {
            console.log(data)
            document.getElementById('loadingAll').classList.add('hideElement')
            if (data == "LICSE_SUCCESS"){
                notifArea('SUCCESS', 'Email de verificação enviado com êxito!<br><br> + Após verificar, saia da sessão e entre nela novamente.')
            }else{
                notifArea('ERROR', 'O Email de verificação não pode ser enviado por questões de segurança.<br><br> + Tente sair da sessão e entrar nela novamente.')
            }
            
        })
        .catch(error => {
            console.log(error)
            document.getElementById('loadingAll').classList.add('hideElement')
            notifArea('ERROR', 'O Email de verificação não pode ser enviado.<br><br> + Talvez nossos servidores estejam cansados...')
        });
    
}

function deleteAc(){
    fetch('/services/deleteac', {
        method: 'DELETE'
    })
        .then(response => response.text())
        .then(data => {
            console.log(data)
            document.getElementById('loadingAll').classList.add('hideElement')
            if (data == "LICSE_SUCCESS"){
                notifArea('SUCCESS', 'Conta totalmente excluida com êxito!<br><br> + Você agora não tem mais acesso a essa conta, saia da sessão.')
            }else{
                notifArea('ERROR', 'Ocorreu alguma falha ao excluir sua conta<br><br> + Tente sair da sessão e entrar nela novamente, caso não seja possivel entrar novamente, sua conta foi parcialmente removida.')
            }
            
        })
        .catch(error => {
            console.log(error)
            document.getElementById('loadingAll').classList.add('hideElement')
            notifArea('ERROR', 'Não foi possível completar a ação de exclusão da conta...<br><br> + Talvez nossos servidores estejam cansados...')
        });
    
}



function getSessionChats(){
    fetch('/services/getchats', {
        method: 'GET'
    })
        .then(response => response.json())
        .then(data => {
            notifArea('SUCCESS', 'Conversas carregadas com êxito!')
            document.getElementById('loadingAll').classList.add('hideElement');
            allChats = data
            userShowCuChat(curChat)
            loadCurrentChatInView();
        })
        .catch(error => {
            console.log(error)
            notifArea('ERROR', 'Não foi possivel carregar o conteúdo das conversas...')
            document.getElementById('loadingAll').classList.add('hideElement');
        });
}

function userShowCuChat(chatId){
    document.getElementById('chatTitle').innerHTML = allChats[chatId]['chatTitle']
}

function selectChatSession(ChatId){
    fetch('/services/curchat?chatId=' + ChatId, {
        method: 'GET'
    })
        .then(response => response.text())
        .then(data => {
            var chaves = Object.keys(allChats);
            if (data != "OK"){
                notifArea('ERROR', 'Ocorreu alguma falha ao selecionar a conversa na sessão<br><br> + Tente sair da sessão e entrar nela novamente.')
            }
            
        })
        .catch(error => {
            console.log(error)
            notifArea('ERROR', 'Não foi possível completar a ação...<br><br> + Talvez nossos servidores estejam cansados...')
        });
    
}

function deleteChat(prChatId){
    fetch('/services/deletechat?chatId=' + prChatId, {
        method: 'DELETE'
    })
        .then(response => response.text())
        .then(data => {
            console.log(data)
            document.getElementById('loadingAll').classList.add('hideElement')
            if (data == "LICSE_SUCCESS"){
                notifArea('SUCCESS', 'Sucesso ao excluir este chat!')
                let chatBt = document.getElementById(prChatId)
                console.log(prChatId)
                chatBt.parentNode.removeChild(chatBt);

                delete allChats[prChatId]

                var last = getLastAvailableChat()
                curChat = last[1]
                
                selectChatSession(curChat);
                userShowCuChat(curChat);
                if (curChat != '1'){
                    selectedBtChat('bt_' + curChat);
                }
                
            }else{
                notifArea('ERROR', 'Ocorreu alguma falha ao excluir este chat<br><br> + Tente sair da sessão e entrar nela novamente.')
            }
            
        })
        .catch(error => {
            console.log(error)
            document.getElementById('loadingAll').classList.add('hideElement')
            notifArea('ERROR', 'Não foi possível completar a ação...<br><br> + Talvez nossos servidores estejam cansados...')
        });
    
}

function getLastAvailableChat() {
    var current
    var chaves = Object.keys(allChats);
    if (chaves.length > 0) {
        current = allChats[chaves[0]];
    } else {
        chaves = ['1']

        current = {
            'chatTitle':'Bem-vindo! Inicie uma nova conversa para começar!',
            'messages':{}
        };

        allChats = {'1': current} 
    }
    return [current, chaves[0]]
}


function getResponse(prompt, pType="WEB"){
    if (pType != "NOTE"){
        fetch('/services/licseprompt?prompt=' + prompt + "&type=" + pType, {
            method: 'GET'
        })
            .then(response => response.json())
            .then(data => {
                
                if ('licse' in data){
                    console.log(data)
    
                    addMessage(asSender=false, message=data['licse'])
    
                    document.getElementById("promptText").value = ""
                    document.getElementById("promptText").disabled = false
                    document.getElementById("sendPromptBt").disabled = false
                    document.getElementById("sendPromptBt").classList.remove("hideElement")
                    document.getElementById("wtngSpin").classList.add("hideElement")
                    document.getElementById("promptText").focus()
                    
                    clearTimeout(timeoutSig)
                }else{
                    addMessage(asSender=false, "<i class=\"fa-solid fa-circle-exclamation\"></i> Ocorreu um erro... Tente atualizar a página...", onlyload= true)
                }
                
            })
            .catch(error => {
                console.log(error)
                notifArea('ERROR', 'Não foi possível completar a ação...<br><br> + Talvez nossos servidores estejam cansados...')
            });
            
            if(pType == "WEB"){
                addMessage(asSender=false, "<i class=\"fa-solid fa-globe\"></i> Pesquisando na web...", onlyload= true)
            }
    }
 
}

function saveMsg(prChatId, msg, sender){
    document.getElementById('cloudStatus').innerHTML = "Salvando na nuvem <span class=\"loadingSpinMini\"></span>"
    fetch('/services/addmsg?chatId=' + prChatId + "&msg=" + msg + "&sender=" + sender, {
        method: 'POST'
    })
        .then(response => response.text())
        .then(data => {
            console.log(data)
            document.getElementById('loadingAll').classList.add('hideElement')
            if (data == "LICSE_SUCCESS"){
                document.getElementById('cloudStatus').innerHTML = "Salvo <i class=\"fa-solid fa-cloud\"></i>"
            }else{
                document.getElementById('cloudStatus').innerHTML = "Off <i class=\"fa-solid fa-bug\"></i>"
                notifArea('ERROR', 'Ocorreu uma falha ao salvar mensagem<br><br> + Tente sair da sessão e entrar nela novamente.')
            }
            
        })
        .catch(error => {
            console.log(error)
            document.getElementById('loadingAll').classList.add('hideElement')
            document.getElementById('cloudStatus').innerHTML = "Off <i class=\"fa-solid fa-bug\"></i>"
            notifArea('ERROR', 'Não foi possível completar a ação...<br><br> + Talvez nossos servidores estejam cansados...')
        });
    
}
