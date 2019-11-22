s --> sn(NUMERO, _, ANIMA), sv(NUMERO, ANIMA).

sn(NUMERO, GENERO, ANIMA) --> art(NUMERO, GENERO), nome(NUMERO, GENERO, ANIMA).
sv(NUMERO, ANIMA) --> verbo(NUMERO, ANIMA).

nome(sing, masc, anim) --> [fabio] | [fernando] | [menino] | [garoto].
nome(sing, fem, anim) --> [ana] | [joana] | [beatriz] | [menina].
nome(sing, fem, inanim) --> [bola].

verbo(sing, anim) --> [corre] | [morre] | [anda] | [pula].
verbo(sing, inanim) --> [corre] | [anda] | [pula].

art(sing, masc) --> [o] | [um].
art(sing, fem) --> [a] | [uma].