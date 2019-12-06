% Vários autores têm descrito alterações nas propriedades dos nanocompósitos.
% Várias autoras têm descrito alterações nas propriedades dos nanocompósitos.

s --> noun_phrase(_GENDER), verb_phrase.

noun_phrase(GENDER) --> quantif(GENDER), subj(GENDER).
verb_phrase --> aux, verb, obj_phrase.

quantif(masc) --> [varios].
quantif(fem) --> [varias].
subj(masc) --> [autores].
subj(fem) --> [autoras].

aux --> [tem].
verb --> [descrito].

obj_phrase --> obj, compl_obj, compl_compl.
obj --> [alteracoes].
compl_obj --> obj_prep, obj_noun.
obj_prep --> [nas].
obj_noun --> [propriedades].

compl_compl --> compl_compl_prep, compl_compl_noun.
compl_compl_prep --> [dos].
compl_compl_noun --> [nanocompositos].