def find_image(base_range, mapping):

    # Start with the entire base range as a segment to consider
    segments_to_consider = [base_range]
    intersections = []
    images=[]
    
    for map in mapping:
        r=(map[1],map[1]+map[2]-1)
        dest=map[0]
        new_segments = []
        for segment in segments_to_consider:
            lower_bound = max(segment[0], r[0])
            upper_bound = min(segment[1], r[1])

            # If there's an intersection, add it to the intersections list
            if lower_bound <= upper_bound:
                intersections.append((lower_bound, upper_bound))
                images.append((dest+(lower_bound-r[0]),dest+(upper_bound-r[0])))
                # Add the non-intersecting parts to the new segments
                if segment[0] < lower_bound:
                    new_segments.append((segment[0], lower_bound-1))
                if upper_bound < segment[1]:
                    new_segments.append((upper_bound+1, segment[1]))
            else:
                # If no intersection, keep the segment as it is
                new_segments.append(segment)

        # Update the segments to consider for the next range
        segments_to_consider = new_segments

    # Combine the intersections and the remaining segments
    total_coverage = intersections + segments_to_consider
    images=images+segments_to_consider
    return images
import re
with open("day5input.txt", "r") as file:
    lines = file.readlines()
maxSeed=0


seeds = [int(num) for num in lines[0].split(":")[1].strip().split(" ")]
seedRanges = [(seeds[i],seeds[i]+seeds[i+1]-1) for i in range(0,len(seeds),2)]

lines=lines[2:]
pattern = r'(\d+)'
maps=[]
mapping=[]
OGseedRanges=seedRanges
for i,line in enumerate(lines):
    if re.findall(pattern, line):
        mapping.append([int(num) for num in re.findall(pattern, line)])
        
    elif line.strip()=="":
        maps.append(mapping)
        tempRanges=[]
        for seedRange in seedRanges:
            tempRanges+=find_image(seedRange,mapping)
        seedRanges=tempRanges
        mapping=[]
possibilities=[seedRanges[0] for seedRanges in seedRanges]
minSeed=min(possibilities)
print(minSeed)


        