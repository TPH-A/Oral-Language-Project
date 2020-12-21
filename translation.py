from translate import Translator

datas = """
Act I Down the Rabbit Hole
(Alice is very bored. At that time, a white rabbit runs by her.)
White Rabbit:Oh! Tin going to be late!
Alice(WJR): (excited) A talking rabbit! I canft believe it.(The White Rabbit jumps into a hole, and Alice follows him.)(Thump! Alice is in a long hallway with many locked doors.)
Alice(WJR):(curiously) Where am I? Oh, what is this?(Alice picks up a small golden key from a glass table.)(opening a door) The key unlocks this small door.(looking through the doorway) What a beautiful garden!I want to go into the garden, but I am too big.(looking around) Oh, that bottle says "DRINK ME” on it.(drinking from the bottle) Oh, I'm getting smaller and smaller!I'm small enough to fit through the door, but it's locked!(looking around again) That cake box says "EAT MEn on it (eating a piece of cake) Oh, no! I'm getting bigger and bigger!Now I'm too big! I can't go into the garden!
Alice starts crying. Soon her tears make a big pool. Suddenly, the White Rabbit runs by Alice.)
(softly) Please, sir Help me. (The White Rabbit is surprised.He drops his gloves and fan and runs away.)
It's very hot!(Alice picks up the gloves and fan and starts to fan herself.)Oh, I'm growing small again!
(Alice runs to get the key, but she slips into the pool of her own tears.) (Alice sees a little mouse splashing in the water.The Mouse and Alice swim to the shore.Many strange birds and animals sit on the shore . Everyone is wet.)
Alice(WJR): (sadly) I miss Dinah.
Alice(WJR): Dinah is my cat. She is a great bird hunter 一 Oh,
I am sorry.
Act II A Mad Tea Party
Alice(WJR):  May I sit down?
Alice(WJR):  (sitting down) There's plenty of room!(The Hatter takes his watch and looks at it.) 
Alice(WJR):  It is Wednesday.
Alice(WJR):  That's strange. The watch tells you the day, but it doesn't tell you the time.
Alice(WJR): No, but it's the same year for a very long time.
Alice(WJR): (saying to herself) Well, I don't really understand.
Alice(WJR): What did they draw?
Alice(WJR): What is muchness? (Nobody answers.)I've never heard of muchness!This is a stupid tea party! (Alice gets up and walks away.)(Alice sees a big tree with a door in it.)
Alice(WJR): How strange! Anyway, I'll go into the door.
(Alice is back in the long hallway again.)(excitedly) Now I can get the key, unlock the door, and go into the garden!
Act III Who Stole the Tarts?
Alice(WJR): Ah-ha! This must be a courtroom!Maybe the Knave of Hearts stole some tarts.The King must be the judge and the twelve birds and animals must be the jury.
Alice(WJR): I can't help it! (The Dormouse suddenly falls asleep.)
Act IV Alice's Evidence
Alice(WJR): Nothing.(The King looks at Alice carefully.)
Alice(WJR): I'm not a mile high, so I'm not leaving! You made that rule just now.
Alice(WJR): Then it should be Rule Number One! (The King's face goes white, but he says nothing.)
Alice(WJR): (turning to the Queen) How foolish you are!
The jury must decide first!
Alice(WJR): I'm not afraid at all. You're only a pack of cards! (The whole pack of cards rises up. They come flying down upon Alice.) Ahhhhhhh! (Alice wakes up and sees her sister.)
Alice(WJR): Oh, I had a dream. It was strange but exciting.
"""
trs = Translator(to_lang="chinese", from_lang="english").translate(datas)
print(trs)
