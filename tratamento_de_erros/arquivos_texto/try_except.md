# Try Except

## O que é

É uma forma de tratar exceções dentro do python. Isso é possível, pois assim que algo da errado dentro de um bloco try, ele cai diretamente no except, levantando alguma exceção específica (levantar a exceção não é obrigatório, mas é considerado uma boa prática de programação). O try é extremamente útil para tratamento de erros, porém, diferentemente de um if, for ou while, tem a função de simplesmente rodar o código contido em seu escopo e testar seu funcionamento. Caso não funcione, o try é quebrado e entra no except, onde será tratada a exceção.

## Como implementar

A implementação de um bloco try é similar à de outros blocos de código, como if e for. Contudo, nada é declarado a seguir da chamada do try, sendo colocado o código apenas dentro de seu escopo. O except sim recebe o código logo em seguida de sua chamada, onde será passado o possível erro levantado pelo try.

## Finally e Else

Ao final de um bloco try-except, é possível a inserção de um bloco finally, que vai receber um código que sempre é executado. O else, assim como o presente no if, pode ser usado para executar um código caso o if tenha dado certo.
