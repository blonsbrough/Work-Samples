def main():
    dice_rolls_permutations = [
        (a,b,c,d,e)
        for a in range(1,7)
        for b in range(1,7)
        for c in range(1,7)
        for d in range(1,7)
        for e in range(1,7)
    ]

    dice_rolls_combinations = [
        (a,b,c,d,e)
        for a in range(1,7)
        for b in range(a,7)
        for c in range(b,7)
        for d in range(c,7)
        for e in range(d,7)
    ]
    print("Number of permutations: "+str(len(dice_rolls_permutations)))
    print("Number of combinations: "+str(len(dice_rolls_combinations)))

main()