const textoPrincipal = document.getElementById('textoPrincipal');
const textoSecundario = document.getElementById('textoSecundario');
const paragrafo = document.getElementById('paragrafo');
const entrada = document.getElementById('entrada');
const botaoAdicionar = document.getElementById('botaoAdicionar')
const botao = document.getElementById('botao');

let processo = 0;
let jogadores = []

//função para tela inicial
function telaInicial(){
    botaoAdicionar.style.display = 'none'
    textoPrincipal.textContent = 'Bem vindo à cidade!'
    textoSecundario.textContent = 'Aperte o botão para jogar'
    botao.textContent = 'Jogar'
    paragrafo.textContent = ''
    entrada.value = ''
    entrada.style.visibility = 'hidden'
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
    textoPrincipal.textContent = 'Jogadores'
    textoSecundario.textContent = 'Adicione os jogadores, um de cada vez.'
    entrada.style.visibility = 'visible'
    botaoAdicionar.style.display = 'block'
    botaoAdicionar.textContent = 'Adicionar'
    botaoAdicionar.onclick = adicionarJogador
    botao.textContent = 'Começar'
}

//chama as funções de cada tela
function processos(){
    if(processo == 0){
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
processos()