Liste =["I", "dag", "er", "jeg", "så", "lykkelig", "så", "lykkelig", "så", "lykkelig", "det", "hele", "endte", "dejligt", "jeg", "synger", "og", "er", "glad", "Ja", "alting", "endte", "lykkeligt", "så", "lykkeligt", "så", "lykkeligt", "i", "dag", "er", "jeg", "så", "lykkelig", "som", "dagen", "den", "er", "lang"]

print("Det er ",len(Liste)," ord i listen")
print("Det er ",Liste.count("så"), " så i listen ")
print("Det er ",Liste.count("lykkelig"), " lykkelig i listen")
print("Det er ",Liste.count("dag"), " dag i listen ")

Ordbokd ={ "så" : Liste.count("så"), "lykkelig" : Liste.count("lykkelig"), "dag" : Liste.count("dag")}
for e in Ordbokd:
    print(e, ":", Ordbokd[e])
