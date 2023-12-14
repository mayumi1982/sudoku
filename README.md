# Sudoku: Resolução Computacional 
O Sudoku é um quebra-cabeça numérico amplamente conhecido que demanda o preenchimento de espaços em branco em uma grade 9x9 com dígitos de 1 a 9, garantindo que cada coluna, linha e subgrade de 3x3 contenha todos os números de forma única. Diversas abordagens, incluindo técnicas computacionais, foram utilizadas para resolver esse desafio. Neste projeto, serão realizadas as seguintes tarefas:

**Função SolveSudoku()**: Recebe um grid como argumento e retorna verdadeiro se houver uma solução possível, e falso caso contrário. Quando retorna falso, o programa exibirá "Nenhuma solução existe".
**Função printGrid()**: Recebe um grid como argumento e imprime os 81 números do Sudoku resolvido em uma única linha, separados por espaços, sem adicionar um caractere de nova linha após a impressão do grid.

# Estratégia Utilizada

Visualize uma grade composta por nove linhas e nove colunas. Cada célula nessa grade representa um espaço onde é possível inserir um número de 1 a 9. Essa é a premissa do Sudoku. A biblioteca NumPy foi empregada para organizar os números do Sudoku em uma matriz, facilitando a manipulação e resolução do quebra-cabeça.

<img width="428" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/811ee15c-7254-4a96-8ea7-35ed249b6109">

A lógica computacional utilizada é o Backtracking. Esse algoritmo segue uma abordagem de tentativa e erro. Inicialmente, preenche o tabuleiro vazio com números e verifica a validade da inserção. Se a escolha for válida, avança para a próxima célula vazia. Caso contrário, retrocede (backtrack) e tenta outro número na célula anterior.

#### Verificador de Regras:

<img width="431" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/2fff3a81-657d-4e17-99a9-1270a85e6710">

#### Função SolveSudoku:

<img width="442" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/e881c362-8a36-4ec1-ae97-335b21724951">

_Empregando o método backtracking_

#### Função printGrid:

<img width="414" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/946f995c-4b4f-47db-9ee9-bf0a6932e0fd">

_Para formatar a saída adequadamente_

#### Função print:

<img width="261" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/7e4eaeb9-0536-4b00-8979-3b3820e4b42a">


# Resultado

#### Com solução:

<img width="170" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/86f59bf6-649a-4758-a6eb-ec147f465e0b">

Terminal:

<img width="127" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/123bc3df-2379-48b8-a164-601bd401f893">

#### Sem solução: 

<img width="173" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/dce7fcaf-1946-46a9-ba5d-b217b264a747">

Terminal:

<img width="95" alt="image" src="https://github.com/mayumi1982/sudoku/assets/70608757/55737c14-5ff8-4448-86c8-6237c671441f">

Observa-se que o exemplo de uso com um grid com solução aparenta estar correto, enquanto o segundo exemplo (sem solução) possui um valor repetido (6) na segunda coluna da primeira linha, impossibilitando a resolução do Sudoku.


