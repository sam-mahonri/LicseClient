function sendVerEmail(selfBt){
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
