# dat = "seeds: 79 14 55 13\n\nseed-to-soil map:\n50 98 2\n52 50 48\n\nsoil-to-fertilizer map:\n0 15 37\n37 52 2\n39 0 15\n\nfertilizer-to-water map:\n49 53 8\n0 11 42\n42 0 7\n57 7 4\n\nwater-to-light map:\n88 18 7\n18 25 70\n\nlight-to-temperature map:\n45 77 23\n81 45 19\n68 64 13\n\ntemperature-to-humidity map:\n0 69 1\n1 0 69\n\nhumidity-to-location map:\n60 56 37\n56 93 4"
f = open('/users/natalierobinson/Desktop/github/advent_of_code/2023/day5.txt', 'r')
dat = f.read()

# 1. Map seeds to soils, soils to fertilizers, etc. until the locations are returned. Find the smallest locations
seeds = dat.split("seeds: ")[1].split("\n")[0].split(" ")
mappings = [i.split("\n") for i in dat.split("\n\n")][1:]

locations = []
for s in seeds:
    mapped = int(s)
    i = 0
    while i < len(mappings):
        maps = mappings[i][1:]
        for m in maps:
            nums = m.split(" ") 
            if mapped in range(int(nums[1]),int(nums[1])+int(nums[2])):
                mapped = mapped - int(nums[1]) + int(nums[0])
                break
        i += 1
    locations.append(mapped)
                
        
min(locations)   # 600279879

# 2. Find smallest location if seeds line represents ranges
seeds = dat.split("seeds: ")[1].split("\n")[0].split(" ")
mappings = [i.split("\n") for i in dat.split("\n\n")][1:]

minLocs = []
for s in list(range(0,len(seeds),2)):
    rngSt = int(seeds[s])
    rngEnd = rngSt + int(seeds[s+1]) - 1
    converted = []
    remainder = [[rngSt,rngEnd]]  # Initiate numbers to check
    i = 0
    while i < len(mappings):
        maps = mappings[i][1:] 
        for r in remainder:
            for m in range(len(maps)):
                if len(r) > 0:
                    nums = maps[m].split(" ")
                    st = r[0]
                    end = r[1]
                    r = []
                    if st in range(int(nums[1]),int(nums[1])+int(nums[2])):
                        newSt = st - int(nums[1]) + int(nums[0])
                        if end in range(int(nums[1]),int(nums[1])+int(nums[2])):
                            newEnd = end - int(nums[1]) + int(nums[0])
                        else:
                            newEnd = int(nums[0]) + int(nums[2]) - 1
                            r = [int(nums[1])+int(nums[2]), end]
                        converted.append([newSt, newEnd])
                    else:
                        if end in range(int(nums[1]),int(nums[1])+int(nums[2])):
                            newEnd = end - int(nums[1]) + int(nums[0])
                            newSt = int(nums[0])
                            converted.append([newSt, newEnd])
                            r = [st,int(nums[1])-1]
                        else:
                            r = [st, end]
                    if m == len(maps) - 1:
                        if len(r) > 0:
                            converted.append(r)
        # Initiate the list of ranges for the next iteration    
        remainder = converted  
        converted = []
        i += 1
    # Get min
    minLocs.append(min([min(i) for i in remainder for i in remainder]))
                    
min(minLocs)  # 20191102
  