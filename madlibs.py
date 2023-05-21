#1. Noun (plural)
#2. Adjective
#3. Verb (past tense)
#4. Adverb
#5. Noun
#6. Adjective
#7. Verb
#8. Noun (plural)
#9. Adjective
#10. Verb (past tense)
#11. Adjective

welcome = print("""\nWelcome to The Wacky Adventure. In this hilarious madlibs game, 
      \nwe'll need some random words to fill in the blanks. 
      \nDon't worry; it's all about having fun and creating a silly story! 
      \nPlease provide the following types of words: """)

noun_1 = input("\nEnter a random noun: ")
adjective_2 = input("Give me an adjective that describes something funny: ")
verb_3 = input("Tell me a verb in past tense: ")
adverb_4 = input("Think of an adverb (e.g., hilariously, clumsily): ")
noun_5 = input("Name a random object or thing: ")
adjective_6 = input("Describe something using an adjective that makes you laugh: ")
verb_7 = input("Provide a verb that indicates a funny action: ")
noun_8 = input("Think of a plural noun: ")
adjective_9 = input("Give me an adjective that describes something silly: ")
verb_10 = input("Tell me a verb (e.g., dance, sing) that makes you chuckle: ")
adjective_11 = input("Describe something using an adjective that makes you giggle: ")

story = f"""Once upon a time, in a land far, far away, there lived a group of {noun_1} who were known for their {adjective_2} shenanigans. One day, they {verb_3} {adverb_4} into a magical {noun_5}. To their surprise, the {adjective_6} {noun_5} transported them to a {verb_7} world filled with talking {noun_8}.

Excited but slightly {adjective_9}, the group {verb_10} around to explore this new land. They encountered a {adjective_11} wizard named Zucchini, who claimed to have the power to grant one wish to each of them.

The first {noun_1} stepped forward and said, "Oh, mighty Zucchini, I wish for a pair of {adjective_2} {noun_8} that can make me fly!" With a wave of his wand, Zucchini turned the {noun_8} into magical wings, and the {noun_1} soared through the sky, laughing like a {adjective_6}.

The second {noun_1} followed suit, saying, "Wise Zucchini, I wish for a {verb_10} {11} hat that can make me invisible!" Zucchini chuckled and transformed the {noun_8} into a hat that could turn anyone invisible. The {noun_1} wore the hat and disappeared, causing everyone else to stumble around, bumping into {noun_8} and giggling uncontrollably.

As each {noun_1} made their wish, the land became more and more {adjective_2} and filled with {adjective_6} creatures. The group laughed, danced, and {verb_7} until they were exhausted. But they couldn't have been happier.

Finally, the last {noun_1} approached Zucchini with a twinkle in their eye. "Oh, magnificent Zucchini, I wish for a giant {verb_3} to make everyone in this world {adjective_11}!" Zucchini burst into laughter, and with a wave of his wand, a massive {verb_3} appeared, causing everyone to burst into uncontrollable fits of {adjective_11}.

And so, the {noun_1} and their newly found friends lived happily ever after, reveling in the joy of their {adjective_2}, {adjective_6}, and {adjective_11} adventures in the wacky world.

The End."""

print(story)