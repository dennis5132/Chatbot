import random
from datetime import datetime
# print("hallo")
begroetingen = ["hallo","yo","hoi, hoe gaat het","welkom","goed je te zien", "ben je er weer"]
grapstart = ["nou, hier is er eentje:", "als je de mijn grappen leuk vindt:", "hier gaat dan iets:"]
grappen = ["Twee verliefde tieners zitten op een bankje. Het meisje vraagt aan de jongen: “Wil je zien waar ik aan mijn blindedarm ben geopereerd?” “Ja, graag!”, antwoordt de jongen enthousiast. “Daar, in dat grote gebouw met al die ramen…”",
           "Fred gaat naar de dokter. Hij loopt naar binnen en zegt: “Ik heb een bril nodig.”Waarop de dame achter de balie antwoord: “Inderdaad, want u staat nu in de kaaswinkel…”",
           "Een man komt bij de Chinees. De dame van de bediening komt en vraagt: ‘Wilt u menu?’ De man zegt: ‘Nou nee, liever na het eten.’",
           "Hoe noem je een ijsbeer met oorwarmers? Laat maar. Hij kan je toch niet horen…",
           "Er komt een man bij een garage en zegt: “Ik wil graag twee ruitenwissers voor m’n Lada.” Waarop de garagehouder zegt: “Oké, dat lijkt me een prima deal.”",
           "Jan zegt: “Altijd als ik op reis ga, doe ik de nacht ervoor geen oog dicht…” Waarop zijn vriend zegt: “Waarom ga je dan niet gewoon een dagje eerder?”",
           "Er is een dame in een kledingwinkel en vraagt: ‘Mag ik die jurk in de etalage passen?’ Antwoordt de verkoper: ‘Ja hoor, maar we hebben ook pashokjes hoor!’",
           "Piet gaat op een dag naar de vader van zijn vriendin om hem de hand van zijn dochter te vragen. “Ik dacht het niet!”, zegt de vader nors. “Ik wil niet hebben dat mijn dochter haar leven verknoeit bij zo’n lapzwans!” Waarop Piet antwoordt: “Precies meneer, dat wil ik ook niet. Daarom kom ik nu juist haar hand vragen!”",
           "Een man heeft net een vinger laten amputeren. Hij vraagt aan de dokter: “Kan ik nu piano spelen dokter?’ De dokter antwoord: “Natuurlijk, geen probleem!’ Waarop de man blij zegt: “Wow, dat is geweldig! Dat kon ik voor de operatie niet!”",
           "Er komt een man bij de dokter. Hij zegt: Dokter, kunt u iets doen aan mijn verstopte neus? dokter: “Oké oké, ik help wel zoeken…”",
           "Er komt een man bij de dokter en zegt: ‘Als ik op mijn arm druk doet het zeer, als ik op mijn been druk doet het zeer en als ik op mijn buik druk doet het zeer.’ Waarop de dokter zegt: ‘Ik weet het al; een gebroken vinger!’",
           "Een man zegt tegen zijn vrouw: “Schat, laten we er eens een mooi weekend van maken.” “Wat een leuk idee!”, antwoordt zij. Waarop de man zegt: “Prima, dan zien we elkaar maandag weer!”",
           "Twee dommeriken staan allebei aan een kant van de sloot. Vraagt de ene oen aan de andere: ‘Hoe kom ik aan de overkant?’ Waarop de andere oen antwoordt: “Hoezo? Daar sta je toch al..?”",
           "Gooit een man een brief in de bus. Vraagt de buschauffeur: ‘Wat moet ik hier mee…?’",
           "Een man graaft een groot gat in zijn tuin. Zijn nieuwsgierige buurvrouw vraagt: “Waarom graaft u z’n groot gat in uw tuin, buurman?” De buurman antwoordt: “Om mijn vis te begraven.” “Uw vis? Waarom zo’n groot gat dan?” Waarop de buurman zegt: “Mijn vis is opgegeten door uw kat.”",
           "Weet jij de overeenkomst tussen je billen en de woestijn? Kaktussen…",
           "Een man staat voor de rechter omdat hij zijn vrouw heeft doodgeschoten toen hij haar met een andere man in bed aantrof. De rechter vraagt: “Waarom heeft u eigenlijk uw vrouw doodgeschoten?” Waarop de man antwoordt: “Het leek me beter om één keer mijn vrouw dood te schieten dan iedere week een andere vent…”",
           "Op de A4 Den Haag Amsterdam is een tankwagen met zoutzuur gekanteld. De file is inmiddels opgelost…",
           "Een lange en een korte man staan naast elkaar te plassen in een urinoir. Vraagt de lange aan de korte: “Wat sta je toch de hele tijd met je ogen te knipperen? Ben je nerveus of zo?” “Nee hoor,” zegt die korte, “dat komt omdat jij zo staat te spetteren…”",
           "Twee oudjes zitten op een bankje. Zegt de ene tegen de andere: ‘Ik heb een nieuw gehoorapparaat. Een hele goeie, want ik hoor nu alles weer!’ De andere: ‘Oh wat fijn, en wat kostte die?’ ‘Half vijf!’",
           "“Wat was het een fantastische wedstrijd, scheids!”, zegt de trainer van het verliezende elftal tegen de scheidsrechter. “Jammer dat u niet gekeken heeft!”",
           "De juf vraagt aan Olivia: “Ik ben mooi. Is deze zin tegenwoordige tijd of verleden tijd?” Waarop Olivia antwoordt: “Verleden tijd, juf.”",
           "Er staat een man midden op een kruispunt. Hij vraagt aan een automobilist: “Hoe kom ik het snelst bij het ziekenhuis?’ Deze antwoordt: “Gewoon hier blijven staan!”",
           "Een man komt bij de dokter. “Dokter, kunt u me helpen te zorgen dat ik niet meer zo vreselijk uit mijn mond stink?” Na wat onderzoeken zegt de dokter: “U kunt dit op 2 manieren oplossen. Of u stopt met nagelbijten, of u stopt met het krabben aan uw kont…”",
           ]
rps = ["steen","schaar","papier"]
rpsstart = ["steen, papier, schaar:","steen, papier, schaar dan maar:", "ik kies steen, papier, schaar:", "steen, papier, schaar vindt ik altijd wel oké:"]
commandoError = ["geen flauw idee wat dat is","kun je ook echte commando's geven?", "dat snap ik niet"]
irritatie = ["tjonge, jij stelt veel vragen", "alweer een vraag?","nog eentje?","je kan niet stoppen met vragen, hé"]
now = datetime.now()
running = True
askedQ = 0

def pickanswer(list):
    print(random.choice(list))
def RPS():
    rps1 = input("steen, papier, schaar:")
    rps2 = random.choice(rps)
    print(rps2)
    if rps1 == "steen":
        if rps2 == "steen":
                print("gelijk")
        if rps2 == "papier":
                print("ik win")
        if rps2 == "schaar":
                print("jij wint")
    elif rps1 == "papier":
        if rps2 == "steen":
                print("jij wint")
        if rps2 == "papier":
                print("gelijk")
        if rps2 == "schaar":
                print("ik win")
    elif rps1 == "schaar":
        if rps2 == "steen":
                print("ik win")
        if rps2 == "papier":
                print("jij wint")
        if rps2 == "schaar":
                print("gelijk")
    else:
          print("kies steen, papier of schaar")
          RPS()

pickanswer(begroetingen)
while running:
    print("wat wil je doen:")
    print("- vertel een grap")
    print("- hoe laat is het")
    print("- speel een spel")
    print("- eindig programma")
    command = input()
    askedQ += 1
    if askedQ > 3:
          pickanswer(irritatie)
    if command == "vertel een grap":
        pickanswer(grapstart)
        pickanswer(grappen)
    elif command == "hoe laat is het":
        print("het is nu", now.hour,"uur en", now.minute,"minuten")
    elif command == "speel een spel":
        RPS()
       
    elif command == "eindig programma":
        print("tot ziens")
        running = False
    else:
        pickanswer(commandoError)