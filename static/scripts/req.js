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


