% Ele notou ligações químicas entre vários materiais híbridos.
% Eles notaram ligações químicas entre vários materiais híbridos.
% Ela notou ligações químicas entre vários materiais híbridos.
% Elas notaram ligações químicas entre vários materiais híbridos.

s --> noun_phrase(_GENDER, NUM), verb_phrase(NUM).
noun_phrase(GENDER, NUM) --> pron(GENDER, NUM).
verb_phrase(NUM) --> verb(NUM), obj_phrase, adv, compl_phrase.
obj_phrase --> obj_noun, obj_adj.
compl_phrase --> quantif, compl_noun, compl_adj.

pron(masc, sing) --> [ele].
pron(masc, plur) --> [eles].
pron(fem, sing) --> [ela].
pron(fem, plur) --> [elas].

verb(sing) --> [notou].
verb(plur) --> [notaram].

obj_noun --> [ligacoes].
obj_adj --> [quimicas].

adv --> [entre].

quantif --> [varios].
compl_noun --> [materiais].
compl_adj --> [hibridos].