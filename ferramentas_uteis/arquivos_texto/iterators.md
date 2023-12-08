# Iterator

## O que é

Iterators, são as ferramentas responsáveis por iterar a respeito de elementos de um objeto. Os iterators, são responsáveis apenas por "saber" o próximo valor daquilo que ele está iterando sobre. Iterators fornecem uma maneira de acessar sequencialmente os elementos de um objeto agregado sem expor sua representação subjacente. Para algo ser iterável, deve possuir os métodos '__iter__' e '__next__'.

## Como implementar um iterator

Dentre as formas mais simples e usuais de implementar iterators, é usando loops 'for', que nada mais nada menos que usam os métodos iter dos dados os quais são entregues a ele. Contudo, existem outras formas, como por exemplo, usando os métodos das classes em si, usando __iter__ ou até mesmo a função iter().