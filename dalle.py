from dalle2 import Dalle2
dalle = Dalle2("sess-PpNMhxpECX3BpvXuyhaWKSJhiKUiwfp3pX1PlkEU")

generations = dalle.generate("A few days ago a flood shocked the Valcamonica, snatching the fruits of a whole life of sacrifices from too many people. Citizens deserve quick and concrete solutions: the Lombardy Region responded immediately with the first € 5 million, waiting for the government to decree a State of Emergency.")
print(generations)

file_paths = dalle.download(generations)
print(file_paths)

