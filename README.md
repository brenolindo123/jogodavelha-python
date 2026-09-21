# Jogo da Velha em Python

Este guia ensina, passo a passo, como preparar o computador e executar um jogo da velha feito em Python.

## 1. Verifique se o Python já está instalado

### Windows

1. Abra o **Prompt de Comando**:
   - Pressione `Windows + R`.
   - Digite `cmd` e pressione `Enter`.
2. Execute um destes comandos:

```bash
python --version
```

ou:

```bash
py --version
```

Se aparecer algo parecido com `Python 3.12.0`, o Python já está instalado. Anote o comando que funcionou (`python` ou `py`), pois ele será usado mais adiante.

### Linux e macOS

1. Abra o aplicativo **Terminal**.
2. Execute:

```bash
python3 --version
```

Se aparecer a versão do Python, ele já está instalado.

## 2. Instale o Python, se necessário

Baixe o Python somente pelo site oficial: [python.org/downloads](https://www.python.org/downloads/).

### Windows

1. Entre em [python.org/downloads](https://www.python.org/downloads/).
2. Clique em **Download Python 3**.
3. Abra o instalador baixado.
4. **Muito importante:** antes de clicar em `Install Now`, marque a opção **Add python.exe to PATH**.
5. Aguarde a instalação terminar.
6. Feche e abra o Prompt de Comando novamente.
7. Confira a instalação com:

```bash
python --version
```

### macOS ou Linux

Siga as instruções disponíveis no site oficial ou no gerenciador de pacotes da sua distribuição. Depois, confirme a instalação com:

```bash
python3 --version
```

## 3. Baixe os arquivos do jogo

### Opção A: baixar pelo navegador

1. Abra a página do projeto: <https://github.com/brenolindo123/jogodavelha-python>.
2. Clique no botão verde **Code**.
3. Clique em **Download ZIP**.
4. Abra a pasta onde o arquivo `.zip` foi baixado.
5. Clique com o botão direito no arquivo e escolha **Extrair tudo** (Windows) ou extraia-o usando a ferramenta disponível no seu sistema.
6. Entre na pasta extraída.

Dentro dela, deve existir um arquivo Python com extensão `.py`, como `jogo_da_velha.py`.

### Opção B: baixar usando Git

Se o Git estiver instalado, abra o Terminal ou Prompt de Comando e execute:

```bash
git clone https://github.com/brenolindo123/jogodavelha-python.git
cd jogodavelha-python
```

## 4. Abra o Terminal na pasta do projeto

É necessário executar o jogo dentro da pasta que contém o arquivo `.py`.

### Windows

Uma forma simples é abrir a pasta no Explorador de Arquivos, clicar na barra de endereço, digitar `cmd` e pressionar `Enter`. O Prompt de Comando será aberto já na pasta correta.

Outra opção é usar `cd`. Exemplo:

```bash
cd C:\Users\SeuNome\Downloads\jogodavelha-python-main
```

### macOS e Linux

No Terminal, use `cd` para entrar na pasta. Exemplo:

```bash
cd ~/Downloads/jogodavelha-python
```

Para conferir os arquivos da pasta, use:

- Windows: `dir`
- macOS/Linux: `ls`

## 5. Execute o jogo

Substitua `jogo_da_velha.py` pelo nome exato do arquivo Python que estiver na pasta.

### Windows

Se o comando `python` funcionou na verificação:

```bash
python jogo_da_velha.py
```

Se você usa o inicializador do Windows:

```bash
py jogo_da_velha.py
```

### macOS e Linux

```bash
python3 jogo_da_velha.py
```

O jogo será iniciado no próprio Terminal. Leia as instruções exibidas na tela e digite a posição escolhida quando for a sua vez.

## 6. Como jogar

Em geral, o jogo da velha funciona assim:

1. Dois jogadores alternam as jogadas.
2. Um jogador usa `X` e o outro usa `O`.
3. Cada jogador escolhe uma casa vazia do tabuleiro.
4. Vence quem formar primeiro uma linha com três símbolos iguais:
   - na horizontal;
   - na vertical; ou
   - na diagonal.
5. Se todas as casas forem preenchidas sem formar uma linha, ocorre empate.

Siga exatamente o formato solicitado pelo programa. Por exemplo, se ele pedir um número de `1` a `9`, digite apenas o número correspondente à casa desejada.

## 7. Funcionamento do sistema

O sistema exibe o tabuleiro do jogo no Terminal e alterna a vez entre os dois jogadores. A cada rodada, o jogador atual informa a posição onde deseja colocar seu símbolo (`X` ou `O`). O programa verifica se a posição escolhida está disponível, atualiza o tabuleiro e confere se houve uma vitória ou empate. O jogo continua até que um jogador forme uma linha com três símbolos iguais ou todas as casas sejam preenchidas.

## 8. Problemas comuns

### “python não é reconhecido como um comando”

No Windows, o Python provavelmente não foi adicionado ao `PATH`. Reinstale o Python e marque **Add python.exe to PATH**. Depois, abra um novo Prompt de Comando.

Também tente:

```bash
py --version
```

### “python3: command not found”

O Python 3 não está instalado ou não está disponível no `PATH`. Instale-o pelo site oficial e abra um novo Terminal.

### “No such file or directory” ou “can't open file”

Você provavelmente está na pasta errada ou digitou o nome do arquivo incorretamente. Use `dir` ou `ls` para listar os arquivos e copie o nome exato do arquivo `.py` no comando.

### O arquivo abre e fecha rapidamente

Execute-o pelo Terminal, em vez de clicar duas vezes nele. Assim, você conseguirá ver as mensagens e possíveis erros do programa.

## 9. Parar o jogo

Para interromper o programa a qualquer momento, pressione:

```text
Ctrl + C
```

Bom jogo!

## Informações do projeto

- **Nome do projeto:** Jogo da Velha
- **Integrantes:** Breno e Crysthofer
- **Objetivo do sistema:** Jogo para passar o tempo e se divertir
- **Tema:** Animais

colaborador: @LeandroMontanari/jogo-da-velha-python3
