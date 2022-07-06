# AgentBreakout 


###  Implementação de uma solução de aprendizagem por reforço para o jogo Breakout do Atari.

## Descrição

A dinâmica, você move uma raquete e bate a bola em uma parede de tijolos no topo da tela. Seu objetivo é destruir a parede de tijolos. Você pode tentar quebrar a parede e deixar a bola causar estragos do outro lado, tudo por conta própria! Você tem cinco vidas.

## Dados 

<table border="1">
<tr>
  <td>Espaço de Açãos</td>
  <td>Discreto(18)</td>
<tr>
  <tr>
  <td>Espaço de Observação</td>
  <td>(210, 160, 3)</td>
<tr>
  <tr>
  <tr>
  <td>Observação Alta</td>
  <td>255</td>
<tr>
  <tr>
  <tr>
  <td>Observação Baixa</td>
  <td>0</td>
<tr>
</table>

## Ações 

<table border="1">
<tr>
  <td>2</td>
  <td>Mover Direita</td>
<tr>
  <tr>
  <td>3</td>
  <td>Mover Direita</td>
</table>

## Recompensas

Você marca pontos destruindo tijolos na parede. A recompensa por destruir um tijolo depende da cor do tijolo.

## Treinar Agente 

```bash
Execute o arquivo em src 'train.py' 
``` 

## Executar um Agente já treinado 

```bash
Execute o arquivo em src 'agentTest.py' 
É preciso especificar  o caminho do agente treinado na variável 'a2c_path'
``` 
## Dependências

Será necessário :

- [Gym](https://www.gymlibrary.ml/) 
- [Stable-baselines3](https://stable-baselines3.readthedocs.io/en/master/) 
- [Tensorboard](https://www.tensorflow.org/tensorboard/get_started) 

Pode importar facilmente esssas dependências atraves do [Anaconda-navigator](https://anaconda.org/anaconda/anaconda-navigator)

```bash
Import no anaconda o arquivo 'agentBreakout.yaml' localizado na pasta ambienteAnaconda
``` 

## Relatórios com tensorboard
Na pasta logs execute o comando 
```bash
tensorboard --logdir=.
``` 
```bash
TensorBoard 2.9.1 at http://localhost:6006/ (Press CTRL+C to quit)
``` 

## Tecnologias 
```bash
Python 
Anaconda-navigator 
Gym 
Stable-baselines3
Tensorboard
```