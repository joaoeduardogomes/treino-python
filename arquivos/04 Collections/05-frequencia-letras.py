# Analisar a frequência com que cada caractere aparece.

from collections import Counter

def conta_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    for caractere, proporcao in proporcoes.items():
        print(f"{caractere} => {proporcao * 100:.2f}%")

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f"{caractere} => {proporcao * 100:.2f}%")

texto1 = """
Embora ciente de que esteja atrasado, venho compartilhar uma lista com meus dez jogos favoritos da última década. Para montá-la, levei em conta os títulos lançados entre os anos 2011 e 2020 e que, é claro, eu tenha jogado até o final. Peço desculpas pela demora, mas, para mim, não foi nada fácil eleger dez entre tantos jogos incríveis que experienciei nesse período. Apesar disso, sinto que era importante para mim poder fazer essa seleção.

Imagino que para alguns seja quase uma ofensa eu não ter citado alguns de seus jogos favoritos lançados entre esse intervalo de anos. Porém, venho lembrar que esta lista transmite apenas meu gosto pessoal, portanto, ela não é uma ferramenta para desmerecer seus tão queridos jogos.

Outra informação importante é que essa lista não está em ordem de preferência, pois para mim essa seria uma tarefa ainda mais difícil. Apenas listei os jogos que escolhi depois de pensar bastante, pois cada um deles me é precioso por razões diferentes. Dessa forma, meu critério de listagem foi meramente o ano de lançamento de cada título.

Abaixo estão os nomes dos jogos escolhidos com o ano de lançamento ao lado. Abaixo dessas informações discorro brevemente sobre por que ele me cativou. Não vou me estender muito nessa parte porque este texto não é uma resenha e porque não quero torná-lo demasiadamente enfadonho.


Seguem os escolhidos:

1. Heavy Rain (2011)
A temática de detetive, investigação e mistério sempre me atraiu. Tanto em filmes e séries como também nos jogos, fossem eles de tabuleiro ou eletrônicos.

Heavy Rain me trouxe uma experiência que gradualmente se tornava mais interessante e intrigante. Quanto mais jogava, mais queria saber onde aquilo ia chegar.

A dinâmica de alternar entre quatro protagonistas foi uma experiência que nunca tive de maneira tão bem elaborada. A história me lembrou muito filmes como Seven (1995) e Saw (2004); e o ponto de virada no último ato do jogo me pegou de surpresa, embora eu tivesse escolhido ignorar certas pistas por achar que era coisa da minha cabeça. Por ter múltiplos finais, o jogo também tem um bom fator de rejogabilidade. Algo que aprecio bastante.

2. The Last of Us (2013)
Com certeza foi o jogo que mais me surpreendeu. Não esperava nada dele e acabei entrando em uma aventura muito emocionante e que me fez sentir cúmplice de algumas escolhas do protagonista, uma vez que eu tinha o controle em mãos.

The Last of Us me representou com excelência diversas variantes do comportamento humano. Entre elas o egoísmo, o perdão e o carinho. É difícil se desprender de um jogo desses. Se o jogador for dotado de pelo menos um pouco de sensibilidade, carregará essa história e esses personagens consigo para sempre.

3. Pokémon Y (2013)
Foi difícil escolher entre Pokémon White e Pokémon Y. Embora o primeiro tenha, na minha opinião, o melhor roteiro de toda a série — o que, em se tratando de Pokémon, basta ter um roteiro —, o segundo trouxe diversas mudanças na fórmula que me foram muito bem recebidas. Entre elas a possibilidade de personalizar seu personagem; o Exp. Share compartilhado com todo o time, o que permite uma progressão mais homogênea; movimentação 360º do personagem, enquanto que antes só podíamos andar em quatro direções; modelos 3D dos monstrinhos; batalhas exclusivamente com Pokémon voadores; um grupo de amigos; a possibilidade de ter um apelido desses amigos; a maneira como a câmera muda ao se entrar em uma caverna; e até a possibilidade de um novo transporte, os patins. Muitas dessas mudanças, inclusive, abandonadas nos jogos seguintes.

Em se tratando do Exp. Share, foi uma ótima mudança. Até o Pokémon White, só podíamos compartilhar a experiência ganha com um outro Pokémon, o que, para mim, dava a sensação de que o treinamento levava mais tempo. E hoje não temos tanto tempo para dedicar ao fortalecimento de nossos monstrinhos de maneira tão individual; seja por não termos tempo por estarmos ocupados com outras tarefas — como estudar, trabalhar, dentre outras responsabilidades — quanto por vivermos em uma época que muitos conteúdos de entretenimento competem por nossa atenção. É mais animador saber que nossa equipe vai progredir de maneira melhor equilibrada e que não vamos ter de repetir o mesmo grinding que fizemos em praticamente todos os títulos anteriores da série.

E também acho esse jogo bastante injustiçado. Muitos desgostam dele e o condenam como sendo “muito fácil”. Mas, convenhamos, dificuldade nunca foi uma marca da franquia.

4. GTA V (2013)
Embora alguns fãs da série o achem muito fraco, achei o mais envolvente de todos os títulos. Antes do lançamento, vi muitas pessoas se questionando se o uso de três protagonistas iria funcionar. Para mim, todos eles são excelentes à sua própria maneira, e achei uma mudança incrível. Principalmente quando estamos em missão e podemos alternar entre eles para realizar tarefas diferentes e termos um outro ponto de vista dos acontecimentos — a exemplo de quando controlamos o Franklin com uma sniper, enquanto que Michael está em um navio enfrentando inimigos mais de perto.

O jogo é bastante cinematográfico, especialmente pelo final. As interpretações de todos, inclusive dos coadjuvantes, foi muito boa. Realmente me importava com cada um deles.

E também devo destacar que a física dos veículos no jogo é até hoje referência. Desde seu lançamento, sempre que um jogo do estilo é lançado o público não pode deixar de comparar a física dos veículos com a de GTA V. A física dos personagens, no entanto, deixou a desejar para mim. Achei a movimentação deles pouco natural, especialmente os figurantes na rua.

5. The Witcher 3 (2015)
Uma das maiores representações do RPG de mesa que já experimentei. Tanto pelo estilo quanto pela temática.

O jogo é envolvente, com personagens carismáticos e dá uma aula de como produzir história e narrativa. As missões secundárias do jogo são quase que obrigatórias para se te ruma experiência completa jornada de Geralt.

Embora seja um jogo longo, os múltiplos caminhos que podemos tomar na história aumenta o fator de rejogabilidade. Dá vontade de explorar outras opções de diálogos e tentar dar uma personalidade diferente ao protagonista. O meu, por exemplo, era piedoso e heroico. Sempre tratando bem as pessoas. Tenho curiosidade de fazer uma segunda run com um Geralt mais impiedoso.

E a DLC Blood and Wine, para mim, dá um final perfeito para o jogo. Muito melhor do que o que vemos no jogo base.

6. Life is Strange (2015)
Outro jogo que adquiri sem esperar nada. Experimentei por recomendação de uma colega de faculdade, joguei aquele começo e achei bem mais ou menos. Mas, conforme progredia na história, ficava cada vez mais envolvido em estar na pele da protagonista, Max, e em me relacionar com as pessoas daquela diegese.

Jogo envolvente, mecânicas muito interessantes de manipulação do tempo, personagens memoráveis, múltiplas opções de diálogos e de relações com os NPCs. Tudo isso misturado a uma trilha sonora impecável, arte belíssima e narrativa emocionante.

7. Firewatch (2016)
Confesso que no momento em que vi a intro de Firewatch em uma gameplay no YouTube eu soube queria esse jogo. Comprei ele e embarquei na tocante história de Henry como guarda florestal.

Suas motivações para estar ali, sua maneira de agir e reagir, o ambiente em volta — tudo monta uma belíssima imersão naquele momento. Naquele espaço em que ele está vivendo.

Os diálogos do jogo são um prato cheio. De longe a parte mais rica para mim. A arte também é muito bonita. E confesso que em alguns momentos fiquei aflito e tenso, especialmente com um acontecimento próximo ao final do jogo.

8. What Remains of Edith Finch (2017)
Jogo simples que, visualmente, lembra um pouco a arte de Firewatch. A trama é intrigante, nos colocando no papel de diversos personagens em suas respectivas mini-histórias narradas pela protagonista.

Alguns momentos do jogo contam com elementos narrativos extremamente narrativos, como um em que jogamos entre os frames de uma história em quadrinhos, ou outro que vemos pela perspectiva de uma câmera fotográfica. Ainda há um momento em que vemos o desenrolar dos eventos através de desenhos em um bloco de notas.

Quanto mais a protagonista nos conta as histórias dos personagens, mais curiosos ficamos. O final também conta com um ponto de virada bastante criativo.

9. The Legend of Zelda: Breath of the Wild (2017)
Admito que essa foi minha primeira experiência com a série Zelda que joguei até o final. Outros títulos da série não me cativaram a ponto de me manterem interessado.

Particularmente, não gosto muito de jogos de mundo aberto, mas acredito que o mundo aberto é justamente o ponto alto deste título. Ele nos coloca numa aventura em que a narrativa é a própria jornada, e não uma série de eventos/cutscenes/falações, como acontece tradicionalmente.

Breath of the Wild é um jogo simples, mas que cumpre com excelência todos os conteúdos do jogo. Desde a movimentação do personagem até a interação com o ambiente e os inimigos. Claro que ele fica atrás na questão complexidade em alguns aspectos, mas isso compensa com uma maestria de construção de mundo, trilha sonora, efeitos sonoros e diversos “mistérios” no mapa que nos deixam cada vez mais curiosos em explorar.

10. Persona 5 (2017)
Este foi o jogo que me fez morder a língua. Isso porque nunca fui muito interessado por jogos em que o combate se dá por turnos. Ainda hoje fico entediado pela sensação de repetição que esse modelo me traz. Pokémon sempre foi a única exceção, mas especialmente pelo fator da coleção dos monstrinhos.

Decidi experimentar Persona 5 e fui surpreendido. Uma narrativa riquíssima, profunda e tratando com uma mistura de delicadeza e acidez temas bastante polêmicos foram os pontos que mais me chamaram atenção logo de início. Isso somado às partes mais mecânicas como sistema, trilha sonora inesquecível, relacionamentos com os NPC, mecânica de aquisição de habilidades passivas por meio dessas relações etc. E também temos a parte artística, como o próprio design de personagens, arte, cores, interpretação dos personagens, representação dos distritos de Tóquio. Com exceção de algumas questões pontuais, tudo parecia perfeito.

Persona 5 me fez morder a língua não apenas por ter me surpreendido como um dos melhores jogos da década, mas também como uma das melhores histórias em que já me envolvi.


Esta foi minha lista com meus dez jogos favoritos da última década. Não farei menções honrosas pois há realmente muita coisa a ser citada. Se for o caso, posso citar outros títulos que experimentei nesse período e que tem um lugar querido na minha memória.

Novamente digo que, se seus jogos favoritos não estão na lista, não precisa se desesperar. Talvez eu não os tenha jogado ou talvez eu apenas tenha tido uma relação melhor com os jogos que resolvi trazer. Isso não significa de maneira nenhuma que estou diminuindo suas experiências com os títulos que mais lhe agradaram. Inclusive, fica o convite para compartilhá-los conosco nos comentários.
"""


# exibe a frequência de todos os caracteres presentes no texto:
conta_letras(texto1)

# exibe a frequência dos 10 caracteres mais frequentes:
analisa_frequencia_de_letras(texto1)