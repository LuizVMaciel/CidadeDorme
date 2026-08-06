const textoPrincipal = document.getElementById('textoPrincipal');
const textoSecundario = document.getElementById('textoSecundario');
const paragrafo = document.getElementById('paragrafo');
const entrada = document.getElementById('entrada');
const botaoAdicionarRemover = document.getElementById('botaoAdicionar')
const botao = document.getElementById('botao');
const botaoVerJogadores = document.getElementById('botaoVerJogadores')
const botaoVoltar = document.getElementById('botaoVoltar')

let processo = 0;
let jogadores = []
let telaVerJogadores = false

//função para tela inicial
function telaInicial(){
    botao.style.visibility = 'visible'
    botaoAdicionarRemover.style.display = 'none'
    textoPrincipal.textContent = 'Bem vindo à cidade!'
    textoSecundario.textContent = 'Aperte o botão para jogar'
    botao.textContent = 'Jogar'
    paragrafo.textContent = ''
    entrada.value = ''
    entrada.style.visibility = 'hidden'
    botaoVerJogadores.style.visibility = 'hidden'
    botaoVoltar.style.visibility = 'hidden'
}

//função para tela de registro de jogadores para partida
function telaAdicionarJogadores(){
    function adicionarJogador(){
        let valorEntrada = entrada.value;
        if (valorEntrada != ''){
            if(jogadores.includes(valorEntrada) == false){
                jogadores.push(valorEntrada)
                console.log(jogadores)
                entrada.value = ''
                paragrafo.textContent = 'Jogador adicionado'
            }
            else{
                paragrafo.textContent = 'Jogador já registrado'
            }
        }
        else{
            paragrafo.textContent = 'Nome inválido'
        }
    }
    botao.style.visibility = 'visible'
    paragrafo.textContent = ''
    textoPrincipal.textContent = 'Jogadores'
    textoSecundario.textContent = 'Adicione os jogadores, um de cada vez.'
    entrada.style.visibility = 'visible'
    botaoAdicionarRemover.style.display = 'block'
    botaoAdicionarRemover.textContent = 'Adicionar'
    botaoAdicionarRemover.onclick = adicionarJogador
    botao.textContent = 'Começar'
    botaoVerJogadores.style.visibility = 'visible'
    botaoVoltar.style.visibility = 'visible'
}

function verJogadoresRegistrados(){
    function removerJogador(){
        let valorEntrada = entrada.value;
        if (valorEntrada != ''){
            if(jogadores.includes(valorEntrada) == true){
                let indiceJogador = jogadores.indexOf(valorEntrada)
                jogadores.splice(indiceJogador, 1)
                console.log(jogadores)
                entrada.value = ''
                paragrafo.textContent = 'Jogador removido'
                textoSecundario.textContent = ''
                for(i = 0; i < jogadores.length; i++){
                    textoSecundario.textContent += `${jogadores[i]},\n`
                }
            }
            else{
                paragrafo.textContent = 'Jogador nao registrado'
            }
        }
        else{
            paragrafo.textContent = 'Nome inválido'
        }
    }
    textoSecundario.textContent = ''
    paragrafo.textContent = ''
    textoPrincipal.textContent = 'Jogadores'
    botao.style.visibility = 'hidden'
    botaoAdicionarRemover.textContent = 'remover'
    botaoAdicionarRemover.onclick = removerJogador
    for(i = 0; i < jogadores.length; i++){
        textoSecundario.textContent += `${jogadores[i]},\n`
    }
}

//chama as funções de cada tela
function processos(){
    if(telaVerJogadores == true){
        verJogadoresRegistrados()
    }
    else if(processo == 0){
        telaInicial();
    }
    else if(processo == 1){
        telaAdicionarJogadores();
    }
}

//define qual tela será chamada
function trocarTela(){
    if(processo == 0){
        processo = 1
    }
    else if(processo == 1){
        processo = 0
    }
    processos()
}

//execução
botao.onclick = trocarTela
botaoVerJogadores.onclick = function(){
    telaVerJogadores = true
    processos()
}
botaoVoltar.onclick = function(){
    if(telaVerJogadores == true){
        telaVerJogadores = false
    }
    else{
        processo--
    }
    processos()
}
processos()