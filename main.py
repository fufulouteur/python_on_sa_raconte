adjectif1 = input('saisar un adjectif: ').lower()
jeu = input("sasir le nom d'un jeu de plage: ").lower()
adjectif2 = input('un autre adjectif: ').lower()
ami = input("le prenom d'un ami: ").capitalize()
verbe = input("un verbe d'action: ").lower()
adjectif3 = input("un autre adjectif: ").lower()


histoire = (f"en ce jour d'ete sur la plage {adjectif1}, mes \
ami et moi etions dans l'eau a jouer au  {jeu}.\n \
soudain, une vague {adjectif2} arriva et mon pote {ami} a \
crie, \"attention, une meduse {verbe}  !\" \
{ami} a couru se refugier  sur la plage. \n \
Il avait tres peur des meduse qui {verbe}. les autre \
sont reste a jouer au {jeu}. les meduses qui {verbe} sont \
{adjectif3}.\n ")

print(histoire)