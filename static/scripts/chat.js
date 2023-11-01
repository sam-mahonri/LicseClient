var timeoutSig
var idMsg
var pType = "WEB"
var limitTime = 10000

function processarPrompt(event) {
    event.preventDefault();

    const prompt = document.getElementById("promptText").value;

    

    console.log("Prompt", prompt);
    document.getElementById("promptText").disabled = true
    document.getElementById("sendPromptBt").disabled = true
    document.getElementById("promptText").value = "Aguardando resposta..."
    document.getElementById("sendPromptBt").classList.add("hideElement")
    document.getElementById("wtngSpin").classList.remove("hideElement")
    addMessage(true, prompt)
    timeoutSig = setTimeout(() => {
        document.getElementById("promptText").value = ""
        document.getElementById("promptText").disabled = false
        document.getElementById("sendPromptBt").disabled = false
        document.getElementById("sendPromptBt").classList.remove("hideElement")
        document.getElementById("wtngSpin").classList.add("hideElement")
        document.getElementById("promptText").focus()
    }, limitTime);

    getResponse(prompt, pType)
}

var msgId = 0

function addMessage(asSender=true, message, onlyload=false){
    msgArea = document.getElementById('messageArea')

    var novaDiv = document.createElement("div");
    novaDiv.id = 'messageId_' + String(idMsg)
    var novoSpan = document.createElement("span");
    novoSpan.innerHTML = '<p>' + message.replace("\n", "<br>"); + '</p>';
    idMsg++;
    novaDiv.appendChild(novoSpan);
    var sender = ''

    if (asSender){
        sender = 'you'
        novaDiv.className = "senderMessage";
    }else{
        sender = 'licse'
        novaDiv.className = "licseMessage";
    }

    novaDiv.classList.add('fadeIn')

    msgArea.appendChild(novaDiv);
    
    console.log(String(msgId));

    if(!onlyload){
        if (!allChats[curChat]['messages']) {
            allChats[curChat]['messages'] = {};
        }
          
    
        allChats[curChat]['messages'][String(msgId)] = {
            'sender':sender,
            'message':message,
            'timestamp':''
        }

        saveMsg(curChat, message, sender)
    }

    msgId++;
    msgArea.parentNode.scrollTop = msgArea.parentNode.scrollHeight;
}

function loadCurrentChatInView(){
    console.log(allChats[curChat]['messages'])
    msgId = 0
    if ('messages' in allChats[curChat]){
        document.getElementById('messageArea').innerHTML = '';
        addMessage(asSender=false, message='Este é o inicio desta conversa!', onlyload=true);
        for (var msg of Object.values(allChats[curChat]['messages'])){
            if (msg['sender'] == 'you'){
                
                addMessage(asSender=true, message=msg['message'], onlyload=true)
            }else{
                addMessage(asSender=false, message=msg['message'], onlyload=true)
            }
        }
    }else{
        document.getElementById('messageArea').innerHTML = '';
        addMessage(asSender=false, message='Envie alguma mensagem!', onlyload=true);
    }
    

}

function setFuncType(typeFunc){
    pType = typeFunc
    if (pType == "SUMMARIZE"){
        limitTime = 10000
        addMessage(asSender=false, message='Olá! Agora estou no modo de resumo, envie qualquer texto no prompt que eu tentarei sumarizar com IA 😊🐶');
    } else if (pType == "WEB"){
        limitTime = 10000
        addMessage(asSender=false, message='Agora serei capaz de pesquisar na internet, eu, Licse, irei obter palavras chaves da sua pergunta, buscarei por artigos e, por fim, vou resumí-los para você! 🤓🐕');
    } else if (pType == "NOTE"){
        limitTime = 300
        addMessage(asSender=false, message='Escreva o que quiser, não irei mais responder, vou apenas salvar suas anotações, bons estudos! 🤓🐶😊💭');
    }
}